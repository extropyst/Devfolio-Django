from django.urls import path
from .views import menu
from .views import login
from .views import index
from .views import registro
from .views import addmenu


urlpatterns = [
    path('menu/', menu, name="menu"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path('registro/', registro, name="registro"),
    path('addmenu/', addmenu, name="addmenu"),
]