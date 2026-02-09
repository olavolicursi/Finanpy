"""
Account views for the Finanpy project.

Provides CRUD views for managing bank accounts:
- AccountListView: Lists all accounts for the logged-in user.
- AccountCreateView: Creates a new account for the logged-in user.
- AccountUpdateView: Edits an existing account owned by the logged-in user.
- AccountDeleteView: Deletes an account owned by the logged-in user.
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.forms import AccountForm
from accounts.models import Account


class AccountListView(LoginRequiredMixin, ListView):
    """Display a list of all accounts belonging to the logged-in user."""

    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).order_by('name')


class AccountCreateView(LoginRequiredMixin, CreateView):
    """Create a new bank account for the logged-in user."""

    model = Account
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('accounts:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Conta criada com sucesso!')
        return super().form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """Edit an existing bank account owned by the logged-in user."""

    model = Account
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('accounts:list')

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Conta atualizada com sucesso!')
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a bank account owned by the logged-in user."""

    model = Account
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('accounts:list')

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Conta excluída com sucesso!')
        return super().form_valid(form)
