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
        self.name = AbstractAgent.__name__
        self.description = description
        self.community_id = community_id

    def move(self, nameFile, path='/Users/juanpablo/PycharmProjects/agent.TLON', Type=1):
        '''Move agente to another point in network'''
        '''Type parameter allow the agent to move in diferente ways: 0 = Clone, 1 = Disperse, 2 = Migrate '''

        options = { 0 : clone,
                    1 : disperse,
                    2 : migrate }
        options[Type]()

        name = 'MouseTrap6'
        file = open('nameFile' + '.py', 'r')
        agent_code = file.read()
        file.close()

        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        # host = ('fe80::ba27:ebff:fea1:5493%bridge100', 12345, 0, 5)
        host = ('fe80::38c9:86ff:fea1:3c64', 12345, 0, 5)
        port = 12345

        message = ('_clone_', path + '/' + name + '.py', agent_code)
        m = json.dumps(message).encode('utf8')

        print('request : %s to %s' % (message[0], host))
        s.connect(host)
        print('Sending data')
        s.sendall(m)
        data = json.loads(s.recv(16382).decode('utf8'), strict=False)
        print("received data:", data)
        print('Connection close')
        s.close

    def clone(self):
        '''cloning'''
        pass
    
    def disperse(self):
        '''dispersing'''
        pass

    def migrate(self):
        '''clonning'''
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


