from django.contrib import admin
from django.urls import path,include
from UserApp import views
urlpatterns = [
    path('', views.home),
    path('ShowProduct/<gid>',views.ShowProduct),
    path('SignUp/',views.SignUp),
    path('Login',views.Login),
    path('Logout',views.Logout),
    path('ViewDetails/<grocery_id>',views.ViewDetails),
    path('AddToCart',views.AddToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('Makepayment',views.makepayment),


]
