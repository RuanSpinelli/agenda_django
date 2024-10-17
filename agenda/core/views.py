from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect("/agenda/")



def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.method == 'POST':
        # Corrigir a forma de obter os dados de login
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/agenda/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/login/')


@login_required(login_url="/login/")
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario= usuario)    
    dados = {'eventos': evento}
    return render(request , 'agenda.html', dados)
    """
    eventos = Evento.objects.all()  # Obtém todos os eventos
    return render(request, 'agenda.html', {'eventos': eventos})  # Certifique-se de que 'agenda.html' está no caminho correto
    """





