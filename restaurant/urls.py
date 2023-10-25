from django.contrib import admin
from django.urls import path
from restaurant import views
urlpatterns = [
   path('',views.home,name='home'), 
   path('authpage',views.authpage,name='authpage'),
   path('user_registration',views.user_registration,name='user_registration'),
]

    