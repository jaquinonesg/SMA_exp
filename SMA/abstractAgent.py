import random
import socket
import json
from transitions import Machine

class AbstractAgent(object):
    '''Basic structure of an agent in SMA'''
    states = []

    def __init__(self, description, community_id):
        ''' '''
        self.id = random.random()
        self.name = AbstractAgent.__name__
        self.description = description
        self.community_id = community_id

    def mobility(self):
        ''' mobility '''
        pass
    
    def state_diagram(self):
        ''' printStateDiagram '''
        pass
    
    def comunication(self):
        ''' comunication '''
        pass

    def log(self):
        ''' log '''
        pass
    
    def handling(self):
        ''' handling '''
        pass



