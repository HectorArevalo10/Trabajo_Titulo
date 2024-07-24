from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')
    phone_number = forms.CharField(label='Número de teléfono')
    birth_date = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'birth_date', 'password1', 'password2')