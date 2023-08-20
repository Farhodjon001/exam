from django.contrib import admin
from .models import Customer,RepairType,RepairRequest

# Register your models here.
admin.site.register(Customer)
admin.site.register(RepairType)
admin.site.register(RepairRequest)

