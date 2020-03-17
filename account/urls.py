from django.urls import path, include
from django.contrib.auth import views as auth_views

from account import views
from account import views

urlpatterns = [

    # dashboard url
    path('', views.dashboard, name='dashboard'),

    # built-in urls for authentication
    path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

]
