from django.urls import path

from . import views


urlpatterns = [

    # =====================================
    # STAFF DASHBOARD
    # =====================================

    path(
        '',
        views.staff_dashboard,
        name='staff_dashboard'
    ),

    # =====================================
    # STAFF PROFILE
    # =====================================

    path(
        'profile/<int:staff_id>/',
        views.staff_profile,
        name='staff_profile'
    ),

    # =====================================
    # SALARY SLIP PDF
    # =====================================

    path(
        'salary-slip/<int:staff_id>/',
        views.salary_slip_pdf,
        name='salary_slip_pdf'
    ),

    # =====================================
    # EXPORT EXCEL
    # =====================================

    path(
        'export/excel/',
        views.export_staff_excel,
        name='export_staff_excel'
    ),

]