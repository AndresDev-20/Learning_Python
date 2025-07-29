from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    edad = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"