"""
Transaction views for the Finanpy project.

Provides CRUD views for managing transactions and updates account balance
on create, update, and delete.
"""
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction as db_transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.models import Account
from transactions.forms import TransactionForm
from transactions.models import Transaction


def _apply_transaction_to_balance(account, transaction_type, amount):
    """Apply a single transaction effect to account balance."""
    amount = Decimal(str(amount))
    if transaction_type == 'income':
        account.balance += amount
    else:
        account.balance -= amount
    account.save(update_fields=['balance'])


def _revert_transaction_from_balance(account, transaction_type, amount):
    """Revert a transaction effect from account balance."""
    amount = Decimal(str(amount))
    if transaction_type == 'income':
        account.balance -= amount
    else:
        account.balance += amount
    account.save(update_fields=['balance'])


class TransactionListView(LoginRequiredMixin, ListView):
    """Display a list of all transactions belonging to the logged-in user."""

    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        return (
            Transaction.objects.filter(user=self.request.user)
            .select_related('account', 'category')
            .order_by('-date', '-created_at')
        )


class TransactionCreateView(LoginRequiredMixin, CreateView):
    """Create a new transaction for the logged-in user and update account balance."""

    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        with db_transaction.atomic():
            response = super().form_valid(form)
            account = form.instance.account
            _apply_transaction_to_balance(
                account,
                form.instance.transaction_type,
                form.instance.amount,
            )
        messages.success(self.request, 'Transação criada com sucesso!')
        return response


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    """Edit an existing transaction and recalculate account balance(s)."""

    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')
    context_object_name = 'transaction'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        old = self.object
        old_account = old.account
        old_type = old.transaction_type
        old_amount = old.amount
        new_account = form.cleaned_data['account']
        new_type = form.cleaned_data['transaction_type']
        new_amount = form.cleaned_data['amount']

        with db_transaction.atomic():
            _revert_transaction_from_balance(old_account, old_type, old_amount)
            response = super().form_valid(form)
            account_to_update = Account.objects.get(pk=new_account.pk)
            _apply_transaction_to_balance(account_to_update, new_type, new_amount)
        messages.success(self.request, 'Transação atualizada com sucesso!')
        return response


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a transaction and revert its effect on account balance."""

    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:list')
    context_object_name = 'transaction'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def form_valid(self, form):
        obj = self.object
        with db_transaction.atomic():
            _revert_transaction_from_balance(
                obj.account,
                obj.transaction_type,
                obj.amount,
            )
            response = super().form_valid(form)
        messages.success(self.request, 'Transação excluída com sucesso!')
        return response
