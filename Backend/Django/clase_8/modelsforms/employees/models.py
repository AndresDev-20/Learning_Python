from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"