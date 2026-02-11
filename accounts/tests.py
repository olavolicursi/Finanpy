"""
Unit tests for the accounts app.

Tests Account model, CRUD views, and AccountForm.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from accounts.forms import AccountForm
from accounts.models import Account

User = get_user_model()


class AccountModelTests(TestCase):
    """Tests for the Account model."""

    def setUp(self):
        self.user = User.objects.create_user(
            email='account@example.com',
            password='testpass123',
        )

    def test_create_account(self):
        """Account can be created with required fields."""
        account = Account.objects.create(
            user=self.user,
            name='Conta Teste',
            account_type='checking',
            balance=Decimal('1000.00'),
        )
        self.assertEqual(account.name, 'Conta Teste')
        self.assertEqual(account.account_type, 'checking')
        self.assertEqual(account.balance, Decimal('1000.00'))
        self.assertTrue(account.is_active)
        self.assertEqual(account.color, '#06b6d4')

    def test_account_str_returns_name(self):
        """__str__ returns the account name."""
        account = Account.objects.create(
            user=self.user,
            name='Minha Conta',
            account_type='savings',
            balance=Decimal('0'),
        )
        self.assertEqual(str(account), 'Minha Conta')

    def test_account_types_choices(self):
        """Account has expected type choices."""
        self.assertIn(('checking', 'Conta Corrente'), Account.ACCOUNT_TYPES)
        self.assertIn(('savings', 'Poupança'), Account.ACCOUNT_TYPES)


class AccountViewTests(TestCase):
    """Tests for account CRUD views and permissions."""

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

    def test_list_requires_login(self):
        """Account list requires authentication."""
        response = self.client.get(reverse('accounts:list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('users:login'), response.url)

    def test_list_shows_only_own_accounts(self):
        """User sees only their own accounts."""
        self.client.force_login(self.user_a)
        response = self.client.get(reverse('accounts:list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context['accounts'],
            [self.account_a],
            transform=lambda x: x,
        )

    def test_create_account_redirects_and_creates(self):
        """Creating account redirects to list and creates record."""
        self.client.force_login(self.user_a)
        response = self.client.post(reverse('accounts:create'), {
            'name': 'Nova Conta',
            'account_type': 'savings',
            'balance': '200.00',
            'color': '#10b981',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:list'))
        self.assertTrue(
            Account.objects.filter(user=self.user_a, name='Nova Conta').exists()
        )

    def test_edit_own_account_succeeds(self):
        """User can edit their own account."""
        self.client.force_login(self.user_a)
        response = self.client.post(
            reverse('accounts:edit', args=[self.account_a.pk]),
            {
                'name': 'Conta A Atualizada',
                'account_type': 'checking',
                'balance': '600.00',
                'color': '#06b6d4',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.account_a.refresh_from_db()
        self.assertEqual(self.account_a.name, 'Conta A Atualizada')

    def test_user_cannot_edit_other_user_account(self):
        """User cannot edit another user's account (404)."""
        self.client.force_login(self.user_b)
        response = self.client.get(
            reverse('accounts:edit', args=[self.account_a.pk])
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_own_account_succeeds(self):
        """User can delete their own account."""
        self.client.force_login(self.user_a)
        response = self.client.post(
            reverse('accounts:delete', args=[self.account_a.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Account.objects.filter(pk=self.account_a.pk).exists())


class AccountFormTests(TestCase):
    """Tests for AccountForm validation."""

    def setUp(self):
        self.user = User.objects.create_user(
            email='form@example.com',
            password='testpass123',
        )

    def test_form_with_valid_data(self):
        """Form is valid with correct data."""
        form = AccountForm(data={
            'name': 'Conta Form',
            'account_type': 'checking',
            'balance': '100.00',
            'color': '#06b6d4',
        })
        self.assertTrue(form.is_valid())

    def test_form_has_expected_fields(self):
        """Form contains expected fields."""
        form = AccountForm()
        self.assertIn('name', form.fields)
        self.assertIn('account_type', form.fields)
        self.assertIn('balance', form.fields)
        self.assertIn('color', form.fields)
