from django.shortcuts import render,redirect
from . import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from restaurant.models import Userprofile,Restaurant,Item

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
       if user_ZIPCODE=='':
           user_ZIPCODE = 0
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
    if request.user.is_authenticated:
        user_id = request.user
        your_restaurant = Restaurant.objects.filter(user = user_id )
        return render (request,"add_rest.html",{"your_restaurant":your_restaurant})
    return render (request,"add_rest.html")

def regist_your_resta(request):
    if request.user.is_authenticated:
        return render (request,"regist_rest.html")
    return redirect("authpage")

def resta_form_save(request):
    if request.method == 'POST':
        restaurant_name = request.POST.get('restaurant_name')
        restaurant_address = request.POST.get('Restaurant_address')
        restaurant_country = request.POST.get('restaurant_country')
        restaurant_state = request.POST.get('restaurant_state')
        restaurant_city = request.POST.get('restaurant_city')
        restaurant_pincode = request.POST.get('restaurant_pincode')
        restaurant_phone = request.POST.get('restaurant_phone')
        restaurant_owner_phone = request.POST.get('restaurant_owner_phone')
        restaurant_owner_name = request.POST.get('restaurant_owner_name')
        restaurant_owner_email = request.POST.get('restaurant_owner_email')
        open_time = request.POST.get('open_time')
        close_time = request.POST.get('close_time')
        menu_image = request.FILES.get('menu_image')
        restaurant_image = request.FILES.get('restaurant_image')
        user  = request.user
        restaurant = Restaurant(
            rest_name=restaurant_name,
            location=restaurant_address,
            city=restaurant_city,
            country=restaurant_country,
            pin=restaurant_pincode,
            state=restaurant_state,
            rest_cantact_no=restaurant_phone,
            owner_contact_no=restaurant_owner_phone,
            ownername=restaurant_owner_name,
            owneremail=restaurant_owner_email,
            open_time=open_time,
            close_time=close_time,
            menu_image=menu_image,
            restaurant_image=restaurant_image,
            user = user,
        )
        restaurant.save()
        messages.success(request, 'Your Restaurant has been successfully Registered!')
        return redirect('home')  
    return redirect('restaurant_MPO')



@login_required
def restaurant_MPO(request):
    user = request.user
    restaurant = Restaurant.objects.get(user = user)
    restaurant_menu = Item.objects.filter(restaurant = restaurant)
    context = {'restaurant':restaurant,
               'restaurant_menu':restaurant_menu
               }
    return render (request ,"restaurant_MPO.html",context)


def add_item(request, restaurant_id):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        item = Item(restaurant=restaurant, item_name=item_name, price=price)
        item.save()
        messages.success(request,"Item is Successfully Added")
    return redirect('restaurant_MPO',)  




def Menu(request):
    Menu_Item = Item.objects.all()
    return render (request ,"menu.html",{"Menu_Item":Menu_Item})




def Filter(request):
  if request.method=="POST":
    location = request.POST.get('location')
    restaurant_name = request.POST.get('restaurant_name')
    item_name = request.POST.get('item_name')


    if location and restaurant_name:
       restaurants = Restaurant.objects.filter(Q(location_icontains=location) & Q(rest_name_icontains=restaurant_name))
    if location==None and restaurant_name:
       restaurants = Restaurant.objects.filter(rest_name__icontains=restaurant_name)
    if restaurant_name==None and location:  
       restaurants = Restaurant.objects.filter(location__icontains=location) 
    else:
       restaurants=restaurants.objects.all() 

    restaurant_names = restaurants.values_list('rest_name', flat=True)
    Menu_Item = Item.objects.filter(restaurant__in=restaurants)

    if item_name :
       Menu_Item = Item.objects.filter(Q(item_name__icontains=item_name))
    
    return render(request ,"menu.html",{"Menu_Item":Menu_Item})
  return redirect('menu')