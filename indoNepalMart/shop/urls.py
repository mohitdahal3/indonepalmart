from django.urls import path
from shop import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('contact' , views.contact , name="contact"),
    path('products' , views.products , name="products"),
    path('order' , views.order , name="order"),
    path('productview/<int:id>' , views.productView , name = "productView"),
    path('order-from-inventory/<int:id>' , views.orderFromInventory , name = "orderFromInventory"),
    path('search-product' , views.searchProduct , name="searchProduct"),
    path('logout' , views.handleLogout , name="logoutpage"),
    path('addcomment' , views.addComment , name="addComment"),
]
