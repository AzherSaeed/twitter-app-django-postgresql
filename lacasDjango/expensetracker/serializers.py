from rest_framework import serializers

from .models import ExpenseTracker



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTracker
        fields = [
            "title",
            "amount",
            "transaction_type"
        ]