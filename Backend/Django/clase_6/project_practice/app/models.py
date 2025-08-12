from django.db import models

# Create your models here.
class Empleado(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.ForeignKey('Salary', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Salary(models.Model):
    amount = models.IntegerField()
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

    def __str__(self):
        return f"Salary: {self.amount}"


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name