from django.shortcuts import render,redirect
from . import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from restaurant.models import Userprofile,Restaurant,Item,Manager,Cart,Order,OrderItem
from django.db.models import Q
from django.shortcuts import get_object_or_404
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


def user_logout(request):
    logout(request)
    messages.success(request, 'Loged out successfully!')
    return redirect('home')

@login_required(login_url='/authpage')
def user_profile(request):
    user = request.user
    try:
        profile = Userprofile.objects.get(user=user)
    except Userprofile.DoesNotExist:
        return render(request, 'pagenotfound.html')
    return render(request,"profile.html",{'profile':profile})

@login_required(login_url='/authpage')
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

@login_required(login_url='/authpage')
def regist_your_resta(request):
    if request.user.is_authenticated:
        return render (request,"regist_rest.html")
    return redirect("authpage")

@login_required(login_url='/authpage')
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
    return redirect('restaurant_MPO')



@login_required(login_url='/authpage')
def restaurant_MPO(request):
    user = request.user
    restaurant = Restaurant.objects.get(user = user)
    restaurant_menu = Item.objects.filter(restaurant = restaurant)
    context = {'restaurant':restaurant,
               'restaurant_menu':restaurant_menu
               }
    return render (request ,"restaurant_MPO.html",context)

def restaurant_UPV(request,id):
    restaurant = Restaurant.objects.get(id = id)
    menu_items = Item.objects.filter(restaurant=restaurant)
    context = {'restaurant':restaurant,
               'menu_items':menu_items
               }
    return render (request ,"restaurant_UPV.html",context)

@login_required(login_url='/authpage')
def add_item(request, restaurant_id):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        price = request.POST.get('price')
        image = request.FILES.get('item_image')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        item = Item(restaurant=restaurant, item_name=item_name,item_description= item_description, price=price,image =image)
        item.save()
        messages.success(request,"Item Added Successfully")
    return redirect('restaurant_MPO',) 

@login_required(login_url='/authpage') 
def delete_menu(request,id):
    item = Item.objects.get(id = id)
    item.delete()
    messages.success(request,"Item deleted Successfully")
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
       restaurants = Restaurant.objects.filter(Q(rest_name__icontains=restaurant_name))
    if restaurant_name==None and location:  
       restaurants = Restaurant.objects.filter(Q(location__icontains=location)) 
    else:
       restaurants=Restaurant.objects.all() 
    Menu_Item = Item.objects.filter(restaurant__in=restaurants)

    if item_name :
       Menu_Item = Menu_Item.filter(Q(item_name__icontains=item_name))
    
    return render(request ,"menu.html",{"Menu_Item":Menu_Item})
  return redirect('menu')

@login_required(login_url='/authpage')
def manager_dash(request):
    user = request.user
    restaurant = Restaurant.objects.get(user =user)
    manager = Manager.objects.filter(restaurant=restaurant)
    context ={
          'restaurant':restaurant,
          'managers':manager,
    }
    return render(request,"manager_dash.html",context)

@login_required(login_url='/authpage')
def manager(request):
    id =''
    if request.method == 'POST':
        restaurant_id = request.POST['restaurant_id']
        manager_name = request.POST['managername']
        manager_contact = request.POST['managercontact']
        manager_email = request.POST['manageremail']
        manager_address = request.POST['manageraddress']
        manager_bank_name = request.POST['managerbankname']
        manager_bank_branch = request.POST['managerbankbranch']
        manager_bank_ifsc = request.POST['managerbankIFSC']
        manager_bank_account = request.POST['managerbankaccount']
        manager_about = request.POST['managerabout']
        restaurant = Restaurant.objects.get(id=restaurant_id)
        manager=Manager(
            restaurant=restaurant,
            Name = manager_name,
            Contact = manager_contact,
            Email = manager_email,
            Address = manager_address,
            BankName = manager_bank_name,
            BankAccount = manager_bank_account,
            BankBranch = manager_bank_branch,
            BankIFSC = manager_bank_ifsc,
            About = manager_about,
             )
        manager.save()
        id = restaurant_id
        messages.success(request, 'Manager Details Added successfully!')
    return redirect("manager_dash", id)


@login_required(login_url='/authpage')
def manager_update(request):
    id =''
    if request.method == 'POST':
        restaurant_id = request.POST['restaurant_id']
        manager_name = request.POST['managername']
        manager_contact = request.POST['managercontact']
        manager_email = request.POST['manageremail']
        manager_address = request.POST['manageraddress']
        manager_bank_name = request.POST['managerbankname']
        manager_bank_branch = request.POST['managerbankbranch']
        manager_bank_ifsc = request.POST['managerbankIFSC']
        manager_bank_account = request.POST['managerbankaccount']
        manager_about = request.POST['managerabout']
        restaurant = Restaurant.objects.get(id=restaurant_id)

        manager = Manager.objects.get(restaurant=restaurant)

        manager.restaurant=restaurant
        manager.Name = manager_name
        manager.Contact = manager_contact
        manager.Email = manager_email
        manager.Address = manager_address
        manager.BankName = manager_bank_name
        manager.BankAccount = manager_bank_account
        manager.BankBranch = manager_bank_branch
        manager.BankIFSC = manager_bank_ifsc
        manager.About = manager_about
             
        manager.save()
        id = restaurant_id
        messages.success(request, 'Manager Details Updated successfully!')
    return redirect("manager_dash", id)

