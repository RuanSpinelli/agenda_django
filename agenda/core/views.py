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
    dados = {
        'eventos': evento,
        'nome_usuario': usuario.username
        }
    return render(request , 'agenda.html', dados)
    """
    eventos = Evento.objects.all()  # Obtém todos os eventos
    return render(request, 'agenda.html', {'eventos': eventos})  # Certifique-se de que 'agenda.html' está no caminho correto
    """


@login_required(login_url="/login/")
def evento(request):
    id_evento = request.GET.get("id")
    dados = {}

    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, "evento.html", dados)


@login_required(login_url="/login/")
def submit_evento(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        data_evento = request.POST.get("data_evento")
        descricao = request.POST.get("descricao")
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()


            # É uma forma de fazer a solução
            """
            Evento.objects.filter(id=id_evento).update(titulo= titulo, 
                                                       data_evento= data_evento,
                                                       descricao= descricao)
            """
        else:
            Evento.objects.create(titulo=titulo, 
                                data_evento=data_evento, 
                                descricao= descricao, 
                                usuario= usuario)
        
    
    return redirect("/")

@login_required(login_url="/login/")
def delete_evento(request, id_evento):

    usuario = request.user
    evento = Evento.objects.get(id=id_evento) # Apaga um evento específico com base no id
    
    if usuario == evento.usuario:
        evento.delete()
    return redirect("/")


