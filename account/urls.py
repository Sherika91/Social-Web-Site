# from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    # Previous URL adress for Login
    # path('login/', views.user_login, name='login'),

    # Djangoss Log-in & Log-out URLs
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #
    # # Password Change URLs
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # # Password Reset URLs
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    #
    # path('password-reset-done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    #
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    #
    # path('password-reset/complete/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

    # Djangos's All Auth URLs, All the ones above.
    path('', include('django.contrib.auth.urls')),

    # Dashboard URLs
    path('', views.dashboard, name='dashboard'),

    # User Register URL's
    path('register/', views.register, name='register'),

    # User Profile Edit URL's
    path('edit/', views.edit, name='edit'),

    # User List URL's
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.use_detail, name='user_detail'),
]
