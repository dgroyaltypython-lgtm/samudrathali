from django.db import models
from django.utils import timezone
from decimal import Decimal


# =========================================
# FUND CATEGORY
# =========================================

class FundCategory(models.Model):

    title = models.CharField(
        max_length=100,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['title']

    def __str__(self):

        return self.title


# =========================================
# MANAGEMENT FUND ENTRY
# =========================================

class ManagementFund(models.Model):

    person_name = models.CharField(
        max_length=255
    )

    category = models.ForeignKey(
        FundCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    purpose = models.TextField(
        blank=True,
        null=True
    )

    is_returnable = models.BooleanField(
        default=True
    )

    used_date = models.DateField(
        default=timezone.now
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-used_date']

    def __str__(self):

        return (
            f"{self.person_name} "
            f"- ₹{self.amount}"
        )


    # =====================================
    # TOTAL RETURNED
    # =====================================

    @property
    def total_returned(self):

        total = self.returns.aggregate(
            total=models.Sum('amount')
        )['total']

        return total or Decimal('0.00')


    # =====================================
    # PENDING BALANCE
    # =====================================

    @property
    def pending_balance(self):

        if self.is_returnable:

            return (
                self.amount -
                self.total_returned
            )

        return Decimal('0.00')


# =========================================
# FUND RETURN ENTRY
# =========================================

class FundReturn(models.Model):

    management_fund = models.ForeignKey(
        ManagementFund,
        on_delete=models.CASCADE,
        related_name='returns'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    return_date = models.DateField(
        default=timezone.now
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-return_date']

    def __str__(self):

        return (
            f"{self.management_fund.person_name} "
            f"- ₹{self.amount}"
        )