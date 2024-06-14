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
   path('restaurant_UPV/<int:id>',views.restaurant_UPV,name="restaurant_UPV"),
   path('menu',views.Menu,name="menu"),
   path('delete-menu/<int:id>',views.delete_menu,name="delete_menu"),
   path('regist_your_resta',views.regist_your_resta,name="regist_your_resta"),
   path('resta_form_save',views.resta_form_save,name="resta_form_save"),
   path('add_item/<int:restaurant_id>',views.add_item,name="add_item"),
   path('filter',views.Filter,name="Filter"),
   path('manager_dash/<int:id>',views.manager_dash,name='manager_dash'),
   path('manager',views.manager,name='manager'),
   path('manager_update',views.manager_update,name='manager_update'),
   path('restaurant_update/<int:id>',views.restaurant_update,name='restaurant_update'),
   path('restaurantupdate/<int:id>',views.restaurantupdate,name='restaurantupdate'),
   path('menu_update/<int:item_id>', views.menu_update, name='menu_update'),
   path('add_to_cart/<int:item_id>', views.add_to_cart, name='add_to_cart'),
   path('add_to_cart2/<int:item_id>', views.add_to_cart2, name='add_to_cart2'),
   path('order_now/<int:item_id>', views.order_now, name='order_now'),
   path('cart_display', views.cart_display, name='cart_display'),
   path('remove_from_cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
   path('checkout', views.checkout, name='checkout'),
]

    