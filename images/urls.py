from django.urls import path

from images import views

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>', views.image_detail, name='detail'),
    path('ranking/', views.image_ranking, name='create'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
]
