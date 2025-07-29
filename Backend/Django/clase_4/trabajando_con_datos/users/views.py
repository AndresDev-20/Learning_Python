from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def createUser(request):
    # Primera forma de principiante
    #user = User(firstname="Yeison", lastname="Andres", email="yeison.andres@example.com", password="securepassword", edad=20)
    #user.save()

    # Segunda forma de principiante
    user = User.objects.create(firstname="Alisson", lastname="Veronica", email="alisson.veronica@example.com", password="securepassword", edad=2)
    return HttpResponse(f"User {user.firstname} {user.lastname} created successfully!")

def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponse(f"User {user.firstname} {user.lastname} deleted successfully!")
    