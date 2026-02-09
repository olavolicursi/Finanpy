"""
URL configuration for the categories app.

Provides routes for the full CRUD of transaction categories:
- list: Display all categories for the logged-in user.
- create: Form to create a new category.
- edit: Form to update an existing category.
- delete: Confirmation page to delete a category.
"""
from django.urls import path

from categories.views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)

app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete'),
]
