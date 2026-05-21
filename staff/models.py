from django.db import models
from django.utils import timezone
from decimal import Decimal


# =========================================
# DESIGNATION
# =========================================

class Designation(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):

        return self.name


# =========================================
# STAFF MODEL
# =========================================

class Staff(models.Model):

    name = models.CharField(
        max_length=255
    )

    designation = models.ForeignKey(
        Designation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    monthly_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    overtime_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=50
    )

    joining_date = models.DateField(
        default=timezone.now
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['name']

    def __str__(self):

        return self.name


    # =====================================
    # TOTAL ADVANCE
    # =====================================

    @property
    def total_advance(self):

        total = self.advances.aggregate(
            total=models.Sum('amount')
        )['total']

        return total or Decimal('0.00')


    # =====================================
    # ATTENDANCE COUNTS
    # =====================================

    @property
    def present_days(self):

        return self.attendance_records.filter(
            status='Present'
        ).count()


    @property
    def absent_days(self):

        return self.attendance_records.filter(
            status='Absent'
        ).count()


    @property
    def half_days(self):

        return self.attendance_records.filter(
            status='Half Day'
        ).count()


    @property
    def leave_days(self):

        return self.attendance_records.filter(
            status='Leave'
        ).count()


    # =====================================
    # OVERTIME HOURS
    # =====================================

    @property
    def total_overtime_hours(self):

        total = self.attendance_records.aggregate(
            total=models.Sum('overtime_hours')
        )['total']

        return total or Decimal('0.00')


    # =====================================
    # OVERTIME AMOUNT
    # =====================================

    @property
    def overtime_amount(self):

        return (
            self.total_overtime_hours
            * self.overtime_rate
        )


    # =====================================
    # PER DAY SALARY
    # =====================================

    @property
    def per_day_salary(self):

        return (
            self.monthly_salary
            / Decimal('30')
        )


    # =====================================
    # ABSENT DEDUCTION
    # =====================================

    @property
    def absent_deduction(self):

        return (
            self.absent_days
            * self.per_day_salary
        )


    # =====================================
    # HALF DAY DEDUCTION
    # =====================================

    @property
    def half_day_deduction(self):

        return (

            self.half_days
            * (self.per_day_salary / 2)

        )


    # =====================================
    # FINAL SALARY
    # =====================================

    @property
    def final_salary(self):

        final_salary = (

            self.monthly_salary

            + self.overtime_amount

            - self.total_advance

            - self.absent_deduction

            - self.half_day_deduction

        )

        return round(final_salary, 2)


# =========================================
# STAFF ADVANCE
# =========================================

class SalaryAdvance(models.Model):

    ADVANCE_TYPE = (

        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),

    )

    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='advances'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    advance_type = models.CharField(
        max_length=20,
        choices=ADVANCE_TYPE
    )

    advance_date = models.DateField(
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

        ordering = ['-advance_date']

    def __str__(self):

        return f"{self.staff.name} - ₹{self.amount}"


# =========================================
# ATTENDANCE
# =========================================

class Attendance(models.Model):

    STATUS_CHOICES = (

        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Half Day', 'Half Day'),
        ('Leave', 'Leave'),

    )

    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    attendance_date = models.DateField(
        default=timezone.now
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Present'
    )

    overtime_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            'staff',
            'attendance_date'
        )

        ordering = ['-attendance_date']

    def __str__(self):

        return (

            f"{self.staff.name}"
            f" - {self.attendance_date}"

        )