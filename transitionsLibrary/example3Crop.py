import os, sys, inspect

cmd_folder = os.path.realpath(
    os.path.dirname(
        os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
    
from transitions import *
from transitions.extensions import GraphMachine

class Scrops(object):

    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('SCrops.png', prog='dot')

states=['Inicio','TomarMedida','EnviarMedida','Terminar']

transitions = [
    { 'trigger': 'ConfiguracionTerminada', 'source': 'Inicio', 'dest': 'TomarMedida' },
    { 'trigger': 'ProcesadoConjunto', 'source': 'TomarMedida', 'dest': 'EnviarMedida' },
    { 'trigger': 'Apagar', 'source': 'Inicio', 'dest': 'Terminar' },
    { 'trigger': 'Apagar', 'source': 'Tomarmedida', 'dest': 'Terminar' },
    { 'trigger': 'Apagar', 'source': 'EnviarMedida', 'dest': 'Terminar' },
    { 'trigger': 'MedirDeNuevo', 'source': 'EnviarMedida', 'dest': 'TomarMedida' },
    { 'trigger': 'ContinuarMidiendo', 'source': 'TomarMedida', 'dest': 'TomarMedida' }
]

model = Scrops()
machine = GraphMachine(model=model, 
                       states=states, 
                       transitions=transitions,
                       initial='Inicio',
                       show_auto_transitions=False, # default value is False
                       title="Agente",
                       show_conditions=True)
model.show_graph()

