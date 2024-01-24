from django.urls import path
from . import views
from .apps import ImagesConfig

app_name = ImagesConfig.name

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),

]
