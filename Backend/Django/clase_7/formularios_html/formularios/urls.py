from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/forms/', views.getform, name='form'),
    path('get/goals/', views.getsuccess, name='goals'),
    path('post/users/', views.postusers, name='addusers')
]
