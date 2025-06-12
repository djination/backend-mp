from rest_framework import serializers
from . import models

class AccountSerializer(serializers.ModelSerializer):
    industry_name = serializers.CharField(source='industry.name', read_only=True)
    # type_of_business_display = serializers.SerializerMethodField(read_only=True)
    type_of_business_name = serializers.CharField(source='type_of_business.name', read_only=True)
    type_of_business_detail = serializers.CharField(source='type_of_business.detail', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    account_category_name = serializers.CharField(source='account_category.name', read_only=True)
    parent_name = serializers.CharField(source='parent.name', read_only=True, allow_null=True, default=None)

    # def get_type_of_business_display(self, obj):
    #     if obj.type_of_business:
    #         name = obj.type_of_business.name or ""
    #         detail = obj.type_of_business.detail or ""
    #         return f"{name} - {detail}" if detail else name
    #     return None

    class Meta:
        model = models.Account
        fields = [
            'id', 'name', 
            'industry_name', 'type_of_business_name', 'type_of_business_detail', 'account_type_name', 'account_category_name', 'parent_name',
            # tambahkan field lain yang ingin ditampilkan
        ]
        extra_kwargs = {
            'industry': {'write_only': False},
            'type_of_business': {'write_only': False},
            'account_type': {'write_only': False},
            'account_category': {'write_only': False},
            'parent': {'write_only': False},
        }

class AccountBankSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    bank_category_name = serializers.CharField(source='bank.category.name', read_only=True)
    
    class Meta:
        model = models.AccountBank
        fields = [
            'id', 'account_name', 'bank_account_no', 'bank_name', 'bank_category_name',
            'bank_account_holder_name', 'is_active'
        ]

        extra_kwargs = {
            'account': {'write_only': False},
            'bank': {'write_only': False},
            'bank_category': {'write_only': False},
            'parent': {'write_only': False},
        }

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountType
        fields = '__all__'

class AccountCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountCategory
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = '__all__'

class TypeOfBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeOfBusiness
        fields = '__all__'

class AccountAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountAddress
        fields = '__all__'

class AccountPICSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountPIC
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = '__all__'

class BankCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCategory
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'

