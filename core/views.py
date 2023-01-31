from django.shortcuts import render
from .models import Plant
from .models import Person

# Create your views here.

#Plant.site.register(Plant)

def menu(request):
    plantas= Plant.objects.all()
    datos = {
        'plantas': plantas
    }
    return render(request,'core/menu.html', datos)

def login(request):
    return render(request,'core/login.html')

def index(request):
    return render(request,'core/index.html')


def registro(request):
    return render(request,'core/registro.html')

    
def addmenu(request):
    return render(request,'core/addmenu.html')

    
