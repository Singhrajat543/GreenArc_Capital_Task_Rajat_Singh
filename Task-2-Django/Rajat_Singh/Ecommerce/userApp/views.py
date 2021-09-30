from django.contrib.auth import views
from django.shortcuts import redirect, render
from django.views import View 
from .models import Customer , Product , Cart , OrderdPlace
from .forms import CustomerRegistrationForm
from django.contrib import messages 
from .forms import CustomerProfileForm
from .models import Customer
from django.db.models import Q 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self,request):
        Mobiles = Product.objects.filter(catogary='Mobile')
        Laptops = Product.objects.filter(catogary='Laptop')
        topwears = Product.objects.filter(catogary='Top Wear')
        BottomWear = Product.objects.filter(catogary='Bottom wear') 
        return render(request ,'app/home.html',{'Mobiles':Mobiles,'Laptops':Laptops,'topwears':topwears,'BottomWear':BottomWear})
        



class ProductDetailView(View):
    def get(self,request,pk): 
        product = Product.objects.get(pk=pk) 
        return render(request,'app/productdetail.html',{'product':product}) 
        
@login_required
def add_to_cart(request):
    user=request.user   
    product_id = request.GET.get('prod_id')  
    
    product = Product.objects.get(id=product_id) 
    A = Cart(user=user , Product=product)
    A.save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user  
        cart= Cart.objects.filter(user=user)   

        ammounts=0.0
        shipping_ammount=70.0
        Total_Ammount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user] 
     

        if cart_product: 
            for p in cart_product: 
                tempammount=(p.quantity * p.Product.discounted_price) 
               
                ammounts += tempammount
                TotalAmount = ammounts + shipping_ammount
            return render(request, 'app/addtocart.html',{'carts':cart,'TotalAmount':TotalAmount,'ammounts':ammounts})

        else:
            return render(request, 'app/EmpattyCart.html')



def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        ammounts=0.0
        shipping_ammount=70.0
        Total_Ammount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user]
       

        for p in cart_product: 
          tempammount=(p.quantity * p.Product.discounted_price) 
               
          ammounts += tempammount 
          TotalAmount = ammounts + shipping_ammount
        
                 
        data = {

          'Quantity': c.quantity ,
          'amount': ammounts ,
          'totalamounts': TotalAmount


                }
        return JsonResponse(data)





def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        ammounts=0.0
        shipping_ammount=70.0
        Total_Ammount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user] 
    
        

        for p in cart_product: 
          tempammount=(p.quantity * p.Product.discounted_price) 
               
          ammounts += tempammount 
          TotalAmount = ammounts + shipping_ammount
        
                 
        data = {

          'Quantity': c.quantity ,
          'amount': ammounts ,
          'totalamounts': TotalAmount


                }
        return JsonResponse(data)



def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.delete()
        ammounts=0.0
        shipping_ammount=70.0
        Total_Ammount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user == request.user] 

        for p in cart_product: 
          tempammount=(p.quantity * p.Product.discounted_price) 
               
          ammounts += tempammount 
          TotalAmount = ammounts + shipping_ammount
        
                 
        data = {

          'amount': ammounts ,
          'totalamounts':  ammounts + shipping_ammount


                }
        return JsonResponse(data)






def buy_now(request):
 return render(request, 'app/buynow.html')


@login_required
def address(request):
    add = Customer.objects.filter(user= request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})
        



def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None): 
                                
    if data == None:
        mobiles = Product.objects.filter(catogary='Mobile')
    elif data == 'Mi' or data == 'Samsung':
        mobiles= Product.objects.filter(catogary='Mobile').filter(brand=data)

    elif data=='below':
        mobiles= Product.objects.filter(catogary='Mobile').filter(discounted_price__lt=10000)

    elif data=='above':
        mobiles= Product.objects.filter(catogary='Mobile').filter(discounted_price__gt=10000)

    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def Laptop(request, data=None):
    if data == None:
        Laptops = Product.objects.filter(catogary='Laptop')
    elif data == 'HP' or data == 'Microsoft':
        Laptops= Product.objects.filter(catogary='Laptop').filter(brand=data)
    elif data == 'Asus':
        Laptops= Product.objects.filter(catogary='Laptop').filter(brand=data)

    elif data=='below':
        Laptops= Product.objects.filter(catogary='Laptop').filter(discounted_price__lt=26000)
    elif data=='above':
        Laptops= Product.objects.filter(catogary='Laptop').filter(discounted_price__gt=26000)

    return render(request, 'app/Laptop.html',{'Laptops':Laptops})



class CostomerRegistrationView(View):
    def get(self , request): 
        form = CustomerRegistrationForm()   
        return render(request,'app/customerregistration.html', {'form':form} ) 

    def post(self, request): 
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulation Registerd succesfuly')
            form.save()
        return render(request,'app/customerregistration.html', {'form':form} )    



def Upload_Product(request):
    if request.method == "POST":
        prod = Product()
        prod.title = request.POST.get('title')
        prod.selling_price = request.POST.get('selling_price')
        prod.discounted_price = request.POST.get('discounted_price')
        prod.brand = request.POST.get('brand')
        prod.Comment = request.POST.get('comment')


        prod.discription = request.POST.get('discription')

        prod.catogary = request.POST.get('catogary')

        if len(request.FILES) !=0:
            prod.product_image = request.FILES['image']
        prod.save()
        
        messages.success(request,"Added Successfuly")
        
    return render(request,'app/UploadProduct.html')    


@login_required
def checkout(request):
    user = request.user  
    Address=Customer.objects.filter(user=user) 
    Cart_Items = Cart.objects.filter(user=user) 
    ammounts=0.0
    shipping_ammount=70.0
    Total_Ammount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user == request.user]
    if cart_product: 
        for p in cart_product:
            tempammount=(p.quantity * p.Product.discounted_price)
            ammounts += tempammount 
        Total_Ammount = ammounts+shipping_ammount    
    return render(request, 'app/checkout.html',{'add':Address, 'totalAmount':Total_Ammount,
        'Cart_Items':Cart_Items})



@login_required
def payment_done(request):
    User = request.user
    custid = request.GET.get('custid')
    
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=User)
    for c in cart:

        A= OrderdPlace (user=User,customer=customer,product=c.Product,quantity=c.quantity)
        A.save()
        c.delete()
    return redirect("orders")    

@login_required
def orders(request):
    Order_Placed = OrderdPlace.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'orderPlace':Order_Placed})






@method_decorator(login_required , name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form , 'active':'btn-primary'})



    def post(self,request):
        form = CustomerProfileForm(request.POST) 
        if form.is_valid(): 
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg= Customer(user=usr, name=name, locality=locality,city=city,state=state, zipcode=zipcode )

            reg.save()
            messages.success(request, 'congratulation Your Profile Added')

        return render(request,'app/profile.html', {'form':form, 'active':'btn-primary'})    



