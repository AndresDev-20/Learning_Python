from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def success(request):
    return render(request, 'success.html')