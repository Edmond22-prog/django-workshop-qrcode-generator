from django.contrib import admin

from website.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "department")
    list_filter = ("department",)
    search_fields = ("fullname", "email")
