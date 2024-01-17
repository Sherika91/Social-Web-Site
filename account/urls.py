from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # Previous URL adress for Login
    # path('login/', views.user_login, name='login'),

    # Djangoss Log-in & Log-out URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard URLs
    path('', views.dashboard, name='dashboard'),
]