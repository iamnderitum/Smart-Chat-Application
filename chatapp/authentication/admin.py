"""
Django admin customization
"""
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Define the Admin pages for users."""
    ordering = ["id",]
    list_display = ("email", "name", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissins"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            }
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "name",
                "is_active",
                "is_staff",
                "is_superuser",
            )
        }),
    )
