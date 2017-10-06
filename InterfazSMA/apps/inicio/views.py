from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.defaults import page_not_found

def error_404(request):
    nombre_template = '404.html'
 
    return page_not_found(request, template_name=nombre_template)

class Inicio(TemplateView):
    template_name = 'inicio/index.html'

    class Perrito():
        def __init__(self, num_patas):
            self.num_patas= num_patas
            print(num_patas)
            

    def get(self, request):
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
        return render(request, self.template_name, context)

