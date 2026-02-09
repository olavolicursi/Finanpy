from django.contrib import admin

from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin configuration for the Transaction model."""

    list_display = ('description', 'user', 'transaction_type', 'amount', 'account', 'category', 'date')
    list_filter = ('transaction_type', 'account', 'category', 'user')
    search_fields = ('description', 'user__email')
    date_hierarchy = 'date'
    list_per_page = 25
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('user', 'account', 'category')
