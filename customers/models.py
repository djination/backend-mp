from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class TypeOfBusiness(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_type_of_business'
        verbose_name_plural = 'Type of Busineses'

class AccountType(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_account_type'
        verbose_name_plural = 'Account Types'

class AccountCategory(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_account_category'
        verbose_name_plural = 'Account Categories'

class Industry(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    # Tambahkan field lain jika diperlukan

    class Meta:
        db_table = 'm_industry'
        verbose_name_plural = "Industries"

class Account(models.Model):
    account_no = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=200)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)
    type_of_business = models.ForeignKey(TypeOfBusiness, on_delete=models.SET_NULL, null=True, blank=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True, blank=True)
    account_category = models.ForeignKey(AccountCategory, on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        # Assuming AccountCategory with id=1 is 'Parent'
        if self.account_category_id == 1 and self.parent is not None:
            raise ValidationError("Parent field must be empty if account_category is 'Parent'.")
        elif self.account_category_id != 1 and self.parent is None:
            raise ValidationError("Parent field must be filled if account_category is not 'Parent'.")
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_account'

class AccountAddress(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    sub_district = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_account_address'
        verbose_name_plural = 'Account Addresses'

class Bank(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_bank'

class BankCategory(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_bank_category'
        verbose_name_plural = 'Bank Categories'

class AccountBank(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank_account_no = models.CharField(max_length=50)
    bank_category = models.ForeignKey(BankCategory, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    bank_account_holder_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'm_account_bank'
        verbose_name_plural = 'Account Banks'

class Position(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_position'

class AccountPIC(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    phone_no = models.CharField(max_length=30)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'm_account_pic'
        verbose_name_plural = 'Account PICs'