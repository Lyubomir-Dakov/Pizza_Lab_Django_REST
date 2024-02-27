from django.contrib import admin

from pizza_lab.accounts.models import Employee  # type: ignore


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
