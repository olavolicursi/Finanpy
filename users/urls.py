"""
URL configuration for the users app.

Placeholder patterns - will be fully implemented in Task 1.5.
"""
from django.urls import path
from django.views.generic import TemplateView

app_name = 'users'

# Placeholder URL patterns for navbar compatibility.
# These will be replaced with real authentication views in Task 1.5.
urlpatterns = [
    path('login/', TemplateView.as_view(template_name='base.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='base.html'), name='register'),
    path('logout/', TemplateView.as_view(template_name='base.html'), name='logout'),
]
