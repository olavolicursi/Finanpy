"""
URL configuration for the categories app.

Placeholder patterns - will be fully implemented in Sprint 4.
"""
from django.urls import path
from django.views.generic import TemplateView

app_name = 'categories'

# Placeholder URL patterns for sidebar navigation compatibility.
urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='list'),
]
