"""
Account models for the Finanpy project.

Defines the Account model representing a user's bank accounts,
wallets, and other financial containers.
"""
from django.conf import settings
from django.db import models


class Account(models.Model):
    """
    Represents a financial account (bank account, wallet, etc.)
    belonging to a user.

    Each user can have multiple accounts of different types.
    The balance is updated whenever transactions are created,
    edited, or deleted (handled in the transactions app).
    """

    ACCOUNT_TYPES = [
        ('checking', 'Conta Corrente'),
        ('savings', 'Poupança'),
        ('investment', 'Investimento'),
        ('cash', 'Dinheiro'),
        ('other', 'Outro'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='accounts',
        verbose_name='usuário',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='nome',
    )
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPES,
        verbose_name='tipo de conta',
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='saldo',
    )
    color = models.CharField(
        max_length=7,
        default='#06b6d4',
        verbose_name='cor',
        help_text='Cor em formato hexadecimal (ex: #06b6d4)',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='ativa',
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
        verbose_name = 'conta'
        verbose_name_plural = 'contas'
        ordering = ['name']

    def __str__(self):
        return self.name
