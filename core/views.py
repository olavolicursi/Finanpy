"""
Core views for the Finanpy project.

Contains public-facing views like the landing page.
"""
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
