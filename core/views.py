"""
Core views for the Finanpy project.

Contains public-facing views like the landing page and
the main dashboard view for authenticated users.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


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

    Context data will be populated with real values in Sprint 6 (Task 6.1).
    For now, placeholder values are provided.
    """

    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Placeholder context — will be populated with real data in Sprint 6
        context.update({
            'total_balance': 0,
            'monthly_income': 0,
            'monthly_expenses': 0,
            'monthly_balance': 0,
            'recent_transactions': [],
            'accounts': [],
        })
        return context
