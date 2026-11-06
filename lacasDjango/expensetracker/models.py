from django.db import models

# Create your models here.

class ExpenseTracker(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, choices=[
        ("CREDIT", "CREDIT"),
        ("DEBIT", "DEBIT"),
    ])


    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"