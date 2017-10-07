from ..environment.communication.socket_methods import *
from ..environment.resources.resources import *
from ..environment.world import *
import inspect
import threading
import random


class AbstractAgent(threading.Thread):
    """
    Set of attributes and methods that  all agents in the system have
    no matter which behavior they exhibit
    """

    def __init__(self, name, description, community_id=''):

        threading.Thread.__init__(self)
        self.setDaemon(False)
        self.community_id = community_id
        self.social_network = None
        self._name = name
        self._agent_id = random.random()
        self._description = description
        self._alive = True
        self._state = None
        self._running = False
        self._force_kill = threading.Event()
        self._force_kill.clear()
        self._environment_id = random.random()
        self._default_behavior = None
        self._behaviour_list = dict()

    @property
    def agent_id(self):
        return self._agent_id

    @property
    def description(self):
        return self._description

    @property
    def name(self):
        return self._name

    @property
    def alive(self):
        return self._alive

    @property
    def environment_id(self):
        return self._name

    #####################################################################

    def perceive(self):
        pass

    #####################################################################

    def clone(self, address=get_ipv6_interface()):
        """
       Copy the agent's code and send it to another environment
        """
        from environment.communication.socket_methods import create_message
        from environment.world import Request
        try:
            agent_code = 'from agent_factory.abstract_agent import *\n\n' + '\n' + \
                         inspect.getsource(self.__class__)
        except Exception as e:
            print('[ERROR]' + e)
            sys.exit(1)

        data = list()
        data.append(self.name)
        data.append(agent_code)

        return create_message(address, Request.CLONE, data)

    def environment_request(self, address, request, data):
        return create_message(address, request, data)

    def get_agent_info(self):
        return self.agent_id, self.community_id, self.description, self.state

    def dispersion(self):
        pass

    def get_code(self):
        return inspect.getsourcelines(self.__class__)

    def _setup(self):
        """
        Configures the agent must be overridden
        """
    pass

    def add_behaviour(self, behaviour, template=None):
        """
        Adds a new behavior to the agent
        """
        try:
            self._behaviour_list[behaviour.__name__] = template
            behaviour.set_agent(self)
            behaviour.start()
        except Exception as e:
            print

    def _register_agent(self):
        """
        Register agent in the agent's directory
        """
        pass

    def p2p_message(self):
        pass

    def community_message(self):
        pass

    def run(self):
        self._setup()
        self._running = True

    #####################################################################
