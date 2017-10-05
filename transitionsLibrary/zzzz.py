from transitions import Machine
from transitions.extensions import GraphMachine


#Clase de integracion con transitionsLib
class Test():
    def __init__(self, states, transitions, initial):
        self.prop1 = ''
        self.states = states
        self.machine = Machine(model=self, states=states, initial=initial, transitions=transitions)

#Clase de integracion con transitionsLib y grafo asociado
class TestG():
    def __init__(self, states, transitions, initial):
        self.prop1 = ''
        self.states = states
        self.machine = GraphMachine(model=self, states=states, initial=initial, show_auto_transitions=False, title="Test", transitions=transitions)
    
    def show_graph(self, **kwargs):
        self.get_graph(**kwargs).draw('TestG.png', prog='dot')



states = ['a','b','c','d']
transition = [
    { 'trigger': 'at', 'source': 'a', 'dest': 'b' },
    { 'trigger': 'bt', 'source': 'b', 'dest': 'c' },
    { 'trigger': 'ct', 'source': 'c', 'dest': 'd' },
    { 'trigger': 'dt', 'source': 'd', 'dest': 'a' },
]

ex = Test(states,transition,states[0])
ex2 = TestG(states,transition,states[0])
ex2.show_graph()

class Cheese(object):
    def __init__(self, num_holes=0, p1='',p2=''):
        "defaults to a solid cheese"
        self.number_of_holes = num_holes
        print(num_holes, p1, p2)

    @classmethod
    def random(cls,num_holes,p1,p2):
        print("aqui1")
        return cls(num_holes,"a","b")

print("a")
a = Cheese()
print("b")
b = Cheese(2)
print("c")
c = Cheese.random(10,"zzz","xxx")