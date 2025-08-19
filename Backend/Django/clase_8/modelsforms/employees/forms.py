from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee 
        fields = ['first_name', 'last_name', 'email', 'phone']
       # fields = '__all__'
       # exclude = ['email']  # Example of excluding a field