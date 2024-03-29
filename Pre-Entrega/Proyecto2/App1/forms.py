from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class blogForms(forms.Form):
    id= forms.IntegerField()
    
    titulo = forms.CharField(max_length=30)

    subtitulo= forms.CharField(max_length=30)

    contenido = forms.CharField(max_length=40)

    autor = forms.CharField(max_length=40)


class UserEditForm(UserCreationForm):
    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True)