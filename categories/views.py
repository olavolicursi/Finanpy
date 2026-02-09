"""
Category views for the Finanpy project.

Provides CRUD views for managing transaction categories:
- CategoryListView: Lists all categories for the logged-in user.
- CategoryCreateView: Creates a new category for the logged-in user.
- CategoryUpdateView: Edits an existing category owned by the logged-in user.
- CategoryDeleteView: Deletes a category owned by the logged-in user.
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from categories.forms import CategoryForm
from categories.models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    """Display a list of all categories belonging to the logged-in user."""

    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user).order_by('category_type', 'name')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """Create a new transaction category for the logged-in user."""

    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Categoria criada com sucesso!')
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """Edit an existing category owned by the logged-in user."""

    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Categoria atualizada com sucesso!')
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a category owned by the logged-in user."""

    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('categories:list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Categoria excluída com sucesso!')
        return super().form_valid(form)
