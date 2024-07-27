from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    list_display = ("email", "name", "is_active")
