from django.contrib import admin
from AdminApp.models import Category,Grocery


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','price','description','imageurl','cat_id')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Grocery,GroceryAdmin)


