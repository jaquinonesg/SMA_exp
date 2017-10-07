from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.defaults import page_not_found
from .forms import *
from .ambiente.main import *

class Gatito():
    def _init_(self):
        print("cacorrada")

def error_404(request):
    nombre_template = '404.html'

    return page_not_found(request, template_name=nombre_template)

class Inicio(TemplateView):
    template_name = 'inicio/index.html'
    context = {
        'header': {
            'title': '',
            'subtitle': '',
            'breadcrumb': [
                { 'name': 'Inicio' }
            ],
            'options': [],
        }
    }

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        r = ReactiveFsm("perrito",2)
        print (r)
        return context

class Programacion(TemplateView):
    template_name = 'inicio/programacion.html'
    form_class = AgenteForm
    context = {
        'header': {
            'title': '',
            'subtitle': '',
            'breadcrumb': [
                { 'name': 'Inicio' }
            ],
            'options': [],
        }
    }

    def get_context_data(self, **kwargs):
        context = super(Programacion, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            agente = form.save(commit=False)
            nombre = request.POST['nombre']
            estado = request.POST['estado']
            transicion = request.POST['transicion']
            agente.save()
            self.context['form'] = form
            self.context['creado'] = 'Agente creado exitosamente'
            return render(request,self.template_name,self.context)




    #def get(self, request):
    #    code = """
#perrito = self.Perrito('hola')
#print (perrito)
#"""
#        print(eval("self.Perrito('hola')"))
        #eval("print(context)")
        #exec("a = Gatito()")
        #loc = {}
        #exec("a = Gatito()", {}, loc)
        #a = loc['a']
        #print(a)
#        return render(request, self.template_name, context)
