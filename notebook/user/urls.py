from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('', views.all_users, name='all_users'),
    path('users/<int:id>/', views.user_details, name='user'),
]
