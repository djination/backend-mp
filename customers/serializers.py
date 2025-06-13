from rest_framework import serializers
from . import models

class AccountReadSerializer(serializers.ModelSerializer):
    industry_name = serializers.CharField(source='industry.name', read_only=True)
    type_of_business_name = serializers.CharField(source='type_of_business.name', read_only=True)
    type_of_business_detail = serializers.CharField(source='type_of_business.detail', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    account_category_name = serializers.CharField(source='account_category.name', read_only=True)
    parent_name = serializers.CharField(source='parent.name', read_only=True, allow_null=True, default=None)

    class Meta:
        model = models.Account
        fields = [
            'id', 'account_no', 'name', 'industry_name', 'type_of_business_name', 'type_of_business_detail',
            'account_type_name', 'account_category_name', 'parent_name',
        ]

class AccountWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = [
            'id', 
            'account_no',
            'name',
            'industry',
            'type_of_business',
            'account_type',
            'account_category',
            'parent',
        ]
        read_only_fields = ['created_by', 'updated_by']
        # fields = '__all__'

class AccountBankReadSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    bank_category_name = serializers.CharField(source='bank.category.name', read_only=True)

    class Meta:
        model = models.AccountBank
        fields = [
            'id', 'account_name', 'bank_name', 'bank_category_name',
            'bank_account_holder_name', 'bank_account_no', 'is_active'
        ]


class AccountBankWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountBank
        fields = [
            'id', 'account', 'bank', 'bank_category',
            'bank_account_holder_name', 'bank_account_no', 'is_active'
        ]
        read_only_fields = ['created_by', 'updated_by']

class AccountTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountType
        fields = ['id', 'name', 'is_active']

class AccountTypeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountType
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['created_by', 'updated_by']

class AccountCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountCategory
        fields = ['id', 'name', 'is_active']

class AccountCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountCategory
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['created_by', 'updated_by']


class IndustryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = ['id', 'name', 'is_active']

class IndustryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['created_by', 'updated_by']

class TypeOfBusinessReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeOfBusiness
        fields = ['id', 'name', 'detail', 'is_active']

class TypeOfBusinessWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeOfBusiness
        fields = ['id', 'name', 'detail', 'is_active']
        read_only_fields = ['created_by', 'updated_by']

class AccountAddressReadSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)

    class Meta:
        model = models.AccountAddress
        fields = [
            'id', 'account_name', 'address1', 'address2', 'sub_district', 'district','city', 'province', 'postalcode', 'country', 'latitude', 'longitude', 'is_active'
        ]

class AccountAddressWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountAddress
        fields = [
            'id', 'account', 'address1', 'address2', 'sub_district', 'district', 'city', 'province', 'postalcode', 'country', 'latitude', 'longitude', 'is_active'
        ]
        read_only_fields = ['created_by', 'updated_by']

class AccountPICReadSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    position_name = serializers.CharField(source='position.name', read_only=True)

    class Meta:
        model = models.AccountPIC
        fields = [
            'id', 'account_name', 'name', 'email', 'phone_no', 'position_name', 'is_active'
        ]

class AccountPICWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AccountPIC
        fields = [
            'id', 'account', 'name', 'email', 'phone_no', 'position', 'is_active'
        ]
        read_only_fields = ['created_by', 'updated_by']

class BankReadSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = models.Bank
        fields = ['id', 'name', 'description', 'is_active']

class BankWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = ['id', 'name', 'description', 'is_active']
        read_only_fields = ['created_by', 'updated_by']

class BankCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCategory
        fields = ['id', 'name','is_active']

class BankCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCategory
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['created_by', 'updated_by']

class PositionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = ['id', 'name', 'is_active']

class PositionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = ['id', 'name', 'is_active']
        read_only_fields = ['created_by', 'updated_by']
