from .models import Plant
from .forms import addmenuForm, menuForm, registroForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.


@csrf_protect
def registro_view(request):
    template_name = 'core/registro.html'
    modelClass = registroForm()
    context = {'form': modelClass}

    if request.method == 'POST':
        # comprobar si los datos del formulario son válidos
        if modelClass.is_valid():
            # guardar los datos del formulario en el modelo
            modelClass.save()
            context['mensaje'] = "Guardado correctamente"
            messages.success(
                request, f'Tu cuenta ha sido creada. ¡Ya puedes iniciar sesión!')
            return HttpResponseRedirect(reverse('login'))

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
    context = {'object': modelClass}

    if request.method == 'POST':
        modelClass = addmenuForm(request.POST)
        # comprobar si los datos del formulario son válidos
        if modelClass.is_valid():
            # guardar los datos del formulario en el modelo
            modelClass.save()
            context['mensaje'] = "Guardado correctamente"

    return render(request, template_name, context)




# @csrf_protect
# def carro_view(request):
#     template_name = 'core/carro.html'
#     modelClass = Carro.objects.all()
#     context = {'producto': modelClass}
#     return render(request, template_name, context)

@csrf_protect
@login_required
def index_view(request):
    return render(request, 'core/index.html')
