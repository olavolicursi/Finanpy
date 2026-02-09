"""
Category models for the Finanpy project.

Defines the Category model used to classify transactions
as either income or expense types.
"""
from django.conf import settings
from django.db import models


class Category(models.Model):
    """
    Represents a transaction category belonging to a user.

    Categories are used to classify transactions into logical
    groups (e.g., 'Salário', 'Alimentação', 'Transporte').
    Each category has a type: income (Receita) or expense (Despesa).
    """

    CATEGORY_TYPES = [
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='usuário',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='nome',
    )
    category_type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPES,
        verbose_name='tipo',
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='ícone',
        help_text='Nome do ícone (ex: home, car, food)',
    )
    color = models.CharField(
        max_length=7,
        default='#06b6d4',
        verbose_name='cor',
        help_text='Cor em formato hexadecimal (ex: #06b6d4)',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='atualizado em',
    )

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['category_type', 'name']

    def __str__(self):
        return self.name
