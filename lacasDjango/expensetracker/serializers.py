from rest_framework import serializers

from .models import ExpenseTracker



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTracker
        fields = [
            "name",
            "amount",
            "transaction_type"
        ]