"""
# app/core/admin.py

Create and Design Django Admin Page Layout
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Importing translation feature to translate information
from django.utils.translation import gettext_lazy as translate
from . import models


# Register your models here.
class UserAdmin(BaseUserAdmin):
    """Define the sections, groups and fields in Django Admin."""
    ordering = ['id']
    list_display = ['name', 'email']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),

        (translate('Permissions'), {'fields': (
            'is_active',
            'is_superuser',
            'is_staff',
        )}),

        (translate('Important Dates'), {'fields': (
            'last_login',
        )}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_superuser',
                'is_staff'
            )
        }),

    )


admin.site.register(models.User, UserAdmin)
