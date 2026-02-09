"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

from core.views import dashboard_placeholder, landing_page

urlpatterns = [
    path('', landing_page, name='landing'),
    path('dashboard/', dashboard_placeholder, name='dashboard'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/', include('categories.urls')),
    path('transactions/', include('transactions.urls')),
]
