from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login


urlpatterns = [
    # Previous URL adress for Login
    # path('login/', user_login, name='login'),

    # Djangoss Log-in & Log-out URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
