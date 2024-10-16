"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("agenda/", views.lista_eventos, name="lista_eventos"),
    path("", views.index),
    path("agenda/evento/delete/<int:id_evento>", views.delete_evento, name="delete_evento"),
    path('login/', views.login_user, name="login"),
    path("agenda/evento/submit", views.submit_evento),
    path('login/submit', views.submit_login),
    path('agenda/lista', views.json_lista_evento),
    path('logout/', views.logout_user),
    path("agenda/evento/", views.evento, name="evento"),
]
