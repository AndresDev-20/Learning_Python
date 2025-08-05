from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Comment

# Create your views here.
def social_index(request):
    return HttpResponse("Hello, world!")

def list_users(request):
    # listamos todos los usuarios
    users = User.objects.all()

    # Obtener datos filtrados por condición
    filtered = User.objects.filter(age__gte=18)

    # Obtener un unico usuario por ID
    user = User.objects.get(id=5)

    # Obtener los 5 primeros usuarios
    first_five_users = User.objects.all()[:5]

    # Obtener 5 elementos saltando los primeros 5
    skipped_users = User.objects.all()[5:10]

    return render(request, 'social/users.html', {'users': users, 'filtered': filtered, 'userId': user, 'first_five_users': first_five_users, 'skipped_users': skipped_users})
