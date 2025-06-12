from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"message": "Welcome to Dashboard!"})

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountTypeViewSet(viewsets.ModelViewSet):
    queryset = models.AccountType.objects.all()
    serializer_class = serializers.AccountTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.AccountCategory.objects.all()
    serializer_class = serializers.AccountCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = serializers.IndustrySerializer
    permission_classes = [permissions.IsAuthenticated]

class TypeOfBusinessViewSet(viewsets.ModelViewSet):
    queryset = models.TypeOfBusiness.objects.all()
    serializer_class = serializers.TypeOfBusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountAddressViewSet(viewsets.ModelViewSet):
    queryset = models.AccountAddress.objects.all()
    serializer_class = serializers.AccountAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountPICViewSet(viewsets.ModelViewSet):
    queryset = models.AccountPIC.objects.all()
    serializer_class = serializers.AccountPICSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountBankViewSet(viewsets.ModelViewSet):
    queryset = models.AccountBank.objects.all()
    serializer_class = serializers.AccountBankSerializer
    permission_classes = [permissions.IsAuthenticated]

class BankViewSet(viewsets.ModelViewSet):
    queryset = models.Bank.objects.all()
    serializer_class = serializers.BankSerializer
    permission_classes = [permissions.IsAuthenticated]

class BankCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.BankCategory.objects.all()
    serializer_class = serializers.BankCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

# Note: The serializers used in the viewsets should be updated to the specific serializers for each model.