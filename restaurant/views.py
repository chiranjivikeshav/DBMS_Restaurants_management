from django.shortcuts import render,redirect
from . import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from restaurant.models import Userprofile

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
        Userprofile.objects.create(
            user=user,
            user_email= useremail,
            user_name = "",
            user_about = "",
            contact_number = "",
            user_address = "",
            user_city = "",
            user_country = "",
            user_state = "",
            )
        return render(request,"auth.html")
    return render(request,'home.html') 


def user_login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['user_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your has been successfully Login!')
            return render(request,'home.html') 
        else:
            messages.warning(request,'Wrong credentials')
            f =1
            return render(request,"auth.html",{"f":f})
    return render(request, 'auth.html')
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Loged out successfully!')
    return redirect('home')

@login_required
def user_profile(request):
    user = request.user
    try:
        profile = Userprofile.objects.get(user=user)
    except Userprofile.DoesNotExist:
        return render(request, 'pagenotfound.html')
    return render(request,"profile.html",{'profile':profile})

def profileupdate(request,id):
    user=User.objects.get(id=id)
    if request.method == 'POST':
       user_name = request.POST['user_name'] 
       user_email = request.POST['user_email'] 
       contact_number = request.POST['contact_number'] 
       user_about = request.POST['user_about'] 
       user_address = request.POST['user_address'] 
       user_city = request.POST['user_city'] 
       user_country = request.POST['user_country'] 
       user_state = request.POST['user_state'] 
       user_ZIPCODE = request.POST['user_ZIPCODE']
    try:
        profile = Userprofile.objects.get(user=user)
        profile.user_name = user_name
        profile.user_email = user_email
        profile.contact_number = contact_number
        profile.user_about = user_about
        profile.user_address = user_address
        profile.user_city = user_city
        profile.user_country = user_country
        profile.user_state = user_state
        profile.user_ZIPCODE = user_ZIPCODE
        profile.save()
        messages.success(request, 'Your profile  has been updated successfully!')
    except Userprofile.DoesNotExist:
        profile=Userprofile(
        user=user,
        user_name = user_name,
        user_email = user_email,
        contact_number = contact_number,
        user_about = user_about,
        user_address = user_address,
        user_city = user_city,
        user_country = user_country,
        user_state = user_state,
        user_ZIPCODE = user_ZIPCODE,
        )
        profile.save()
    return redirect('user_profile')
def add_your_resta(request):
    return render (request,"add_rest.html")
def restaurant_MPO(request):
    return render (request ,"restaurant_MPO.html")