from django.urls import path
from .views import menu_view, index_view, addmenu_view, registro_view


urlpatterns = [
    path('menu/', menu_view, name="menu"),
    path('index/', index_view, name="index"),
    path('registro/', registro_view, name="registro"),
    path('addmenu/', addmenu_view, name="addmenu"),
    
    # path('carro/', carro_view, name="carro"),
]