from django.conf.urls import url
from .views import *

app_name = 'inicio'

urlpatterns = [
	url(r'^$', Inicio.as_view(), name='inicio')
]
