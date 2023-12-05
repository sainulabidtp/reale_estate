# property_management/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Property, Unit, Tenant, RentalInformation


admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(RentalInformation)
