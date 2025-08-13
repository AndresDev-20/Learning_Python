from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', views.form, name='form'),
    path('goals/', views.success, name='goals')
]
