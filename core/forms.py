from django import forms
from .models import Plant
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# CART_SESSION_ID = 'cart'




# class Add2CartForm(forms.Form):
#     quantity = forms.IntegerField(min_value=1, max_value=9,
#                                   widget=forms.NumberInput(attrs={
#          'class': 'form-control',
#          'placeholder': 'quantity',
#          }))



class registroForm(UserCreationForm):

        email = forms.EmailField()
        first_name = forms.CharField(max_length=150)
        last_name = forms.CharField(max_length=150)
        # password1 = forms.CharField(max_length=128)
        # password2 = forms.CharField(max_length=128)
        class Meta:
            model = User  # se especifica el nombre del modelo

            fields = ['username', 'first_name',
                    'last_name', 'email', 'password1', 'password2']
            widgets = {
                # 'username': forms.TextInput(attrs={
                #     'placeholder': 'username',
                #     'style': 'width: 300px;',
                #     'class': 'form-control',
                # }),
                'first_name': forms.TextInput(attrs={
                    'placeholder': 'Nombre',
                    'style': 'width: 300px;',
                    'class': 'form-control',
                }),
                'last_name': forms.TextInput(attrs={
                    'placeholder': 'Apellido',
                    'style': 'width: 300px;',
                    'class': 'form-control',
                }),
                'email': forms.EmailInput(attrs={
                    'placeholder': 'email',
                    'style': 'width: 300px;',
                    'class': 'form-control',
                }),
                'password1': forms.PasswordInput(attrs={
                    'placeholder': 'Contraseña',
                    'style': 'width: 300px;',
                    'class': 'form-control',
                }),
                'password2': forms.PasswordInput(attrs={
                    'placeholder': 'Repita Contraseña',
                    'style': 'width: 300px;',
                    'class': 'form-control',
                }),
            }




# error_messages = {
#     "unique": "El correo ya se encuentra registrado"}




# Creacion del formulario a partir de un modelo, usando ModelForm:
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Person  # se especifica el nombre del modelo
#         fields = "__all__"  # valor especial del atributo de campos para indicar que se deben usar todos los campos del modelo
#         widgets = {
#             'email': forms.EmailInput(attrs={
#                 'placeholder': 'email', 
#                 'style': 'width: 300px;', 
#                 'class': 'form-control', 
#                 }),
#             'password': forms.PasswordInput(attrs={
#                 'placeholder': 'pass', 
#                 'style': 'width: 300px;', 
#                 'class': 'form-control', 
#                 }),
#         }





class addmenuForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"

        def __str__(self):
            return self.common_name



class menuForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"

        def __str__(self):
            return self.title  # permite definir como debe presentarse un objeto al momento de utilizar el método __str__. Al invocar el método __str__ para ese objeto se obtiene el valor de self.email. Para que el usuario vea adecuandamente el objeto cuando esté trabajando con él.






















# class LoginForm(forms.Form):
#     email = forms.EmailField(
#         required=True,
#         label='Correo: *',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control', 
#             'autocomplete': 'off',            
#             'id': 'email'
#         })
#     )
#     password = forms.CharField(
#         max_length=8,
#         required=True,
#         label='Contraseña: *',
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control', 
#             'autocomplete': 'off',            
#             'id': 'password'
#         })
#     )


# class Cart:
#     def __init__(self, request):
#         self.session = request.session
#         self.cart = self.add_cart_session()

#     def __iter__(self):
#         Plant_ids = self.cart.keys()
#         Plants = Plant.objects.filter(id__in=Plant_ids)
#         cart = self.cart.copy()
#         for Plant in Plants:
#             cart[str(Plant.id)]['Plant'] = Plant
#         for item in cart.values():
#             item['total_price'] = int(item['price']) * int(item['quantity'])
#             yield item

#     def add_cart_session(self):
#         cart = self.session.get(CART_SESSION_ID)
#         if not cart:
#             cart = self.session[CART_SESSION_ID] = {}
#         return cart

#     def add(self, Plant, quantity):
#         Plant_id = str(Plant.id)

#         if Plant_id not in self.cart:
#             self.cart[Plant_id] = {
#                 'quantity': 0, 'price': str(Plant.price)}

#         self.cart.get(Plant_id)['quantity'] += quantity
#         self.save()

#     def remove(self, Plant):
#         Plant_id = str(Plant.id)
#         if Plant_id in self.cart:
#             del self.cart[Plant_id]
#             self.save()

#     def save(self):
#         self.session.modified = True

#     def get_total_price(self):
#         return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

#     def clear(self):
#         del self.session[CART_SESSION_ID]
#         self.save()
