"""
URL configuration for the accounts app.

Provides routes for the full CRUD of bank accounts:
- list: Display all accounts for the logged-in user.
- create: Form to create a new account.
- edit: Form to update an existing account.
- delete: Confirmation page to delete an account.
"""
from django.urls import path

from accounts.views import (
    AccountCreateView,
    AccountDeleteView,
    AccountListView,
    AccountUpdateView,
)

app_name = 'accounts'

urlpatterns = [
    path('', AccountListView.as_view(), name='list'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', AccountUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='delete'),
]
