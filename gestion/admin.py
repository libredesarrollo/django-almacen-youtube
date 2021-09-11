from django.contrib import admin

from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    fields = ('title',)

admin.site.register(Category, CategoryAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','category')
    #fields = ('title','title','price','category')

#admin.site.register(Product, ProductAdmin)