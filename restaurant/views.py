from django.shortcuts import render,redirect
from . import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth.models import Restaurant
# Create your views here.
def home(request):
    return render(request,"home.html")

def authpage(request):
    return render(request,"auth.html")
def user_registration(request): 
    if request.method == 'POST':
        username = request.POST['user_name']
        useremail = request.POST['user_email']
        password = request.POST['user_password']
        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            messages.warning(request,'Username already exists')
            return render(request,"auth.html")
        existing_EMAIL = User.objects.filter(email=useremail).exists()
        if existing_EMAIL:
            messages.warning(request,'Email Address already exists')
            return render(request,"auth.html")
        user = User.objects.create_user(username=username,email=useremail, password=password)
        messages.success(request, 'Your account has been created successfully!')
        return render(request,"auth.html")
    return render(request,'home.html')
@login_required 
def register_restaurant(request):
     if request.method == 'POST':
        restaurant_name = request.POST['restaurant_name']
        restaurant_location = request.POST['restaurant_location']
        restaurant_city = request.POST['restaurant_city']
        restaurant_pin = request.POST['restaurant_pin']
        restaurant_state = request.POST['restaurant_state']
        restaurant_country = request.POST['restaurant_ccountry']
        restaurant_no = request.POST['restaurant_no']
        restaurant_ownerno = request.POST['restaurant_ownerno']
        restaurant_ownername = request.POST['restaurant_ownername']
        restaurant_owneremail = request.POST['restaurant_owneremail']
        open_time=request.POST['open_time']
        close_time=request.POST['close_time']

        
        existing_restaurant = Restaurant.objects.filter(name=restaurant_name).exists()
        if existing_restaurant:
            messages.warning(request,'Restaurant already exists')
            return render(request,"restaurants.html",restaurant=existing_restaurant)
        
        restaurant= Restaurant.objects.create(name=restaurant_name,location=restaurant_location,city=restaurant_city,pin=restaurant_pin ,state=restaurant_state ,country=restaurant_country ,no=restaurant_no ,ownerno=restaurant_ownerno,ownername=restaurant_ownername,owneremail=restaurant_owneremail,open_time=open_time,close_time=close_time)
        messages.success(request, 'Your account has been created successfully!')
        return render(request,"restaurants.html",restaurant=restaurant)
# THIS IS FOR THE FILTER THAT WE WILL APPLY ON OUR FOOD MENU CATEGORY

# def category(request):
#     categoryID=(request.GET.get('category'))
#     if categoryID:
#         items=Item.objects.filter(category=categoryID)

#     else:
#         items=Item.objects.all()

#         data={}
#         data['items']=items
#         return render(request,'index.html',data)
# THIS IS FOR THE FILTER THAT WE WILL APPLY TO SEARCH OUR FOOD ITEMS
# def food(request):
# if request.method=="GET":
#     foodID=request.GET.get('foodID')
#     if foodID!=none:
#         items=Item.objects.filter(foodID=foodID)
# items=Item.objects.all()
#  data={}
#         data['items']=items
#         return render(request,'index.html',data)
#    
# THIS IS FOR THE FILTER THAT WE WILL APPLY ON OUR FOOD MENU CATEGORY
# def category(request):
#     categoryID=(request.GET.get('category'))
#     if categoryID:
#         items=Item.objects.filter(category=categoryID)

#     else:
#         items=Item.objects.all()

#         data={}
#         data['items']=items
#         return render(request,'index.html',data)
# THIS IS FOR THE FILTER THAT WE WILL APPLY ON OUR FOOD MENU CATEGORY
# def category(request):
#     categoryID=(request.GET.get('category'))
#     if categoryID:
#         items=Item.objects.filter(category=categoryID)

#     else:
#         items=Item.objects.all()

#         data={}
#         data['items']=items
#         return render(request,'index.html',data)
# THIS IS FOR THE FILTER THAT WE WILL APPLY ON OUR FOOD MENU CATEGORY
# def category(request):
#     categoryID=(request.GET.get('category'))
#     if categoryID:
#         items=Item.objects.filter(category=categoryID)

#     else:
#         items=Item.objects.all()

#         data={}
#         data['items']=items
#         return render(request,'index.html',data)
