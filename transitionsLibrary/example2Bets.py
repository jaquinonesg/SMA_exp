import os, sys, inspect

cmd_folder = os.path.realpath(
    os.path.dirname(
        os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
    
from transitions import *
from transitions.extensions import GraphMachine

class Dealer(object):
    
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('Agente_Dealer.png', prog='dot')

class Apertura(object):
    
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('Agente_Apertura_Apuestas.png', prog='dot')

class Cierre(object):
    
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('Agente_Cierre_Apuestas.png', prog='dot')

class Paga(object):
    
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('betBase.png', prog='dot')


statesDealer=['Configuracion','ConsultarWS','CreacionApuesta']
transitionsDealer = [
    { 'trigger': 'FConfiguracion', 'source': 'Configuracion', 'dest': 'ConsultarWS' },
    { 'trigger': 'NadaNuevo', 'source': 'ConsultarWS', 'dest': 'ConsultarWS'},
    { 'trigger': 'NuevaApuesta', 'source': 'ConsultarWS', 'dest': 'CreacionApuesta' },
    { 'trigger': 'BuscarOtra', 'source': 'CreacionApuesta', 'dest': 'ConsultarWS' }
]
dealer1 = Dealer()
machine1 = GraphMachine(model=dealer1, 
                       states=statesDealer, 
                       transitions=transitionsDealer,
                       initial=statesDealer[0],
                       title="Agente Dealer",
                       show_conditions=True)
dealer1.show_graph()

