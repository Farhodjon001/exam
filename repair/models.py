from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class RepairType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class RepairRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    repair_type = models.ForeignKey(RepairType, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)


