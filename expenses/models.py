from django.db import models
from django.utils import timezone


# =========================================
# EXPENSE CATEGORY
# =========================================

class ExpenseCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name_plural = "Expense Categories"

        ordering = ['name']

    def __str__(self):

        return self.name


# =========================================
# PAYMENT MODE
# =========================================

class PaymentMode(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:

        ordering = ['name']

    def __str__(self):

        return self.name


# =========================================
# EXPENSE MODEL
# =========================================

class Expense(models.Model):

    # =====================================
    # PAYMENT STATUS
    # =====================================

    PAYMENT_STATUS = (

        ('Paid', 'Paid'),
        ('Pending', 'Pending'),

    )

    # =====================================
    # PAYMENT METHOD
    # =====================================

    PAYMENT_METHOD = (

        ('Cash', 'Cash'),
        ('Online', 'Online'),

    )

    category = models.ForeignKey(

        ExpenseCategory,

        on_delete=models.CASCADE,

        related_name='expenses'

    )

    payment_mode = models.ForeignKey(

        PaymentMode,

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )

    title = models.CharField(

        max_length=255

    )

    amount = models.DecimalField(

        max_digits=12,

        decimal_places=2

    )

    expense_date = models.DateField(

        default=timezone.now

    )

    # =====================================
    # NEW PAYMENT TRACKING
    # =====================================

    payment_status = models.CharField(

        max_length=20,

        choices=PAYMENT_STATUS,

        default='Paid'

    )

    payment_method = models.CharField(

        max_length=20,

        choices=PAYMENT_METHOD,

        blank=True,

        null=True

    )

    paid_date = models.DateField(

        blank=True,

        null=True

    )

    # =====================================
    # OTHER DETAILS
    # =====================================

    description = models.TextField(

        blank=True,

        null=True

    )

    receipt = models.ImageField(

        upload_to='expense_receipts/',

        blank=True,

        null=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            '-expense_date',

            '-created_at'

        ]

    def __str__(self):

        return (

            f"{self.title} - ₹{self.amount}"

        )