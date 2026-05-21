from django.db import models
from django.utils import timezone


# =========================================
# INVENTORY ITEM
# =========================================

class InventoryItem(models.Model):

    name = models.CharField(
        max_length=255
    )

    current_stock = models.PositiveIntegerField(
        default=0
    )

    minimum_stock = models.PositiveIntegerField(
        default=5
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# =========================================
# PURCHASE REQUEST
# =========================================

class PurchaseRequest(models.Model):

    STATUS_CHOICES = (

        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),

    )

    item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    request_date = models.DateField(
        default=timezone.now
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.item} - {self.quantity}"