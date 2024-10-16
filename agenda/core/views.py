from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    usuario = request.user
    if usuario.is_authenticated:
        evento = Evento.objects.all()
        print(f'Eventos encontrados: {evento}')  # Linha de depuração
    else:
        evento = Evento.objects.none()  # Retorna um QuerySet vazio se o usuário não estiver autenticado

    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


def index(request):
    return redirect('/agenda /')

