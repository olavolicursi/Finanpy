"""
Core views for the Finanpy project.

Contains public-facing views like the landing page and
placeholder views for features not yet implemented.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def landing_page(request):
    """
    Landing page view.

    Displays the public landing page for unauthenticated visitors.
    Redirects authenticated users to the dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'public/landing.html')


@login_required
def dashboard_placeholder(request):
    """
    Placeholder dashboard view.

    Will be replaced with the real DashboardView in Sprint 2 (Task 2.1).
    For now, renders a simple placeholder page.
    """
    return render(request, 'dashboard/placeholder.html')
