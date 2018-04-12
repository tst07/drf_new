from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Bank, Branch, Accounts, Customer
from .serializers import BankSerializer, BranchSerializer, AccountsSerializer, CustomerSerializer

# Create your views here.

def hello_v2(request, version = "v1"):
	return HttpResponse('base alive hello_v2')

def hello(request, version = "v1"):
	return HttpResponse('base alive hello')

def bye(request, version = "v1"):
	return HttpResponse('base alive bye')


class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bank.objects.all().order_by('-created_at')
    serializer_class = BankSerializer


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class AccountsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
