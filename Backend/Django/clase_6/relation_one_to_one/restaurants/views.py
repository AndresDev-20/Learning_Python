from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the restaurant index")

def create(request):
    # Creamos el sitio
    place = Place(name="Sample Place", address="123 Sample St")
    place.save()

    # Creamos el restaurante con relacion al sitio de uno a uno 
    restaurant = Restaurant(place=place, name="Sample Restaurant")
    restaurant.save()
    return HttpResponse("Create a restaurant")