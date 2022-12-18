from django.shortcuts import redirect, render
from .models import Product
from .models import Category
from .models import Products
from .models import Advatisment
from .models import Customer
from .models import Cart
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse, JsonResponse
import json
from .models import Orders
from django.core.mail import send_mail
#for mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
import mysql.connector as sql
#for payment

import razorpay
import random 
from pack.forms import CustomUserForm




 
# authorize razorpay client with API Keys.

 
#end payment




# Create your views here.
def landpage(request):
    category=Category.objects.filter(status=0)
    
    j=0
    
    Product_objects_shoe= Product.objects.filter(category__slug="Shoes")
    Product_objects_sandle=Product.objects.filter(category__slug='Sandles')
    Product_objects_sleeper=Product.objects.filter(category__slug='Sleeper')
    Advatisment_objects=Advatisment.objects.all()
    if request.method=="GET":
        st=request.GET.get('searchname')
        if st!=None:
            products=Product.objects.filter(category__slug__icontains=st)
            return render(request,'searchpage.html',{'products':products})


    return render(request,'index.html',{'Product_objects_shoe':Product_objects_shoe,'j':j,'Advatisment_objects':Advatisment_objects,'Product_objects_sandle':Product_objects_sandle,'Product_objects_sleeper':Product_objects_sleeper,'category':category})


def collection(request):
    category=Category.objects.filter(status=0)
    context={'category':category}

    return render(request,'collections.html',context)
def collectionview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category_name=Category.objects.filter(slug=slug).first()
        return render(request,'searchpage.html',{'products':products,'category_name':category_name})
    else:
        messages.warning(request,"No such category found")
        return redirect('index')

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first

        else:
            messages.error(request,"No such category found")
            return redirect('index')


    else:
        messages.error(request,"no such category found")
        return redirect('index')
        
    return render(request,'detail.html',{'products':products})
def signupaction(request):
    form=CustomUserForm()
    if request.method == "POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register Successfully! Login to continue")
            return redirect('/login')


    context={'form':form}
    return render(request,'signup.html',context)
    
def loginpage(request):
    

   
    if request.method == "POST":

        name=request.POST.get('username')
        passwd=request.POST.get('password')
        user=auth.authenticate(request,username=name,password=passwd)
        if user is not None:

            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('/')
        else:
            messages.error(request,"Invailid Usename or Password")
            return redirect('/login')

    return render(request,'login.html')


def logoutpage(request):

   if request.user.is_authenticated:
       logout(request)
       messages.success(request,"Logged out Sucessfully")
   return redirect("/")
def addtocart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('prod_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"product already in cart"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"only"+str(product_check.quantity) +"quantity available" })




            else:
                return JsonResponse({'status': "no such product found"})


        else:
            return JsonResponse({'status':"Login to Continue"})
    return redirect('/')

def viewcart(request):
    
    
    return render(request,"cart.html")















    



#checkout page

     

#end checkout page

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data={
            'name':name,
            'email':email,
            'subject':subject,
            'message':message

       }
        message='''
            New message:{}

            From:{}

        '''.format(data['message'],data['email'])
       # send_mail( message,'','aminakhter620129@gmail.com',['aminakhter1166@gmail.com'])
        send_mail(
            data['subject'],
            message,
            data['email'],
            ['aminakhter620129@gmail.com'],
            
            fail_silently=False,
         )
        
    return render(request, 'contact.html',{})
        
         


def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson')
        name=request.POST.get('name')
        amount=request.POST.get('amount')
        
        
        

        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        phone=request.POST.get('phone')
        #payment code
        
        
        order=Orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount,items_json=items_json)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html',{'thank':thank,'id':id})
        #update=OrderUpdate(order_id=order.order_id,update_desc=" The order has been placed")
        #update.save()
        
    
          #request paytm to transfer the amount to your account after payment by user
        
    return render(request, 'checkout.html')


#for payment

    
    
    
    
    
   
    
