"""
Category forms for the Finanpy project.

Provides the CategoryForm for creating and editing transaction categories,
styled with TailwindCSS classes matching the project's design system.
"""
from django import forms

from categories.models import Category

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


class CategoryForm(forms.ModelForm):
    """
    Form for creating and editing transaction categories.

    Fields: name, category_type, icon, color.
    The user field is assigned in the view's form_valid method.
    """

    class Meta:
        model = Category
        fields = ['name', 'category_type', 'icon', 'color']
        labels = {
            'name': 'Nome da Categoria',
            'category_type': 'Tipo',
            'icon': 'Ícone',
            'color': 'Cor',
        }
        help_texts = {
            'icon': 'Nome do ícone para identificar a categoria (ex: home, car, food).',
            'color': 'Escolha uma cor para identificar a categoria.',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: Alimentação, Salário, Transporte...',
                'autocomplete': 'off',
            }),
            'category_type': forms.Select(
                choices=Category.CATEGORY_TYPES,
                attrs={
                    'class': TAILWIND_SELECT_CLASSES,
                },
            ),
            'icon': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: home, car, food...',
            }),
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': TAILWIND_COLOR_CLASSES,
            }),
        }
