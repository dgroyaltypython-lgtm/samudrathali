from django.contrib import admin

from .models import (
    Designation,
    Staff,
    SalaryAdvance,
    Attendance
)


# =========================================
# DESIGNATION ADMIN
# =========================================

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):

    list_display = [

        'name'

    ]

    search_fields = [

        'name'

    ]

    ordering = [

        'name'

    ]


# =========================================
# STAFF ADMIN
# =========================================
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    list_display = [

        'name',
        'designation',
        'monthly_salary',
        'overtime_rate',
        'present_days',
        'half_days',
        'absent_days',
        'total_overtime_hours',
        'overtime_amount',
        'total_advance',
        'final_salary',
        'is_active'

    ]

    list_filter = [

        'designation',
        'is_active',
        'joining_date'

    ]

    search_fields = [

        'name'

    ]

    ordering = [

        'name'

    ]

    readonly_fields = [

        'total_advance',
        'present_days',
        'half_days',
        'absent_days',
        'leave_days',
        'total_overtime_hours',
        'overtime_amount',
        'absent_deduction',
        'half_day_deduction',
        'final_salary'

    ]
# =========================================
# SALARY ADVANCE ADMIN
# =========================================

@admin.register(SalaryAdvance)
class SalaryAdvanceAdmin(admin.ModelAdmin):

    list_display = [

        'staff',
        'amount',
        'advance_type',
        'advance_date'

    ]

    list_filter = [

        'advance_type',
        'advance_date'

    ]

    search_fields = [

        'staff__name'

    ]

    ordering = [

        '-advance_date'

    ]


# =========================================
# ATTENDANCE ADMIN
# =========================================

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = [

        'staff',
        'attendance_date',
        'status',
        'overtime_hours'

    ]

    list_filter = [

        'status',
        'attendance_date'

    ]

    search_fields = [

        'staff__name'

    ]

    ordering = [

        '-attendance_date'

    ]