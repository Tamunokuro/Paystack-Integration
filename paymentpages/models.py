from django.db import models
import secrets
from .paystack import Paystack

# Create your models here.
class Payments(models.Model):
    email = models.EmailField()
    amount = models.PositiveIntegerField()
    reference = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date_created',)
    def __str__(self) -> str:
        return f"{self.reference} - {self.amount}"
    def save(self, *args, **kwargs) -> None:
        while not self.reference:
            reference = secrets.token_urlsafe(50)
            if not Payments.objects.filter(reference=reference).exists():
                self.reference = reference
        super().save(*args, **kwargs)
    def convert_amount(self) -> int:
        return self.amount * 100 
    def verify(self):
        paystack = Paystack()
        status, result = paystack.verify(self.reference, self.amount)
        if status:
            if result['amount'] == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False



