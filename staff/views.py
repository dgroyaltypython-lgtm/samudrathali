from django.shortcuts import (
    render,
    get_object_or_404
)

from django.db.models import Sum

from django.http import HttpResponse

import openpyxl

from reportlab.pdfgen import canvas

from .models import (
    Staff,
    SalaryAdvance,
    Attendance
)

from django.contrib.auth.decorators import login_required


# =========================================
# STAFF DASHBOARD
# =========================================
@login_required
def staff_dashboard(request):

    staffs = Staff.objects.all()

    total_staff = staffs.count()

    total_salary = staffs.aggregate(
        total=Sum('monthly_salary')
    )['total'] or 0

    total_advance = SalaryAdvance.objects.aggregate(
        total=Sum('amount')
    )['total'] or 0

    remaining_balance = (
        total_salary - total_advance
    )

    context = {

        'staffs': staffs,

        'total_staff': total_staff,

        'total_salary': total_salary,

        'total_advance': total_advance,

        'remaining_balance': remaining_balance

    }

    return render(
        request,
        'staff/staff_dashboard.html',
        context
    )


# =========================================
# STAFF PROFILE
# =========================================
@login_required
def staff_profile(request, staff_id):

    staff = get_object_or_404(
        Staff,
        id=staff_id
    )

    advances = SalaryAdvance.objects.filter(
        staff=staff
    )

    attendance = Attendance.objects.filter(
        staff=staff
    )

    total_present = attendance.filter(
        status='Present'
    ).count()

    total_absent = attendance.filter(
        status='Absent'
    ).count()

    context = {

        'staff': staff,

        'advances': advances,

        'attendance': attendance,

        'total_present': total_present,

        'total_absent': total_absent,

    }

    return render(
        request,
        'staff/staff_profile.html',
        context
    )


# =========================================
# SALARY SLIP PDF
# =========================================
@login_required
def salary_slip_pdf(request, staff_id):

    staff = get_object_or_404(
        Staff,
        id=staff_id
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; '
        f'filename="salary_slip_{staff.id}.pdf"'
    )

    p = canvas.Canvas(response)

    # TITLE
    p.setFont(
        "Helvetica-Bold",
        20
    )

    p.drawString(
        200,
        800,
        "Salary Slip"
    )

    # DETAILS
    p.setFont(
        "Helvetica",
        12
    )

    p.drawString(
        100,
        740,
        f"Name: {staff.name}"
    )

    p.drawString(
        100,
        710,
        f"Designation: {staff.designation}"
    )

    p.drawString(
        100,
        680,
        f"Monthly Salary: ₹ {staff.monthly_salary}"
    )

    p.drawString(
        100,
        650,
        f"Advance Deduction: ₹ {staff.total_advance}"
    )

    p.drawString(
        100,
        620,
        f"Remaining Salary: ₹ {staff.remaining_salary}"
    )

    p.drawString(
        100,
        590,
        f"Final Salary: ₹ {staff.final_salary}"
    )

    p.drawString(
        100,
        540,
        "GROUP OF BBN COASTAL PEARL Samudra Thali Restaurant"
    )

    p.showPage()

    p.save()

    return response


# =========================================
# EXPORT STAFF EXCEL
# =========================================
@login_required
def export_staff_excel(request):

    response = HttpResponse(
        content_type=(
            'application/vnd.openxmlformats-'
            'officedocument.spreadsheetml.sheet'
        )
    )

    response['Content-Disposition'] = (
        'attachment; '
        'filename="staff_payroll.xlsx"'
    )

    workbook = openpyxl.Workbook()

    worksheet = workbook.active

    worksheet.title = 'Payroll Report'

    columns = [

        'Name',
        'Designation',
        'Monthly Salary',
        'Advance',
        'Remaining Salary',
        'Final Salary'

    ]

    worksheet.append(columns)

    staffs = Staff.objects.all()

    for staff in staffs:

        worksheet.append([

            staff.name,

            staff.designation,

            float(staff.monthly_salary),

            float(staff.total_advance),

            float(staff.remaining_salary),

            float(staff.final_salary)

        ])

    workbook.save(response)

    return response