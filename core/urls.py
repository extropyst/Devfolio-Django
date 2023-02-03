from django.urls import path
from .views import menu_view, index_view, addmenu_view, registro_view  # , carro_view, cart_add, cart_remove
from django import views

urlpatterns = [
    path('menu/', menu_view, name="menu"),
    path('index/', index_view, name="index"),
    path('registro/', registro_view, name="registro"),
    path('addmenu/', addmenu_view, name="addmenu"),
    # path('carro/', carro_view, name="cart"),
    # path('add/<int:product_id>/', cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
        
]