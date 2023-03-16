from django.db import models
from AdminApp.models import Grocery
from django.db.models.fields import CharField

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    grocery = models.ForeignKey(Grocery,on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"

class Payment(models.Model):
    uname = models.CharField(max_length=20)
    card_no = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length=8)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "Payment"

class Order_Master(models.Model):
    username = models.CharField(max_length=20)
    date_of_order = models.DateField()
    amount = models.FloatField(default=100)
    product_details = CharField(max_length=100)

    class Meta:
        db_table = "Order_Master"

