from django.shortcuts import render

from .models import ExpenseTracker

from .serializers import TransactionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view()
def transactions(request):
    expenses = ExpenseTracker.objects.all()
    serializer = TransactionSerializer(expenses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
