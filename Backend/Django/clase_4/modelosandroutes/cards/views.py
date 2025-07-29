from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("Hello, world! This is a test view for the cards app.")
