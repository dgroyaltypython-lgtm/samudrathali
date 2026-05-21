from django.db import models
from django.utils import timezone


# =========================================
# PAYMENT TYPE
# =========================================

class SalePaymentType(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# =========================================
# SALES ENTRY
# =========================================

class DailySale(models.Model):

    payment_type = models.ForeignKey(
        SalePaymentType,
        on_delete=models.SET_NULL,
        null=True
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    sale_date = models.DateField(
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
        ordering = ['-sale_date', '-created_at']

    def __str__(self):
        return f"{self.sale_date} - ₹{self.total_amount}"