from django.contrib import admin
from django.urls import path
from restaurant import views
urlpatterns = [
   path('',views.home,name='home'), 
   path('authpage',views.authpage,name='authpage'),
   path('user_registration',views.user_registration,name='user_registration'),
   path('user_login',views.user_login,name='user_login'),
   path('user_logout',views.user_logout,name='user_logout'),
   path('user_profile',views.user_profile,name='user_profile'),
   path('profile/update/<int:id>',views.profileupdate,name="profileupdate"),
   path('add_your_resta',views.add_your_resta,name="add_your_resta"),
   path('restaurant_MPO',views.restaurant_MPO,name="restaurant_MPO"),
   path('menu',views.Menu,name="menu"),
   path('regist_your_resta',views.regist_your_resta,name="regist_your_resta"),
   path('resta_form_save',views.resta_form_save,name="resta_form_save"),
   path('add_item/<int:restaurant_id>',views.add_item,name="add_item"),
]

    