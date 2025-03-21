# my_loan_plugin/urls.py

from django.urls import path
from . import views

app_name = "my_loan_plugin"  # for namespacing

urlpatterns = [
    path("", views.loan_list_view, name="loan-list"),
    path("request/", views.loan_request_view, name="loan-request"),
    path("return/<int:pk>/", views.loan_return_view, name="loan-return"),
]
