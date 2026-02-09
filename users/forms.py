"""
Authentication forms for the Finanpy application.

Provides custom registration and login forms that use email
as the primary identifier instead of username.
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()

# Shared Tailwind CSS classes for form widgets
TAILWIND_INPUT_CLASSES = (
    'w-full px-4 py-2.5 bg-gray-800 border border-gray-700 rounded-lg '
    'text-gray-100 placeholder-gray-500 focus:outline-none focus:border-cyan-500 '
    'focus:ring-1 focus:ring-cyan-500 transition-colors duration-200'
)

TAILWIND_INPUT_ERROR_CLASSES = (
    'w-full px-4 py-2.5 bg-gray-800 border border-red-500 rounded-lg '
    'text-gray-100 placeholder-gray-500 focus:outline-none focus:border-red-500 '
    'focus:ring-1 focus:ring-red-500 transition-colors duration-200'
)


class UserRegistrationForm(UserCreationForm):
    """
    Registration form with first_name, last_name, email, password1, password2.

    Uses email as the unique identifier for the user account.
    """

    first_name = forms.CharField(
        label='Nome',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Seu nome',
            'autocomplete': 'given-name',
        }),
    )

    last_name = forms.CharField(
        label='Sobrenome',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Seu sobrenome',
            'autocomplete': 'family-name',
        }),
    )

    email = forms.EmailField(
        label='Email',
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'seu@email.com',
            'autocomplete': 'email',
        }),
    )

    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Mínimo 8 caracteres',
            'autocomplete': 'new-password',
        }),
    )

    password2 = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Repita a senha',
            'autocomplete': 'new-password',
        }),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add error styling to fields with errors
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs['class'] = TAILWIND_INPUT_ERROR_CLASSES


class UserLoginForm(AuthenticationForm):
    """
    Login form customized to use email instead of username.

    Inherits from Django's AuthenticationForm and overrides
    the username field to accept email addresses.
    """

    username = forms.EmailField(
        label='Email',
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'seu@email.com',
            'autocomplete': 'email',
            'autofocus': True,
        }),
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Sua senha',
            'autocomplete': 'current-password',
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add error styling to fields with errors
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs['class'] = TAILWIND_INPUT_ERROR_CLASSES
