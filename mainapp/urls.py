from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.loginUser),
    path('signup/', views.signupUser),
    path('logout/', views.logoutUser),
    path('dashboard/', views.dashboard),
]
