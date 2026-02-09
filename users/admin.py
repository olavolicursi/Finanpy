from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom admin configuration for the User model.
    Adapted to use email instead of username.
    """
    
    # Fields to display in list view
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'created_at',
    )
    
    # Fields to filter by
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'created_at',
    )
    
    # Fields to search by
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    
    # Ordering in list view
    ordering = ('-created_at',)
    
    # Read-only fields
    readonly_fields = ('created_at', 'updated_at', 'last_login', 'date_joined')
    
    # Fieldsets for the edit form
    fieldsets = (
        (None, {
            'fields': ('email', 'password'),
        }),
        (_('Informações Pessoais'), {
            'fields': ('first_name', 'last_name'),
        }),
        (_('Permissões'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Datas Importantes'), {
            'fields': ('last_login', 'date_joined', 'created_at', 'updated_at'),
        }),
    )
    
    # Fieldsets for the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
            ),
        }),
    )
