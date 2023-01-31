from .forms import LoginForm, addmenuForm, registroForm
from .models import Plant, Person
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import Plant
from .models import Person
from .forms import LoginForm

# Create your views here.


@csrf_protect
def login_view(request):
 #crear objeto de formulario
    context = {'form': LoginForm()}

    if request.method== 'POST':
        formulario = LoginForm(request.POST)

        # comprobar si los datos del formulario son válidos
        if formulario.is_valid():
            # guardar los datos del formulario en el modelo
            formulario.save()
            context['mensaje'] = "Guardado correctamente"

    # datos['form'] = form
    return render(request, "core/login.html", context)






# @csrf_protect
# def login_view(request):
#     template_name = 'core/login.html'
#     modelClass = LoginForm()  # crear objeto de formulario
#     context = {'form': modelClass}

#     if request.method == 'POST':
#         modelClass = LoginForm(request.POST)
#         # comprobar si los datos del formulario son válidos
#         if modelClass.is_valid():
#             # guardar los datos del formulario en el modelo
#             modelClass.save()
#             context['mensaje'] = "Guardado correctamente"

#     return render(request, template_name, context)





@csrf_protect
def menu_view(request):
    template_name = 'core/menu.html'
    modelClass = Plant.objects.all()
    context = {'plantas': modelClass}
    return render(request, template_name, context)


@csrf_protect
def registro_view(request):
    template_name = 'core/registro.html'
    modelClass = registroForm()
    context = {'object': modelClass}
    return render(request, template_name, context)


@csrf_protect
def addmenu_view(request):
    template_name = 'core/addmenu.html'
    modelClass = addmenuForm()
    context = {'object': modelClass}
    return render(request, template_name, context)


def index_view(request):
    return render(request, 'core/index.html')
