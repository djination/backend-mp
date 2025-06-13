from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models
from django.utils import timezone
from backend.mixins import NoDeleteMixin

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"message": "Welcome to Dashboard!"})

class AccountViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.Account.objects.all()

    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.AccountReadSerializer
        return serializers.AccountWriteSerializer
    # serializer_class = serializers.AccountSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

class AccountTypeViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.AccountType.objects.all()
    # serializer_class = serializers.AccountTypeSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.AccountTypeReadSerializer
        return serializers.AccountTypeWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class AccountCategoryViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.AccountCategory.objects.all()
    # serializer_class = serializers.AccountCategorySerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.AccountCategoryReadSerializer
        return serializers.AccountCategoryWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class IndustryViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.Industry.objects.all()
    # serializer_class = serializers.IndustrySerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.IndustryReadSerializer
        return serializers.IndustryWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())
    
    permission_classes = [permissions.IsAuthenticated]

class TypeOfBusinessViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.TypeOfBusiness.objects.all()
    # serializer_class = serializers.TypeOfBusinessSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.TypeOfBusinessReadSerializer
        return serializers.TypeOfBusinessWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class AccountAddressViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.AccountAddress.objects.all()
    # serializer_class = serializers.AccountAddressSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.AccountAddressReadSerializer
        return serializers.AccountAddressWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class AccountPICViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.AccountPIC.objects.all()
    # serializer_class = serializers.AccountPICSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.AccountPICReadSerializer
        return serializers.AccountPICWriteSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class AccountBankViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.AccountBank.objects.all()
    # serializer_class = serializers.AccountBankSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.AccountBankReadSerializer
        return serializers.AccountBankWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class BankViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.Bank.objects.all()
    # serializer_class = serializers.BankSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.BankReadSerializer
        return serializers.BankWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

class BankCategoryViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.BankCategory.objects.all()
    # serializer_class = serializers.BankCategorySerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.BankCategoryReadSerializer
        return serializers.BankCategoryWriteSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())
        
    permission_classes = [permissions.IsAuthenticated]

class PositionViewSet(NoDeleteMixin, viewsets.ModelViewSet):
    queryset = models.Position.objects.all()
    # serializer_class = serializers.PositionSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.PositionReadSerializer
        return serializers.PositionWriteSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username, created_at=timezone.now())
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username, updated_at=timezone.now())

    permission_classes = [permissions.IsAuthenticated]

# Note: The serializers used in the viewsets should be updated to the specific serializers for each model.