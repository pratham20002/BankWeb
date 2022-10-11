from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('login',views.Login, name='login'),
    path('logout',views.Logout, name='logout'),
    path('signin',views.SignIn, name='signin'),
    path('create_account',views.create_account, name='create_account'),
    path('deposite',views.deposite, name ='deposite'),
]