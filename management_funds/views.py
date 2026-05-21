from django.shortcuts import render
from django.db.models import Sum

from .models import (
    ManagementFund,
    FundReturn
)
from django.contrib.auth.decorators import login_required

# =========================================
# MANAGEMENT FUND DASHBOARD
# =========================================
@login_required
def management_fund_dashboard(request):

    funds = ManagementFund.objects.all()

    total_used = funds.aggregate(
        total=Sum('amount')
    )['total'] or 0

    total_returned = FundReturn.objects.aggregate(
        total=Sum('amount')
    )['total'] or 0

    total_pending = sum(
        fund.pending_balance
        for fund in funds
    )

    context = {

        'funds': funds,
        'total_used': total_used,
        'total_returned': total_returned,
        'total_pending': total_pending,

    }

    return render(
        request,
        'management_funds/dashboard.html',
        context
    )