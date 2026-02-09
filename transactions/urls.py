"""
URL configuration for the transactions app.

Placeholder patterns - will be fully implemented in Sprint 5.
"""
from django.urls import path
from django.views.generic import TemplateView

app_name = 'transactions'

# Placeholder URL patterns for sidebar navigation compatibility.
urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='list'),
]
