"""
Unit tests for the users app.

Tests User model, authentication views, and UserRegistrationForm.
"""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from users.forms import UserRegistrationForm

User = get_user_model()


class UserModelTests(TestCase):
    """Tests for the custom User model."""

    def test_create_user_with_email(self):
        """User can be created with email and password."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_email_normalized(self):
        """Email domain is normalized to lowercase."""
        user = User.objects.create_user(
            email='Test@EXAMPLE.com',
            password='testpass123',
        )
        # Django's normalize_email lowercases the domain part
        self.assertEqual(user.email, 'Test@example.com')

    def test_create_user_without_email_raises(self):
        """Creating user without email raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            User.objects.create_user(email='', password='testpass123')
        self.assertIn('email', str(cm.exception).lower())

    def test_create_superuser(self):
        """Superuser can be created with is_staff and is_superuser True."""
        user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_user_str_returns_email(self):
        """__str__ returns the user's email."""
        user = User.objects.create_user(
            email='str@example.com',
            password='testpass123',
        )
        self.assertEqual(str(user), 'str@example.com')

    def test_username_field_is_email(self):
        """USERNAME_FIELD is set to email."""
        self.assertEqual(User.USERNAME_FIELD, 'email')

    def test_required_fields_empty(self):
        """REQUIRED_FIELDS is empty (email is the only identifier)."""
        self.assertEqual(User.REQUIRED_FIELDS, [])


class AuthenticationViewTests(TestCase):
    """Tests for registration, login and logout views."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='auth@example.com',
            password='authpass123',
            first_name='Auth',
            last_name='User',
        )

    def test_register_page_returns_200(self):
        """Registration page loads successfully."""
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_creates_user_and_redirects(self):
        """Valid registration creates user and redirects to login."""
        response = self.client.post(reverse('users:register'), {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com',
            'password1': 'newpass123!',
            'password2': 'newpass123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(email='new@example.com').exists())

    def test_login_page_returns_200(self):
        """Login page loads successfully."""
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials_redirects_to_dashboard(self):
        """Login with valid email/password redirects to dashboard."""
        response = self.client.post(reverse('users:login'), {
            'username': 'auth@example.com',
            'password': 'authpass123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_authenticated_user_redirected_from_register(self):
        """Authenticated user visiting register is redirected to dashboard."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_logout_redirects_to_login(self):
        """Logout redirects to login page."""
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))


class UserRegistrationFormTests(TestCase):
    """Tests for UserRegistrationForm validation."""

    def test_form_with_valid_data(self):
        """Form is valid with correct data."""
        form = UserRegistrationForm(data={
            'first_name': 'Form',
            'last_name': 'Test',
            'email': 'form@example.com',
            'password1': 'ValidPass123!',
            'password2': 'ValidPass123!',
        })
        self.assertTrue(form.is_valid())

    def test_form_with_mismatched_passwords(self):
        """Form is invalid when passwords do not match."""
        form = UserRegistrationForm(data={
            'first_name': 'Form',
            'last_name': 'Test',
            'email': 'form@example.com',
            'password1': 'ValidPass123!',
            'password2': 'OtherPass456!',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_form_with_duplicate_email(self):
        """Form is invalid when email already exists."""
        User.objects.create_user(
            email='taken@example.com',
            password='existing123',
        )
        form = UserRegistrationForm(data={
            'first_name': 'Form',
            'last_name': 'Test',
            'email': 'taken@example.com',
            'password1': 'ValidPass123!',
            'password2': 'ValidPass123!',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_required_fields(self):
        """Form has required fields."""
        form = UserRegistrationForm()
        for field in ('first_name', 'last_name', 'email', 'password1', 'password2'):
            self.assertIn(field, form.fields)
