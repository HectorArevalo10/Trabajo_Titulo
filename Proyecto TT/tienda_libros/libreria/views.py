from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Libro
from django.views.generic import DetailView


# Create your views here.


def landing_page(request):
    login_form = LoginForm()
    register_form = RegisterForm()
    context = {
        'login_form': login_form,
        'register_form': register_form
    }
    return render(request, 'landing_page.html', context)

def acerca_de_view(request):
    return render(request, 'acerca_de.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir a la página de perfil del usuario
                return redirect('perfil')  # Asegúrate de que 'perfil' coincida con el nombre de la URL en urls.py
            else:
                # Manejar el caso de credenciales inválidas
                return render(request, 'login.html', {'form': form, 'error': True})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de inicio de sesión
            return redirect('login')  # Asegúrate de tener una URL con nombre 'login' definida en tus urls.py
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def catalogo_view(request):
    genero_seleccionado = request.GET.get('genero', 'all')
    query = request.GET.get('search', '') 
    
    if genero_seleccionado == 'all':
        libros = Libro.objects.all()
    else:
        libros = Libro.objects.filter(genero=genero_seleccionado)
        
    if query:
        libros = libros.filter(titulo__icontains=query)
        
    generos = Libro.objects.values_list('genero', flat=True).distinct()
    
    return render(request, 'catalogo.html', {
        'libros': libros,
        'generos': generos,
        'selected_genero': genero_seleccionado,
        'query': query,
    })



def libro_detalle_view(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libro_detalle.html', {'libro': libro})


@login_required
def perfil_view(request):
    return render(request, 'perfil.html')




