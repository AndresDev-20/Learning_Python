from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse

def form_view(request):
    data_form = MyForm()
    return render(request, 'form.html', {'form': data_form})


def success(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method.", status=405)
    data = request.POST
    return render(request, 'success.html', {'data': data})
