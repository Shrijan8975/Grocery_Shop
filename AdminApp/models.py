from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "Categorty"

class Grocery(models.Model):
    gname = models.CharField(max_length=20)
    price = models.FloatField(default=200)
    description = models.CharField(max_length=100)
    imageurl = models.ImageField(upload_to='images')
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.gname

    class Meta:
        db_table = "Grocery"
