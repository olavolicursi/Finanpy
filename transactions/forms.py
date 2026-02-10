"""
Transaction forms for the Finanpy project.

Provides the TransactionForm for creating and editing transactions,
styled with TailwindCSS and filtering accounts/categories by user.
"""
from django import forms

from accounts.models import Account
from categories.models import Category
from transactions.models import Transaction

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


class TransactionForm(forms.ModelForm):
    """
    Form for creating and editing transactions.

    Fields: transaction_type, account, category, amount, date, description.
    Account and category querysets are filtered by user in __init__.
    The user field is assigned in the view's form_valid method.
    """

    class Meta:
        model = Transaction
        fields = [
            'transaction_type',
            'account',
            'category',
            'amount',
            'date',
            'description',
        ]
        labels = {
            'transaction_type': 'Tipo',
            'account': 'Conta',
            'category': 'Categoria',
            'amount': 'Valor',
            'date': 'Data',
            'description': 'Descrição',
        }
        help_texts = {
            'description': 'Opcional. Breve descrição da transação.',
        }
        widgets = {
            'transaction_type': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'account': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'category': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'amount': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': TAILWIND_INPUT_CLASSES,
            }),
            'description': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: Supermercado, Salário...',
                'autocomplete': 'off',
            }),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['account'].queryset = (
                Account.objects.filter(user=user).order_by('name')
            )
            self.fields['category'].queryset = (
                Category.objects.filter(user=user).order_by('category_type', 'name')
            )
