from .models import Plant   
from .forms import addmenuForm, menuForm, registroForm   # , Add2CartForm, Cart
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect


from django.views.decorators.http import require_POST



# Create your views here.


@csrf_protect
@login_required
def index_view(request):
    return render(request, 'core/index.html')



@csrf_protect
def registro_view(request):
    template_name = 'core/registro.html'
    modelClass = registroForm()
    context = {'form': modelClass}

    if request.method != 'POST':
        modelClass = registroForm()
    else:
        modelClass = registroForm(request.POST)
        if modelClass.is_valid():
            modelClass.save()
            context['mensaje'] = "Guardado correctamente"
            messages.success(
                request, f'Tu cuenta ha sido creada. ¡Ya puedes iniciar sesión!')
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse("Su nombre de usuario y contraseña no coinciden.")
    return render(request, template_name, context)





# @csrf_protect
# def login_view(request):
#     template_name = 'core/login.html'
#     modelClass = LoginForm()  # crear objeto de formulario
#     context = {'form': modelClass}
#     p = Person.objects.get(username=request.POST['username'])

#     if request.method == 'POST':
#         request.session.set_test_cookie()
#         if request.session.test_cookie_worked():
#             request.session.delete_test_cookie()
#             if p.check_password(request.POST['password']):
#                 request.session['person_id'] = p.id
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Your username and password didn't match.")
#         else:
#             return HttpResponse("Please enable cookies and try again.")
#     return render(request, template_name, context)


@csrf_protect
@login_required
def menu_view(request):
    template_name = 'core/menu.html'
    modelClass = Plant.objects.all()
    context = {'planta': modelClass}

    if request.method == 'POST':
        modelClass = menuForm(request.POST)
        # comprobar si los datos del formulario son válidos
        if modelClass.is_valid():
            # guardar los datos del formulario en el modelo
            modelClass.save()
            context['mensaje'] = "Guardado correctamente"

    return render(request, template_name, context)


@csrf_protect
@login_required
def addmenu_view(request):
    template_name = 'core/addmenu.html'
    modelClass = addmenuForm()
    context = {'form': modelClass}

    if request.method == 'POST':
        modelClass = addmenuForm(request.POST)
        # comprobar si los datos del formulario son válidos
        if modelClass.is_valid():
            # guardar los datos del formulario en el modelo
            modelClass.save()
            context['mensaje'] = "Guardado correctamente"
            messages.success(
                request, f'Tu cuenta ha sido creada. ¡Ya puedes iniciar sesión!')
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse("Revisa los datos ingresados nuevamente por favor.")
    return render(request, template_name, context)





# CARRO DE COMPRAS #




# @csrf_protect
# @login_required
# def carro_view(request):
#     cart = Cart(request)
#     return render(request, template_name='core/carro.html', context={'cart': cart})


# @csrf_protect
# @login_required
# @require_POST
# def cart_add(request, Plant_id):
#     cart = Cart(request)
#     Plant = get_object_or_404(Plant, id=Plant_id)
#     form = Add2CartForm(request.POST)

#     if form.is_valid():
#         data = form.cleaned_data
#         cart.add(planta=Plant, quantity=data['quantity'])
#     return redirect('cart:detail')


# @csrf_protect
# @login_required
# def cart_remove(request, Plant_id):
#     cart = Cart(request)
#     Plant = get_object_or_404(Plant, id=Plant_id)
#     cart.remove(Plant)
#     return redirect('cart:detail')







