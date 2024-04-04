from django.shortcuts import render, HttpResponse, redirect
from shop.models import Contact, Order, Product, InventoryOrder, Comment
import re
from django.contrib import messages
from django.contrib.auth import logout




# Create your views here.
def home(request):
    all_comments = Comment.objects.all()
    dictionary = {}

    dictionary["comment_activated"] = True
    dictionary["comments"] = all_comments
    return render(request , 'shop/home.html' , dictionary)





def contact(request):
    all_comments = Comment.objects.all()
    dictionary = {}
    if request.method == 'POST':
        _name = request.POST.get('name' , "")
        _email = request.POST.get('email' , "")
        _phone = request.POST.get('phone' , "")
        _query = request.POST.get('message' , "")

        if( validate_email(_email) == False ):
            messages.error(request , "Please enter a valid email!")
            redirect("/contact")
        else:
            try:
                new_query = Contact(name = _name , email = _email , phone = _phone , query = _query)
                new_query.save()
                messages.success(request , "Message sent successfully!")
            except:
                messages.error(request , "An error has occurred! Try changing some values.")
                redirect("/contact")

    dictionary["comment_activated"] = True
    dictionary["comments"] = all_comments
    return render(request , 'shop/contact.html' , dictionary)






def products(request):
    all_comments = Comment.objects.all()
    all_products = Product.objects.all()

    hasAtleastOneStock = False
    for product in all_products:
        if(product.stock > 0):
            hasAtleastOneStock = True
            break


    dictionary = {
        "products" : all_products,
        "inventory_populated" : hasAtleastOneStock
    }
    dictionary["comment_activated"] = True
    dictionary["comments"] = all_comments

    return render(request , 'shop/products.html' , dictionary)






def searchProduct(request):
    dictionary = {}
    if request.method == "GET":
        _query = request.GET.get("query" , "")
        all_products = Product.objects.all()
        my_products = []
        for product in all_products:
            if( (product.product_name.lower().find(_query.lower()) != -1 or product.category.lower().find(_query.lower()) != -1 or product.product_description.lower().find(_query.lower()) != -1) and (product.stock > 0) ):
                my_products.append(product)
        dictionary['products'] = my_products
        dictionary['query'] = _query

    return render(request , 'shop/searchProduct.html' , dictionary)






def productView(request , id):
    product = Product.objects.get(sno = id)

    dictionary = {
        'product' : product
    }
    return render(request , 'shop/productView.html' , dictionary)







def order(request):
    all_comments = Comment.objects.all()
    dictionary = {}

    if request.method == "POST":
        _name = request.POST.get("name")
        _email = request.POST.get("email" , "")
        _phone1 = request.POST.get("phone1")
        _phone2 = request.POST.get("phone2" , "")
        _address = request.POST.get("address")
        _productName = request.POST.get("productName")
        _image = request.FILES["image"]
        _url = request.POST.get("url")



        if(validate_email_canbeempty(_email) == False):
            messages.error(request , "Please enter a valid email!")
            redirect('/order')
        else:
            try:
                new_order = Order(customer_name = _name , customer_phone_number = _phone1 , secondary_phone_number = _phone2 , customer_email = _email , customer_address = _address , product_name = _productName , product_picture = _image , product_link = _url)
                new_order.save()
                order_number = new_order.order_number
                order_title = new_order.product_name
                messages.success(request , "Order sent successfully!")

                dictionary = {
                    "order_number" : order_number,
                    "order_title" : order_title
                }

            except:
                messages.error(request , "An error has occurred!")
                redirect('/order')
    dictionary["comment_activated"] = True
    dictionary["comments"] = all_comments
    return render(request , 'shop/order.html' , dictionary)





def orderFromInventory(request , id):
    product = Product.objects.get(sno = id)
    dictionary = {
        'product' : product
    }


    if request.method == "POST":
        _name = request.POST.get("name")
        _email = request.POST.get("email")
        _phone1 = request.POST.get("phone1")
        _phone2 = request.POST.get("phone2" , "")
        _address = request.POST.get("address")

        if(validate_email_canbeempty(_email) == False):
            messages.error(request , "Please enter a valid email!")
            redirect(f'/order-from-inventory/{product.sno}')
        else:
            try:
                new_inventory_order = InventoryOrder(customer_name = _name , customer_phone_number = _phone1 , secondary_phone_number = _phone2 , customer_email = _email , customer_address = _address , product = product)
                new_inventory_order.save()
                order_number = new_inventory_order.order_number
                order_title = new_inventory_order.product.product_name
                messages.success(request , "Order sent successfully!")

                dictionary['order_number'] = order_number
                dictionary['order_title'] = order_title

            except:
                messages.error(request , "An error has occurred!")
                redirect(f'/order-from-inventory/{product.sno}')

    

    return render(request , 'shop/orderFromInventory.html' , dictionary)






def addComment(request):
    if(request.method == "POST"):
        _comment = request.POST.get("comment")
        _comment = _comment.strip()
        if(len(_comment) < 1):
            messages.error(request , "Comment cannot be empty!")
            redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            try:
                _user = request.user
                new_comment = Comment(user = _user , comment = _comment)
                new_comment.save()
                redirect(request.META.get('HTTP_REFERER', '/'))
            except:
                messages.error(request , "Some error has occurred!")
                redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect(request.META.get('HTTP_REFERER', '/'))






def handleLogout(request):
    logout(request)
    return redirect('/')






def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def validate_email_canbeempty(email):
    if (email.strip() == "" or email is None):
        return True
    else:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None