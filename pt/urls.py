from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/<id>', views.profile_detail, name='profile_detail'),
    path('register/', views.register, name='register'),

]
