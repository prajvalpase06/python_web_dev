from django.contrib import admin
from django.urls import path
from mapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginpage, name="login"),
    path('register', views.register, name="register"),
]
