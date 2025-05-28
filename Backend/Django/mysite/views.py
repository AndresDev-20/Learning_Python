from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hello world.!")


def despedida(request):
    return HttpResponse("Goobye world.!")