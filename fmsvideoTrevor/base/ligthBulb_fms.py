from random import randint
from time import clock


#===================================
#State based class
State = type("State", (object,), {})

class LigthOn(State):
    def Execute(self):
        print ("Light is ON")

class LightOff(State):
    def Execute(self):
        print ("Light is OFF")

#===================================

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print("Transitioning...")

#===================================

class SimpleFSM(object):
    def __init__(self,char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None

    def SetState(self, stateName):
        self.curState = self.states[stateName]
    
    def Transition(self, transName):
        self.trans = self.transitions[transName]
    
    def Execute(self):
        if(self.trans):
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.curState.Execute()

#===================================

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True

#===================================

if __name__ == "__main__":
    light = Char()
    
    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    
