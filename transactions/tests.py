"""
Unit tests for the transactions app.

Tests Transaction model, CRUD views, permissions, and TransactionForm.
"""
from decimal import Decimal
from datetime import date

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Account
from categories.models import Category
from transactions.forms import TransactionForm
from transactions.models import Transaction

User = get_user_model()


class TransactionModelTests(TestCase):
    """Tests for the Transaction model."""

    def setUp(self):
        self.user = User.objects.create_user(
            email='tx@example.com',
            password='testpass123',
        )
        self.account = Account.objects.create(
            user=self.user,
            name='Conta Teste',
            account_type='checking',
            balance=Decimal('1000.00'),
        )

    def test_create_transaction(self):
        """Transaction can be created with required fields."""
        tx = Transaction.objects.create(
            user=self.user,
            account=self.account,
            transaction_type='expense',
            amount=Decimal('50.00'),
            date=date.today(),
        )
        self.assertEqual(tx.transaction_type, 'expense')
        self.assertEqual(tx.amount, Decimal('50.00'))
        self.assertEqual(tx.account, self.account)

    def test_transaction_str_with_description(self):
        """__str__ returns description when set."""
        tx = Transaction.objects.create(
            user=self.user,
            account=self.account,
            transaction_type='income',
            amount=Decimal('100.00'),
            date=date.today(),
            description='Salário',
        )
        self.assertEqual(str(tx), 'Salário')

    def test_transaction_str_without_description(self):
        """__str__ returns type and amount when description is empty."""
        tx = Transaction.objects.create(
            user=self.user,
            account=self.account,
            transaction_type='income',
            amount=Decimal('100.00'),
            date=date.today(),
        )
        self.assertIn('Receita', str(tx))
        self.assertIn('100', str(tx))

    def test_transaction_types_choices(self):
        """Transaction has expected type choices."""
        self.assertIn(('income', 'Receita'), Transaction.TRANSACTION_TYPES)
        self.assertIn(('expense', 'Despesa'), Transaction.TRANSACTION_TYPES)


class TransactionViewTests(TestCase):
    """Tests for transaction CRUD views and permissions."""

    def setUp(self):
        self.client = Client()
        self.user_a = User.objects.create_user(
            email='usera@example.com',
            password='pass123',
        )
        self.user_b = User.objects.create_user(
            email='userb@example.com',
            password='pass123',
        )
        self.account_a = Account.objects.create(
            user=self.user_a,
            name='Conta A',
            account_type='checking',
            balance=Decimal('500.00'),
        )
        self.category_a = Category.objects.create(
            user=self.user_a,
            name='Categoria A',
            category_type='expense',
        )
        self.transaction_a = Transaction.objects.create(
            user=self.user_a,
            account=self.account_a,
            category=self.category_a,
            transaction_type='expense',
            amount=Decimal('50.00'),
            date=date.today(),
            description='Teste',
        )

    def test_list_requires_login(self):
        """Transaction list requires authentication."""
        response = self.client.get(reverse('transactions:list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('users:login'), response.url)

    def test_list_shows_only_own_transactions(self):
        """User sees only their own transactions."""
        self.client.force_login(self.user_a)
        response = self.client.get(reverse('transactions:list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context['transactions'],
            [self.transaction_a],
            transform=lambda x: x,
        )

    def test_create_transaction_redirects_and_creates(self):
        """Creating transaction redirects to list and creates record."""
        self.client.force_login(self.user_a)
        response = self.client.post(reverse('transactions:create'), {
            'transaction_type': 'income',
            'account': self.account_a.pk,
            'category': self.category_a.pk,
            'amount': '100.00',
            'date': date.today().isoformat(),
            'description': 'Nova receita',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('transactions:list'))
        self.assertTrue(
            Transaction.objects.filter(
                user=self.user_a, description='Nova receita'
            ).exists()
        )

    def test_edit_own_transaction_succeeds(self):
        """User can edit their own transaction."""
        self.client.force_login(self.user_a)
        response = self.client.post(
            reverse('transactions:edit', args=[self.transaction_a.pk]),
            {
                'transaction_type': 'expense',
                'account': self.account_a.pk,
                'category': self.category_a.pk,
                'amount': '75.00',
                'date': date.today().isoformat(),
                'description': 'Editado',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.transaction_a.refresh_from_db()
        self.assertEqual(self.transaction_a.description, 'Editado')
        self.assertEqual(self.transaction_a.amount, Decimal('75.00'))

    def test_user_cannot_edit_other_user_transaction(self):
        """User cannot edit another user's transaction (404)."""
        self.client.force_login(self.user_b)
        response = self.client.get(
            reverse('transactions:edit', args=[self.transaction_a.pk])
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_own_transaction_succeeds(self):
        """User can delete their own transaction."""
        self.client.force_login(self.user_a)
        response = self.client.post(
            reverse('transactions:delete', args=[self.transaction_a.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Transaction.objects.filter(pk=self.transaction_a.pk).exists()
        )

    def test_user_cannot_see_other_user_transactions(self):
        """User B does not see User A's transactions in list."""
        self.client.force_login(self.user_b)
        response = self.client.get(reverse('transactions:list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['transactions']), 0)


class TransactionFormTests(TestCase):
    """Tests for TransactionForm validation and user filtering."""

    def setUp(self):
        self.user = User.objects.create_user(
            email='form@example.com',
            password='testpass123',
        )
        self.account = Account.objects.create(
            user=self.user,
            name='Conta',
            account_type='checking',
            balance=Decimal('0'),
        )
        self.category = Category.objects.create(
            user=self.user,
            name='Cat',
            category_type='expense',
        )

    def test_form_with_valid_data(self):
        """Form is valid with correct data when user is passed."""
        form = TransactionForm(
            user=self.user,
            data={
                'transaction_type': 'expense',
                'account': self.account.pk,
                'category': self.category.pk,
                'amount': '25.00',
                'date': date.today().isoformat(),
                'description': 'Test',
            },
        )
        self.assertTrue(form.is_valid())

    def test_form_has_expected_fields(self):
        """Form contains expected fields."""
        form = TransactionForm(user=self.user)
        self.assertIn('transaction_type', form.fields)
        self.assertIn('account', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('amount', form.fields)
        self.assertIn('date', form.fields)
        self.assertIn('description', form.fields)

    def test_form_filters_accounts_by_user(self):
        """Account queryset only includes user's accounts."""
        other_user = User.objects.create_user(
            email='other@example.com',
            password='pass123',
        )
        other_account = Account.objects.create(
            user=other_user,
            name='Outra Conta',
            account_type='checking',
            balance=Decimal('0'),
        )
        form = TransactionForm(user=self.user)
        account_pks = list(form.fields['account'].queryset.values_list('pk', flat=True))
        self.assertIn(self.account.pk, account_pks)
        self.assertNotIn(other_account.pk, account_pks)
