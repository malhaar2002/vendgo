from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.signup_page),
    path('login', views.login_page),
]
