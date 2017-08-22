from abstractAgent import *

class Matter(AbstractAgent):
    def set_environment(self, temp=0, pressure=101.325):
        self.temp = temp
        self.pressure = pressure
    def print_temperature(self): print("Current temperature is %d degrees celsius." % self.temp)
    def print_pressure(self): print("Current pressure is %.2f kPa." % self.pressure)


something = Matter("Estados de la materia", "Agente que muestra los cambios de la materia", 0)

states = ['liquid','solid','gas','plasma']

transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas' },
    { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
    { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
]
machine = Machine(Matter, states=states, transitions=transitions, initial='solid')
print(Matter.state)