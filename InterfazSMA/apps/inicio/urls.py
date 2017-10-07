from django.conf.urls import url
from .views import *

app_name = 'inicio'

urlpatterns = [
	url(r'^$', Inicio.as_view(), name='inicio'),
	url(r'programacion$', Programacion.as_view(), name='prog'),
	url(r'ejemplos$', Ejemplos.as_view(), name='ejemplos'),
	url(r'404$', View404.as_view(), name='404'),
	url(r'agentes$', Agentes.as_view(), name='agentes'),
	url(r'documentacion$', Documentacion.as_view(), name='doc')
]
