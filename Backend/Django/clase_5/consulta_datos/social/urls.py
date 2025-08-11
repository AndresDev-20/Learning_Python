from django.urls import path
from . import views

urlpatterns = [
    path('', views.social_index, name='social_index'),
    path('users/', views.list_users, name='list_users'),
    path('users/update/<int:user_id>/', views.user_update, name='user_update')
]