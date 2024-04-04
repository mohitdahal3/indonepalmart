from django.contrib import admin

# Register your models here.
from shop.models import Contact, Order, Product, InventoryOrder, Comment

admin.site.register(Contact)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('added_date_and_time',)
admin.site.register(Order , OrderAdmin)



class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('last_updated_date',)
admin.site.register(Product , ProductAdmin)




class InventoryOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('added_date_and_time',)
admin.site.register(InventoryOrder , InventoryOrderAdmin)




class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('added_date',)
admin.site.register(Comment , CommentAdmin)