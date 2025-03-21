# my_loan_plugin/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ItemLoan
from .forms import LoanRequestForm  # You would create this form yourself

@login_required
def loan_list_view(request):
    """
    Display a list of existing loans.
    """
    loans = ItemLoan.objects.all()
    return render(request, "my_loan_plugin/loan_list.html", {"loans": loans})

@login_required
def loan_request_view(request):
    """
    Handle new loan creation.
    """
    if request.method == "POST":
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            new_loan = form.save()
            return redirect(reverse("plugin:my_loan_plugin:loan-list"))
    else:
        form = LoanRequestForm()
    return render(request, "my_loan_plugin/loan_request.html", {"form": form})

@login_required
def loan_return_view(request, pk):
    """
    Mark a loan as returned.
    """
    loan = get_object_or_404(ItemLoan, pk=pk)
    loan.status = "returned"
    loan.loan_end = loan.loan_end or None  # or set it to today's date if needed
    loan.save()
    return redirect(reverse("plugin:my_loan_plugin:loan-list"))
