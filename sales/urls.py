from django.urls import path

from .views import (

    sales_list,
    add_sale,

    export_sales_csv,
    import_sales_csv

)

urlpatterns = [

    # =========================
    # SALES LIST
    # =========================

    path(
        '',
        sales_list,
        name='sales_list'
    ),

    # =========================
    # ADD SALE
    # =========================

    path(
        'add/',
        add_sale,
        name='add_sale'
    ),

    # =========================
    # EXPORT CSV
    # =========================

    path(
        'export-csv/',
        export_sales_csv,
        name='export_sales_csv'
    ),

    # =========================
    # IMPORT CSV
    # =========================

    path(
        'import-csv/',
        import_sales_csv,
        name='import_sales_csv'
    ),

]