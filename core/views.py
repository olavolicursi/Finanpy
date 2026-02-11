"""
Core views for the Finanpy project.

Contains public-facing views like the landing page and
the main dashboard view for authenticated users.
"""
from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import TemplateView

from accounts.models import Account
from transactions.models import Transaction


def landing_page(request):
    """
    Landing page view.

    Displays the public landing page for unauthenticated visitors.
    Redirects authenticated users to the dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'public/landing.html')


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Main dashboard view.

    Displays the financial overview for the authenticated user,
    including total balance, monthly income/expenses, recent
    transactions, and account balances.
    """

    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        now = timezone.now()

        # Saldo total: soma dos saldos de todas as contas do usuário
        accounts = list(
            Account.objects.filter(user=user, is_active=True).order_by('name')
        )
        total_balance = sum((a.balance for a in accounts), Decimal('0'))

        # Receitas e despesas do mês atual
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        month_transactions = Transaction.objects.filter(
            user=user,
            date__gte=month_start,
            date__lte=now,
        )
        monthly_income = (
            month_transactions.filter(transaction_type='income').aggregate(
                total=Sum('amount')
            )['total']
            or Decimal('0')
        )
        monthly_expenses = (
            month_transactions.filter(transaction_type='expense').aggregate(
                total=Sum('amount')
            )['total']
            or Decimal('0')
        )
        monthly_balance = monthly_income - monthly_expenses

        # Últimas 5 transações
        recent_transactions = (
            Transaction.objects.filter(user=user)
            .select_related('account', 'category')
            .order_by('-date', '-created_at')[:5]
        )

        context.update({
            'total_balance': total_balance,
            'monthly_income': monthly_income,
            'monthly_expenses': monthly_expenses,
            'monthly_balance': monthly_balance,
            'recent_transactions': recent_transactions,
            'accounts': accounts,
        })
        return context
