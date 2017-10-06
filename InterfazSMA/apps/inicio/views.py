from django.views.generic import TemplateView
from django.shortcuts import render

class Inicio(TemplateView):
    template_name = 'inicio/index.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Inicio',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            }
        }
        return render(request, self.template_name, context)

