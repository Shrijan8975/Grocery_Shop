from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models import Category,Grocery
from UserApp.models import  UserInfo,MyCart,Payment,Order_Master
from datetime import datetime

# Create your views here.
def home(request):
    cats = Category.objects.all()
    Grocerys = Grocery.objects.all()
    return render(request,"home.html",{"cats":cats,"grocery":Grocerys})

def ShowProduct(request,gid):
    cats = Category.objects.all()
    Grocerys = Grocery.objects.filter(cat_id=gid)
    return render(request,"home.html",{"cats":cats,"grocerys":Grocerys})

def SignUp(request):
    if(request.method=="GET"):
        cats = Category.objects.all()
        return render(request,"SignUp.html",{"cats":cats})

    else:
        u1 = UserInfo()
        u1.username = request.POST["uname"]
        u1.password = request.POST["pwd"]
        u1.save()
        return redirect(home)

def Login(request):
    if(request.method=="GET"):
        cats = Category.objects.all()
        return render(request,"Login.html",{"cats":cats})
    else:
        username = request.POST["uname"]
        password = request.POST["pwd"]
        try:
            u1 = UserInfo.objects.get(username=username,password=password)
            #Create session
            request.session["uname"] = username            
        except:
            pass
        return redirect(home)

def Logout(request):
    request.session.clear()
    return redirect(home)

def ViewDetails(request,grocery_id):
    g1 = Grocery.objects.get(id=grocery_id)
    cats = Category.objects.all()
    return render(request,"ViewDetails.html",{"grocery":g1,"cats":cats})

def AddToCart(request):
    if("uname" in request.session):
        #Add to cart
        u1 = UserInfo.objects.get(username=request.session["uname"])
        g1 = Grocery.objects.get(id=request.POST["groceryid"])
        qty = request.POST["qty"]
        
        try:
            item = MyCart.objects.get(user=u1,grocery=g1)
        except:
            cart = MyCart()
            cart.user = u1
            cart.grocery = g1
            cart.qty = qty
            cart.save()

        return redirect(home)

    else:
        return redirect(Login)

def ShowAllCartItems(request):
    if(request.method=="GET"):
        if("uname" in request.session):
            items = MyCart.objects.filter(user = request.session["uname"])

            total = 0

            for item in items:
                total += item.qty * item.grocery.price

            #print(total)
            request.session["total"] = total
            cats = Category.objects.all()
            return render(request,"ShowallCartItems.html",{"items":items,"cats":cats})
        else:
            return redirect(Login)
    else:
        action = request.POST["action"]
        groceryid= request.POST["grocery_id"]
        item = MyCart.objects.get(user = request.session["uname"],
                                     grocery = Grocery.objects.get(id=groceryid))
        
        if(action == "update"):
            qty  = request.POST["item_qty"]            
            item.qty = qty
            item.save()            
        else: #remove method
            item.delete()

        return redirect(ShowAllCartItems)


def makepayment(request):
    if(request.method=="GET"):
        cats = Category.objects.all()
        return render(request,"cardDetails.html",{"cats":cats})
    else:
        #Buyer
        #list_display = ('id','uname','card_no','cvv','expiry','balance')
        uname = request.POST["uname"]
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            #Payment done
            buyer = Payment.objects.get(uname=uname,card_no=cardno,cvv=cvv,expiry=expiry)
            owner = Payment.objects.get(uname='owner',card_no="222",cvv="222",expiry="12/2025")
            amt = float(request.session["total"])
            buyer.balance -= amt
            owner.balance += amt
            buyer.save()
            owner.save()

            #Update Order Master and delete from MyCart
            items = MyCart.objects.filter(user = request.session["uname"])
            prd_details = []

            for item in items:
                prd_details.append(item.grocery.gname)

            o1 = Order_Master()
            o1.username = request.session["uname"]
            o1.date_of_order = datetime.now()
            o1.amount = float(request.session["total"])
            o1.product_details = ",".join(prd_details)
            o1.save()
            print(o1)

            for item in items:
                item.delete()
            return HttpResponse("Payment Successful")
        except:
            return HttpResponse("Invalid Card Details")
