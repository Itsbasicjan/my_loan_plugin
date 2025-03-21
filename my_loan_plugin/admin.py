# my_loan_plugin/admin.py

from django.contrib import admin
from .models import ItemLoan

@admin.register(ItemLoan)
class ItemLoanAdmin(admin.ModelAdmin):
    list_display = ("id", "stock_item", "borrower", "status", "loan_start", "loan_end")
    list_filter = ("status", "loan_start", "loan_end")
