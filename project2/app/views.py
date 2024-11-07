from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from.models import *
from django.contrib.auth.models import User
import os
from django.contrib import messages

# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"invalid uname and password")
            return redirect(shop_login)
        
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    req.session.flush()
    logout(req)
    return redirect(shop_login)

def shop_home(req):
    if 'shop' in req.session:
        return render(req,'shop/home.html')
    else:
        return redirect(shop_login)

def add_product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['pro_name']
            price=req.POST['pro_price']
            offer_price=req.POST['offer_price']
            dis=req.POST['dis']
            img=req.FILES['img']
            data=Product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,dis=dis,img=img)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_pro.html')
    else:
        return redirect(shop_login)
    
# def edit_prod(req,pid):
#     if 'shop' in req.session:
#             if req.method=='POST':
#                 id=req.POST['pro_id']
#                 name=req.POST['pro_name']
#                 price=req.POST['pro_price']
#                 offer_price=req.POST['offer_price']
#                 dis=req.POST['dis']
#                 img=req.FILES['img']
#                 data=Product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,dis=dis,img=img)
#                 data.save()
#             else:
#                 Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,dis=prd_dis)
#             return redirect(shop_home)
#             else:
#             data=Product.objects.get(pk=pid)
#             return render(req,'shop/edit.html',{'product':data})
#     else:
#         return redirect(shop_login)
def delete_prod(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    return redirect(shop_home)
    
def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shop_login)
        except:
            return redirect(register)
    else:
        return render(req,'user/register.html')

def user_home(req):
    if 'user' in req.session:
        return render(req,'user/home.html')
    else:
        return redirect(shop_login)
    
def view_pro(req,pid):
    data=Product.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':data})

