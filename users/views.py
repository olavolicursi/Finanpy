"""
Authentication views for the Finanpy application.

Provides registration, login and logout views using
email-based authentication.
"""
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserRegistrationForm


class RegisterView(CreateView):
    """
    User registration view.

    Creates a new user account with first_name, last_name,
    email and password. Redirects to login page on success.
    """

    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Add success message after successful registration."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Conta criada com sucesso! Faça login para continuar.',
        )
        return response

    def dispatch(self, request, *args, **kwargs):
        """Redirect authenticated users to the dashboard."""
        if request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(auth_views.LoginView):
    """
    Custom login view using email-based authentication.

    Uses the UserLoginForm which accepts email instead of username.
    Redirects to dashboard after successful login.
    """

    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Add welcome message after successful login."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            f'Bem-vindo(a), {self.request.user.first_name or self.request.user.email}!',
        )
        return response

    def get_default_redirect_url(self):
        """Redirect to dashboard after login."""
        return reverse_lazy('dashboard')


class CustomLogoutView(auth_views.LogoutView):
    """
    Custom logout view.

    Logs the user out and redirects to the login page.
    """

    next_page = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        """Add goodbye message before logout."""
        if request.user.is_authenticated:
            messages.info(request, 'Você saiu da sua conta.')
        return super().dispatch(request, *args, **kwargs)
