from django.urls import path
from . import views

urlpatterns = [
    # URL padrão para a lista de eventos
    path('', views.lista_eventos, name='lista_eventos'),
]
