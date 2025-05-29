from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hello world.!")


def despedida(request):
    return HttpResponse("Goobye world.!")

 # Funcion con parametro
def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("Eres menor de edad")