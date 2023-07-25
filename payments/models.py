from django.db import models
from enum import Enum
from django.core.validators import URLValidator
from borrowings.models import Borrowing
from _decimal import Decimal

FINE_MULTIPLIER = 1.5
class PaymentStatus(Enum):
    PENDING = "PENDING"
    PAID = "PAID"

class PaymentType(Enum):
    PAYMENT = "PAYMENT"
    FINE = "FINE"

class Payment(models.Model):
    status = models.CharField(
        max_length=7, choices=[(status.name, status.value) for status in PaymentStatus]
    )
    type = models.CharField(
        max_length=7, choices=[(type.name, type.value) for type in PaymentType]
    )
    borroving = models.ForeignKey(
        Borrowing, on_delete=models.CASCADE, related_name="payments"
    )
    stripe_sesion_url = models.TextField(
        validators=[URLValidator()],
        null=True,
        blank=True
    )
    stripe_sesion_id = models.CharField(max_length=255, null=True, blank=True)

    @property
    def money_to_pay(self):
        if self.type == "PAYMENT":
            days_borrowed = (
                self.borroving.extend_return_date - self.borroving.borrow_date
            ).days
            return Decimal(days_borrowed) * self.borroving.book.dayly_fee
        if self.type == "FINE" and self.borroving.actual_return_date:
            day_overdue = (
                self.borroving.actual_return_date - self.borroving.extend_return_date
            ).days
        return (
            Decimal(day_overdue)
            * self.borroving.book.dayly_fee
            * Decimal(FINE_MULTIPLIER)
        )