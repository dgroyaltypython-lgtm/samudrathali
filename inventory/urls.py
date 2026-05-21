from django.urls import path

from . import views


urlpatterns = [

    # =====================================
    # INVENTORY REQUEST LIST
    # =====================================

    path(
        '',
        views.purchase_request_list,
        name='inventory_list'
    ),

    # =====================================
    # ADD PURCHASE REQUEST
    # =====================================

    path(
        'add/',
        views.add_purchase_request,
        name='add_purchase_request'
    ),

    # =====================================
    # EXPORT INVENTORY CSV
    # =====================================

    path(
        'export-csv/',
        views.export_inventory_csv,
        name='export_inventory_csv'
    ),

    # =====================================
    # IMPORT INVENTORY CSV
    # =====================================

    path(
        'import-csv/',
        views.import_inventory_csv,
        name='import_inventory_csv'
    ),

]