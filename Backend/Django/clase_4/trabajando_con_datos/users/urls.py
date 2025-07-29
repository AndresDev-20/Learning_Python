from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.createUser, name='create_user'),
    path('delete/<int:user_id>/', views.deleteUser, name='delete_user'),
]
