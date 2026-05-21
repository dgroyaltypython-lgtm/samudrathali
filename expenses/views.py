from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# =========================================
# EXPENSE LIST
# =========================================
@login_required
def expense_list(request):

    expenses = Expense.objects.all()

    total_expense = sum(
        expense.amount for expense in expenses
    )

    context = {

        'expenses': expenses,
        'total_expense': total_expense

    }

    return render(
        request,
        'expenses/expense_list.html',
        context
    )


# =========================================
# ADD EXPENSE
# =========================================
@login_required
def add_expense(request):

    form = ExpenseForm(request.POST or None,
                       request.FILES or None)

    if form.is_valid():

        form.save()

        return redirect('expense_list')

    context = {

        'form': form

    }

    return render(
        request,
        'expenses/add_expense.html',
        context
    )


# =========================================
# EXPORT EXPENSE CSV
# =========================================
@login_required
def export_expenses_csv(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="expenses.csv"'


    writer = csv.writer(response)

    writer.writerow([

        'Title',
        'Category',
        'Amount',
        'Expense Date',
        'Payment Mode',
        'Notes'

    ])


    expenses = Expense.objects.all()

    for expense in expenses:

        writer.writerow([

            expense.title,
            expense.category,
            expense.amount,
            expense.expense_date,
            expense.payment_mode,
            expense.notes

        ])

    return response


# =========================================
# IMPORT EXPENSE CSV
# =========================================
@login_required
def import_expenses_csv(request):

    if request.method == 'POST':

        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode(
            'utf-8'
        ).splitlines()

        reader = csv.DictReader(decoded_file)

        for row in reader:

            Expense.objects.create(

                title=row['Title'],

                amount=row['Amount'],

                expense_date=row['Expense Date'],

                payment_mode=row['Payment Mode'],

                notes=row['Notes']

            )

    return redirect('expense_list')