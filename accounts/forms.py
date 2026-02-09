"""
Account forms for the Finanpy project.

Provides the AccountForm for creating and editing bank accounts,
styled with TailwindCSS classes matching the project's design system.
"""
from django import forms

from accounts.models import Account

# Shared Tailwind CSS classes for form widgets
TAILWIND_INPUT_CLASSES = (
    'w-full px-4 py-2.5 bg-gray-800 border border-gray-700 rounded-lg '
    'text-gray-100 placeholder-gray-500 focus:outline-none focus:border-cyan-500 '
    'focus:ring-1 focus:ring-cyan-500 transition-colors duration-200'
)

TAILWIND_SELECT_CLASSES = (
    'w-full px-4 py-2.5 bg-gray-800 border border-gray-700 rounded-lg '
    'text-gray-100 focus:outline-none focus:border-cyan-500 '
    'focus:ring-1 focus:ring-cyan-500 transition-colors duration-200'
)

TAILWIND_COLOR_CLASSES = (
    'w-full h-11 bg-gray-800 border border-gray-700 rounded-lg '
    'cursor-pointer focus:outline-none focus:border-cyan-500 '
    'focus:ring-1 focus:ring-cyan-500 transition-colors duration-200'
)


class AccountForm(forms.ModelForm):
    """
    Form for creating and editing bank accounts.

    Fields: name, account_type, balance, color.
    The user field is assigned in the view's form_valid method.
    """

    class Meta:
        model = Account
        fields = ['name', 'account_type', 'balance', 'color']
        labels = {
            'name': 'Nome da Conta',
            'account_type': 'Tipo de Conta',
            'balance': 'Saldo Inicial',
            'color': 'Cor',
        }
        help_texts = {
            'balance': 'Informe o saldo atual da conta.',
            'color': 'Escolha uma cor para identificar a conta.',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: Banco do Brasil, Nubank...',
                'autocomplete': 'off',
            }),
            'account_type': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'balance': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
            }),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': TAILWIND_COLOR_CLASSES,
            }),
        }
