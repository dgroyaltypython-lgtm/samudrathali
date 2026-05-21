from django.shortcuts import render, redirect
from .models import PurchaseRequest
from .forms import PurchaseRequestForm
import csv
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# =========================================
# PURCHASE REQUEST LIST
# =========================================
@login_required
def purchase_request_list(request):

    requests = PurchaseRequest.objects.all()

    return render(
        request,
        'inventory/request_list.html',
        {
            'requests': requests
        }
    )


# =========================================
# ADD PURCHASE REQUEST
# =========================================
@login_required
def add_purchase_request(request):

    form = PurchaseRequestForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'purchase_request_list'
        )

    return render(
        request,
        'inventory/add_request.html',
        {
            'form': form
        }
    )

# =========================================
# EXPORT INVENTORY CSV
# =========================================
@login_required
def export_inventory_csv(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="inventory.csv"'


    writer = csv.writer(response)

    writer.writerow([

        'Item Name',
        'Quantity',
        'Unit',
        'Status',
        'Request Date'

    ])

    inventory_items = PurchaseRequest.objects.all()

    for item in inventory_items:

        writer.writerow([

            item.item_name,
            item.quantity,
            item.unit,
            item.status,
            item.request_date

        ])

    return response


# =========================================
# IMPORT INVENTORY CSV
# =========================================
@login_required
def import_inventory_csv(request):

    if request.method == 'POST':

        csv_file = request.FILES.get('csv_file')

        if not csv_file.name.endswith('.csv'):

            messages.error(
                request,
                'Please upload CSV file only.'
            )

            return redirect('inventory_list')

        decoded_file = csv_file.read().decode(
            'utf-8'
        ).splitlines()

        reader = csv.reader(decoded_file)

        next(reader)

        for row in reader:

            PurchaseRequest.objects.create(

                item_name=row[0],
                quantity=row[1],
                unit=row[2],
                status=row[3]

            )

        messages.success(
            request,
            'Inventory CSV Imported Successfully.'
        )

    return redirect('inventory_list')