@login_required(login_url='/authpage')
def restaurant_update(request,id):
    try:
        restaurant = Restaurant.objects.get(id=id)
    except Restaurant.DoesNotExist:
        return render(request, 'pagenotfound.html')
    return render(request,"edit_restaurant_details.html",{'restaurant':restaurant})

@login_required(login_url='/authpage')
def restaurantupdate(request,id):
    restaurant=Restaurant.objects.get(id=id)
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
    try:
        profile = Restaurant.objects.get(restaurant=restaurant)
        profile.rest_name = restaurant_name
        profile.location = restaurant_address
        profile.city = restaurant_country
        profile.country = restaurant_state
        profile.pin = restaurant_city
        profile.state = restaurant_pincode
        profile.rest_cantact_no = restaurant_phone
        profile.owner_contact_no=restaurant_owner_phone
        profile.ownername = restaurant_owner_name
        profile.owneremail= restaurant_owner_email
        profile.open_time = open_time
        profile.close_time = close_time
        profile.menu_image = menu_image
        profile.restaurant_image = restaurant_image
        profile.save()
        messages.success(request, 'Your Restaurant details updated successfully!')
    except Restaurant.DoesNotExist:
        profile=Restaurant(
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
        )
        profile.save()
    return redirect('restaurant_update')

@login_required(login_url='/authpage')
def menu_update(request, item_id):
    menu_item =Item.objects.get(id =item_id)
    if request.method == 'POST':
        menu_item.item_name = request.POST.get('item_name')
        menu_item.item_description = request.POST.get('item_description')
        menu_item.price = request.POST.get('item_price')
        if request.FILES.get('item_image'):
            menu_item.image = request.FILES['item_image']
        menu_item.save()
        messages.success(request, 'Item details updated successfully!')
        return redirect('restaurant_MPO',)

    return redirect('restaurant_MPO',)


@login_required(login_url='/authpage')
def add_to_cart(request, item_id):
    item = Item.objects.get(id =item_id)
    user = request.user
    cart_item, created = Cart.objects.get_or_create(item=item, user=user, defaults={'item_count': 1})
    id = item.restaurant.id
    if not created:
        messages.error(request, 'Item allready in cart!')
        return redirect('restaurant_UPV', id=id)
    messages.success(request, 'Item added to cart!')
    return redirect('restaurant_UPV', id=id)

@login_required(login_url='/authpage')
def add_to_cart2(request, item_id):
    item = Item.objects.get(id =item_id)
    user = request.user
    cart_item, created = Cart.objects.get_or_create(item=item, user=user, defaults={'item_count': 1})
    id = item.restaurant.id
    if not created:
        messages.error(request, 'Item allready in cart!')
        return redirect('menu')
    messages.success(request, 'Item added to cart!')
    return redirect('menu')
    
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.delete()
    return redirect('cart_display')

def cart_display(request):
    user =  request.user
    cart_items = Cart.objects.filter(user = user)
    return render(request ,"cart.html",{"cart_items" : cart_items})

@login_required(login_url='/authpage')
def order_now(request, item_id):
    item = Item.objects.get(id =item_id)
    user = request.user
    cart_item, created = Cart.objects.get_or_create(item=item, user=user, defaults={'item_count': 1})
    id = item.restaurant.id
    if not created:
        messages.error(request, 'Item allready in cart!')
        return redirect('cart_display')
    messages.success(request, 'Item added to cart!')
    return redirect('cart_display')

# ===========this is for order detail form rendering=========
@login_required(login_url='/authpage')
def order_detail(request):
    user =  request.user
    total_cost  = 0
    cart_items = Cart.objects.filter(user = user)
    for cart_item in  cart_items:
        total_cost += cart_item.item.price
    if total_cost == 0:
        messages.success(request,"Please Add Item In the Cart")
        return redirect('cart_display')
    return render (request,"order_details.html",{"cart_items":cart_items,"total_cost":total_cost})

# ===========this is for collecting order detials===========
@login_required(login_url='/authpage')
def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('zip')

        user =  request.user
        cart_items = Cart.objects.filter(user = user)
        total_price = sum(item.item.price * item.item_count for item in cart_items)
        if total_price == 0:
            messages.success(request,"Please Add Item In the Cart")
            return redirect('cart_display')
        order = Order.objects.create(
            user=user,
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pin_code=pincode,
            total_price=total_price
        )
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.item_count,
                price=(cart_item.item.price)*(cart_item.item_count),
            )
            cart_item.delete()
        return redirect('checkout',order.id)
    return redirect('order_detail')  


def checkout(request,order_id):
    user = request.user
    print(order_id)
    cart_items = Cart.objects.filter(user = user)
    total_cost  = 0
    for cart_item in  cart_items:
        total_cost += cart_item.item.price
    return render (request,"payment.html",{"total_cost":total_cost})


def myorder(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    current_orders = orders.filter(payment_status=True, delevery_status=False) 
    payment_left_orders = orders.filter(payment_status=False)
    delivered_orders = orders.filter(payment_status=True, delevery_status=True)
    context = {
        'current_orders': current_orders,
        'payment_left_orders': payment_left_orders,
        'delivered_orders': delivered_orders,
    }
    return render (request,"myorder.html",context)