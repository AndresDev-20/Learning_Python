from django.shortcuts import render



def first_template(request):
    return render(request, 'hola.html')

def  second_template(request, name):
    context = ["JavaScript", "TypeScript", "Python", "Java", "Php"]
    return render(request, 'dinamico.html', {"languajes": context, "name": name})

