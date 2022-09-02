from django.urls import path
from .views import *



urlpatterns = [
    path('boca/', boca, name='boca'),
    path('river/', river, name='river'),
    path('sanlorenzo/', sanlorenzo, name='sanlorenzo'),
    path('', inicio, name='inicio'),
    
    
    
    path('busquedaboca/', busquedaboca, name='busquedaboca'),
    path('buscarboca/', buscarboca, name='buscarboca'),
]
