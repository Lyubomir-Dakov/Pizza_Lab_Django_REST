from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from pizza_lab.accounts.forms import AppUserCreationForm, UserEditForm
from pizza_lab.accounts.models import CustomUser

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = UserEditForm
    model = CustomUser

    list_display = ['email', 'is_staff', 'is_active', 'last_login', 'is_superuser']
    list_filter = ['email', 'is_staff', 'is_active', 'is_superuser']

    fieldsets = [
        ['Base Information', {'fields': ['email', 'date_joined']}],
        ['Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups',)}]
    ]

    add_fieldsets = [
        ['Base information', {'fields': ['email', 'password1', 'password2']}],
        ['User status', {'fields': ['is_staff', 'is_active', 'is_superuser']}]
    ]

    ordering = ['email']
    search_fields = ['email']
    readonly_fields = ['date_joined']
