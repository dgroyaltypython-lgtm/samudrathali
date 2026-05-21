from django.shortcuts import render, redirect
from .models import DailySale
from .forms import DailySaleForm
import csv

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# =========================================
# SALES LIST
# =========================================
@login_required
def sales_list(request):

    sales = DailySale.objects.all()

    total_sales = sum(
        sale.total_amount for sale in sales
    )

    context = {

        'sales': sales,
        'total_sales': total_sales

    }

    return render(
        request,
        'sales/sales_list.html',
        context
    )


# =========================================
# ADD SALE
# =========================================
@login_required
def add_sale(request):

    form = DailySaleForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('sales_list')

    return render(
        request,
        'sales/add_sale.html',
        {
            'form': form
        }
    )

# =========================================
# EXPORT SALES CSV
# =========================================
@login_required
def export_sales_csv(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="sales.csv"'


    writer = csv.writer(response)

    writer.writerow([

        'Date',
        'Total Sales',
        'Payment Method',
        'Notes'

    ])

    sales = DailySale.objects.all()

    for sale in sales:

        writer.writerow([

            sale.sale_date,
            sale.total_sales,
            sale.payment_method,
            sale.notes

        ])

    return response

# =========================================
# IMPORT SALES CSV
# =========================================
@login_required
def import_sales_csv(request):

    if request.method == 'POST':

        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode(
            'utf-8'
        ).splitlines()

        reader = csv.reader(decoded_file)

        next(reader)

        for row in reader:

            DailySale.objects.create(

                sale_date=row[0],
                total_sales=row[1],
                payment_method=row[2],
                notes=row[3]

            )

    return redirect('sales_list')