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
statesApertura=['NuevasApuesta','PublicarConfigurar','AbrirApuesta']
statesCierre=['BuscarACierre','Actualizar','ComunicarJugadores']
statesPaga=['Espera','Contabilidad','Paga']

transitionsDealer = [
    { 'trigger': 'FConfiguracion', 'source': 'Configuracion', 'dest': 'ConsultarWS' },
    { 'trigger': 'NadaNuevo', 'source': 'ConsultarWS', 'dest': 'ConsultarWS'},
    { 'trigger': 'NuevaApuesta', 'source': 'ConsultarWS', 'dest': 'CreacionApuesta' },
    { 'trigger': 'BuscarOtra', 'source': 'CreacionApuesta', 'dest': 'ConsultarWS' }
]
transitionsApertura = [
    { 'trigger': 'RecibeApuesta', 'source': 'NuevaApuesta', 'dest': 'PublicarConfigurar' },
    { 'trigger': 'ApuestaConfigurada', 'source': 'PublicarConfigurar', 'dest': 'AbrirApuesta'},
    { 'trigger': 'ApuestaAbierta', 'source': 'AbrirApuesta', 'dest': 'NuevaApuesta' },
    { 'trigger': 'EApuesta', 'source': 'NuevaApuesta', 'dest': 'NuevaApuesta' }
]
transitionsCierre = [
    { 'trigger': 'A', 'source': 'BuscarACierre', 'dest': 'Actualizar' },
    { 'trigger': 'B', 'source': 'Actualizar', 'dest': 'ComunicarJugadores'},
    { 'trigger': 'C', 'source': 'ComunicarJugadores', 'dest': 'ComunicarJugadores' },
    { 'trigger': 'D', 'source': 'BuscarACierre', 'dest': 'BuscarACierre' }
]
transitionsPaga = [
    { 'trigger': 'A', 'source': 'Espera', 'dest': 'Espera' },
    { 'trigger': 'B', 'source': 'Espera', 'dest': 'Contabilidad'},
    { 'trigger': 'C', 'source': 'Contabilidad', 'dest': 'Paga' },
    { 'trigger': 'D', 'source': 'Paga', 'dest': 'Paga' }
]

dealer1 = Dealer()
apertura1 = Apertura()
cierre1 = Cierre()
paga1 = Paga()

machine1 = GraphMachine(model=dealer1, states=statesDealer, transitions=transitionsDealer,initial=statesDealer[0],title="Agente Dealer", show_conditions=True)
machine2 = GraphMachine(model=apertura1, states=statesApertura, transitions=transitionsApertura,initial=statesApertura[0],title="Agente Apertura Apuestas", show_conditions=True)
machine3 = GraphMachine(model=cierre1, states=statesCierre, transitions=transitionsCierre,initial=statesCierre[0],title="Agente Cierre Apuestas", show_conditions=True)
machine4 = GraphMachine(model=paga1, states=statesPaga, transitions=transitionsPaga,initial=statesPaga[0],title="Agente de Pagos", show_conditions=True)

dealer1.show_graph()
apertura1.show_graph()
cierre1.show_graph()
paga1.show_graph()

