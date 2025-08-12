from django.contrib import admin
from .models import Empleado, Job, Salary, Place, Location, Country

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Job)
admin.site.register(Salary)
admin.site.register(Place)
admin.site.register(Location)
admin.site.register(Country)
