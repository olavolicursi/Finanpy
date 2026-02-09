from django.contrib import admin

from accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Admin configuration for the Account model."""

    list_display = ('name', 'user', 'account_type', 'balance', 'color', 'is_active', 'created_at')
    list_filter = ('account_type', 'is_active', 'user')
    search_fields = ('name', 'user__email')
    list_per_page = 25
    readonly_fields = ('created_at', 'updated_at')
