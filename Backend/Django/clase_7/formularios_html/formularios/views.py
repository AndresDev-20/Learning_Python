from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, 'form.html')

def success(request):
    if request.method != "GET":
        return HttpResponse("Invalid request method.", status=405)
    
    name = request.GET.get("name")
    email = request.GET.get("email")
    return render(request, 'forms/success.html', {"name": name, "email": email})
