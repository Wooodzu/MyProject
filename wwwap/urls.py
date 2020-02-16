from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'www-home'),
    path('about/', views.about, name='www-about'),
    path('contact/', views.contact, name='www-contact'),
]