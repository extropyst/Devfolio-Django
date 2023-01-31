from django.urls import path
from .views import menu_view, login_view, index_view, registro_view, addmenu_view



urlpatterns = [
    path('menu/', menu_view, name="menu"),
    path('login/', login_view, name="login"),
    path('index/', index_view, name="index"),
    path('registro/', registro_view, name="registro"),
    path('addmenu/', addmenu_view, name="addmenu"),
]

