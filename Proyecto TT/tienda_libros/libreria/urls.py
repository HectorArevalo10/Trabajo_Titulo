from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from libreria import views
from .views import libro_detalle_view


urlpatterns = [
    path('principal/', views.landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing_page'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('catalogo/', views.catalogo_view, name='catalogo'),  
    path('acerca_de/', views.acerca_de_view, name='acerca_de'),
    path('libro/<int:pk>/', libro_detalle_view, name='libro_detalle'),
    
    # Otras definiciones de URLs para la aplicación 'libreria'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)