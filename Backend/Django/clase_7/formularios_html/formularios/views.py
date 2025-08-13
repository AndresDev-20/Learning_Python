from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request, 'form.html')

def getsuccess(request):
    if request.method != "GET":
        return HttpResponse("Invalid request method.", status=405)
    
    name = request.GET.get("name")
    email = request.GET.get("email")
    return render(request, 'forms/get/success.html', {"name": name, "email": email})



def postusers(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method.", status=405)

    name = request.POST.get("name")
    email = request.POST.get("email")
    return render(request, 'forms/post/success.html', {"name": name, "email": email})
