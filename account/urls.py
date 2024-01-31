# from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [

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

    # User Follows URL's
    path('users/follow/', views.user_follow, name='user_follow'),

    # User Detail URL's
    path('users/<username>/', views.use_detail, name='user_detail'),

]
