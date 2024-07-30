from django.contrib import admin

from permissions.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name",)
