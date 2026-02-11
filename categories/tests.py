"""
Unit tests for the categories app.

Tests Category model, CRUD views, and CategoryForm.
"""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from categories.forms import CategoryForm
from categories.models import Category

User = get_user_model()


class CategoryModelTests(TestCase):
    """Tests for the Category model."""

    def setUp(self):
        self.user = User.objects.create_user(
            email='category@example.com',
            password='testpass123',
        )

    def test_create_category(self):
        """Category can be created with required fields."""
        category = Category.objects.create(
            user=self.user,
            name='Alimentação',
            category_type='expense',
        )
        self.assertEqual(category.name, 'Alimentação')
        self.assertEqual(category.category_type, 'expense')
        self.assertEqual(category.color, '#06b6d4')

    def test_category_str_returns_name(self):
        """__str__ returns the category name."""
        category = Category.objects.create(
            user=self.user,
            name='Salário',
            category_type='income',
        )
        self.assertEqual(str(category), 'Salário')

    def test_category_types_choices(self):
        """Category has expected type choices."""
        self.assertIn(('income', 'Receita'), Category.CATEGORY_TYPES)
        self.assertIn(('expense', 'Despesa'), Category.CATEGORY_TYPES)


class CategoryViewTests(TestCase):
    """Tests for category CRUD views and permissions."""

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
        self.category_a = Category.objects.create(
            user=self.user_a,
            name='Categoria A',
            category_type='expense',
        )

    def test_list_requires_login(self):
        """Category list requires authentication."""
        response = self.client.get(reverse('categories:list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('users:login'), response.url)

    def test_list_shows_only_own_categories(self):
        """User sees only their own categories."""
        self.client.force_login(self.user_a)
        response = self.client.get(reverse('categories:list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
            response.context['categories'],
            [self.category_a],
            transform=lambda x: x,
        )

    def test_create_category_redirects_and_creates(self):
        """Creating category redirects to list and creates record."""
        self.client.force_login(self.user_a)
        response = self.client.post(reverse('categories:create'), {
            'name': 'Nova Categoria',
            'category_type': 'income',
            'icon': '',
            'color': '#10b981',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('categories:list'))
        self.assertTrue(
            Category.objects.filter(
                user=self.user_a, name='Nova Categoria'
            ).exists()
        )

    def test_edit_own_category_succeeds(self):
        """User can edit their own category."""
        self.client.force_login(self.user_a)
        response = self.client.post(
            reverse('categories:edit', args=[self.category_a.pk]),
            {
                'name': 'Categoria A Atualizada',
                'category_type': 'expense',
                'icon': '',
                'color': '#06b6d4',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.category_a.refresh_from_db()
        self.assertEqual(self.category_a.name, 'Categoria A Atualizada')

    def test_user_cannot_edit_other_user_category(self):
        """User cannot edit another user's category (404)."""
        self.client.force_login(self.user_b)
        response = self.client.get(
            reverse('categories:edit', args=[self.category_a.pk])
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_own_category_succeeds(self):
        """User can delete their own category."""
        self.client.force_login(self.user_a)
        response = self.client.post(
            reverse('categories:delete', args=[self.category_a.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(pk=self.category_a.pk).exists())


class CategoryFormTests(TestCase):
    """Tests for CategoryForm validation."""

    def test_form_with_valid_data(self):
        """Form is valid with correct data."""
        form = CategoryForm(data={
            'name': 'Transporte',
            'category_type': 'expense',
            'icon': 'car',
            'color': '#06b6d4',
        })
        self.assertTrue(form.is_valid())

    def test_form_has_expected_fields(self):
        """Form contains expected fields."""
        form = CategoryForm()
        self.assertIn('name', form.fields)
        self.assertIn('category_type', form.fields)
        self.assertIn('icon', form.fields)
        self.assertIn('color', form.fields)
