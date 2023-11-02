from django.shortcuts import render,redirect
from . import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Item,User
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

def item(request):
    if request.method=='POST':
        item_name=request.POST['item_name']
        price =request.POST['price']
        user_id = request.POST['restaurant']
        restaurant1 = User.objects.filter(user_id=user_id).exists()
        if restaurant1:
            item_name1=Item.objects.filter(item_name=item_name).exists()
            if item_name1:
                messages.warning(request,'Item already resistered')
                return render(request,"item.html")
            else:
                mydata = Item.objects.create(restaurant=user_id,item_name=item_name,price=price)
                messages.success(request, 'Your Item has been added successfully!')
        else:
            messages.warning(request, 'Restaurant does not exist')
    else:
        return render(request,"item.html")
                 







