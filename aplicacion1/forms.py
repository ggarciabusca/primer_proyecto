from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ["username", "email", "last_name", "password1", "password2"]

