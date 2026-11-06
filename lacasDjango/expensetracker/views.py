from django.shortcuts import render

from .models import ExpenseTracker

# Create your views here.



def transactions(request):
    if request.method == "GET":
        expenses = ExpenseTracker.objects.all()
        return render(request, "transactions.html", {"expenses": expenses})
