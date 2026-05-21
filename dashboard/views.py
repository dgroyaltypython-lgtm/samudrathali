from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from decimal import Decimal

from sales.models import DailySale
from expenses.models import Expense
from inventory.models import InventoryItem, PurchaseRequest
from management_funds.models import ManagementFund
from staff.models import Staff

from django.contrib.auth.decorators import login_required


# =========================================
# MAIN DASHBOARD
# =========================================

@login_required
def dashboard(request):

    today = timezone.now().date()

    # =====================================
    # SALES
    # =====================================

    total_sales = DailySale.objects.aggregate(
        total=Sum('total_amount')
    )['total'] or Decimal('0.00')

    today_sales = DailySale.objects.filter(
        sale_date=today
    ).aggregate(
        total=Sum('total_amount')
    )['total'] or Decimal('0.00')

    # =====================================
    # EXPENSES
    # =====================================

    total_expense = Expense.objects.aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')

    pending_expense = Expense.objects.filter(
        payment_status='Pending'
    ).aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')

    # =====================================
    # PROFIT
    # =====================================

    net_profit = total_sales - total_expense

    # =====================================
    # INVENTORY
    # =====================================

    pending_requests = PurchaseRequest.objects.filter(
        status='Pending'
    ).count()

    low_stock_items = InventoryItem.objects.filter(
    current_stock__lte=5
    ).order_by('current_stock')[:6]

    # =====================================
    # MANAGEMENT FUNDS
    # =====================================

    management_used = ManagementFund.objects.aggregate(
        total=Sum('amount')
    )['total'] or Decimal('0.00')

    # =====================================
    # STAFF
    # =====================================

    total_staff = Staff.objects.filter(
        is_active=True
    ).count()

    total_salary = sum(
        staff.final_salary
        for staff in Staff.objects.filter(is_active=True)
    )

    # =====================================
    # RECENT TRANSACTIONS
    # =====================================

    recent_sales = DailySale.objects.order_by(
        '-sale_date'
    )[:5]

    recent_expenses = Expense.objects.order_by(
        '-expense_date'
    )[:5]

    # =====================================
    # CONTEXT
    # =====================================

    context = {

        'total_sales': total_sales,
        'today_sales': today_sales,

        'total_expense': total_expense,
        'pending_expense': pending_expense,

        'net_profit': net_profit,

        'pending_requests': pending_requests,

        'low_stock_items': low_stock_items,

        'management_used': management_used,

        'total_staff': total_staff,
        'total_salary': total_salary,

        'recent_sales': recent_sales,
        'recent_expenses': recent_expenses,

    }

    return render(
    request,
    'dashboard/dashboard.html',
    context
)