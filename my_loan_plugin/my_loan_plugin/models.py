# my_loan_plugin/models.py

from django.db import models
from stock.models import StockItem

class ItemLoan(models.Model):
    """
    Stores loan information for a particular StockItem.
    """

    # Link to the StockItem model
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)

    borrower = models.CharField(max_length=255)
    loan_start = models.DateField()
    loan_end = models.DateField(null=True, blank=True)
    
    LOAN_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("on_loan", "On Loan"),
        ("returned", "Returned"),
    ]
    status = models.CharField(
        max_length=20,
        choices=LOAN_STATUS_CHOICES,
        default="pending"
    )

    agreement_file = models.FileField(
        upload_to="loan_agreements/",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Loan #{self.id} - {self.stock_item} to {self.borrower}"
