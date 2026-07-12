from django.contrib import admin
from .models import Employee, Leave


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "username",
    )

    list_display_links = (
        "employee_id",
    )

    search_fields = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "username",
    )


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "leave_type",
        "from_date",
        "to_date",
        "status",
        "applied_on",
    )

    list_filter = (
        "status",
        "leave_type",
    )

    search_fields = (
        "employee__employee_id",
        "employee__first_name",
        "employee__last_name",
    )