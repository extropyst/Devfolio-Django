from django import forms
from .models import user, Plant



# Creacion del formulario a partir de un modelo, usando ModelForm:
class registroForm(forms.ModelForm):
    class Meta:
        model = user  # se especifica el nombre del modelo
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'username',
                'style': 'width: 300px;',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email',
                'style': 'width: 300px;',
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'pass',
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
            return self.title  # permite definir como debe presentarse un objeto al momento de utilizar el método __str__. Al invocar el método __str__ para ese objeto se obtiene el valor de self.email. Para que el usuario vea adecuandamente el objeto cuando esté trabajando con él.



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
