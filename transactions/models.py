"""
Transaction models for the Finanpy project.

Defines the Transaction model representing financial movements
(income and expenses) linked to accounts and categories.
"""
from django.conf import settings
from django.db import models


class Transaction(models.Model):
    """
    Represents a financial transaction (income or expense)
    belonging to a user.

    Each transaction is linked to an account and optionally
    to a category. The account balance is updated when
    transactions are created, edited, or deleted
    (handled in the views/signals layer).
    """

    TRANSACTION_TYPES = [
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='usuário',
    )
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='conta',
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transactions',
        verbose_name='categoria',
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        verbose_name='tipo',
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='valor',
    )
    date = models.DateField(
        verbose_name='data',
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='descrição',
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
        verbose_name = 'transação'
        verbose_name_plural = 'transações'
        ordering = ['-date', '-created_at']

    def __str__(self):
        if self.description:
            return self.description
        return f'{self.get_transaction_type_display()} - R$ {self.amount}'
