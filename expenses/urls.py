from django.urls import path
from . import views


urlpatterns = [

    # =====================================
    # EXPENSE DASHBOARD
    # =====================================

    path(
        '',
        views.expense_list,
        name='expense_list'
    ),

    # =====================================
    # ADD EXPENSE
    # =====================================

    path(
        'add/',
        views.add_expense,
        name='add_expense'
    ),

    # =====================================
    # EXPORT CSV
    # =====================================

    path(
        'export/csv/',
        views.export_expenses_csv,
        name='export_expenses_csv'
    ),

    # =====================================
    # IMPORT CSV
    # =====================================

    path(
        'import/csv/',
        views.import_expenses_csv,
        name='import_expenses_csv'
    ),

]