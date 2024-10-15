from django.contrib import admin
from core.models import Evento


# Register your models here.


#
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', "data_evento", "data_criacao")



#registrando o modelo dos eventos e vinculando com a classe feita para administrar 
admin.site.register(Evento, EventoAdmin)
