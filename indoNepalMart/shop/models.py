from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    query = models.TextField(max_length = 1000)
    added_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.query[0:50]}... (Contact id: {self.sno})"
    

class Order(models.Model):
    order_number = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=100 , default="")
    customer_phone_number = models.CharField(max_length = 20 , default="")
    secondary_phone_number = models.CharField(max_length = 20 , default="" , blank=True , null=True)
    customer_email = models.CharField(max_length=200 , default="" , blank=True , null = True)
    customer_address = models.CharField(max_length=200 , default="")
    product_name = models.CharField(max_length = 500 , default = "")
    product_picture = models.ImageField(upload_to='shop/client_product_images' , default="")
    product_link = models.CharField(max_length=3000 , default="")
    added_date_and_time = models.DateTimeField(auto_now_add=True)
    order_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name + f"'s order (Order number: {self.order_number})"
    

class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150 , default='')
    category = models.CharField(max_length=100 , default='')
    product_description = models.TextField(max_length=3000 , default='')
    price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to='shop/our_product_images' , default='')
    product_image_2 = models.ImageField(upload_to='shop/our_product_images' , blank=True, null=True)
    product_image_3 = models.ImageField(upload_to='shop/our_product_images' , blank=True, null=True)
    product_image_4 = models.ImageField(upload_to='shop/our_product_images' , blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    last_updated_date = models.DateField(auto_now = True)

    def __str__(self):
        return self.product_name + f" (Product id: {self.sno})"
    

class InventoryOrder(models.Model):
    order_number = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=100 , default="")
    customer_phone_number = models.CharField(max_length = 20 , default="")
    secondary_phone_number = models.CharField(max_length = 20 , default="" , blank=True , null=True)
    customer_email = models.CharField(max_length=200 , default="" , blank=True , null = True)
    customer_address = models.CharField(max_length=200 , default="")
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True , null=True)
    added_date_and_time = models.DateTimeField(auto_now_add=True)
    order_delivered = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.customer_name}'s order (Order number: {self.order_number})"
    

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    added_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.user}'s comment"