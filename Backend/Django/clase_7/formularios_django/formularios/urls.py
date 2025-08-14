
from django.contrib import admin
from django.urls import path
from .views import form_view, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', form_view, name='form'),
    path('success/', success, name='success'),
]
