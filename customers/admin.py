from django.contrib import admin
from . import models

# Register your models here.
admin.site.register([models.Account, models.AccountAddress, models.AccountBank, models.AccountCategory, \
                     models.AccountPIC, models.AccountType, models.Bank, \
                     models.BankCategory, models.Industry, models.Position])  # Register your models here