#!/usr/bin/python3
import sys
sys.path.append('/Users/jorge/Google Drive/Tlon/SMA/Ambiente/')
#from ..environment.communication.socket_methods import *
from ..environment.natural_laws.constants import *
from ..environment.resources.resources import *
from ..utilities.utilities import *
from ..environment.cultural_laws.control_space import *
from ..environment.cultural_laws.games.games import *


#####################################################################
#                   Environment : world
#####################################################################

class Environment(object, metaclass=Singleton):
    """Common space for MAS"""

    games_directory = {}
    agents_directory = {}
    service_directory = {}
    environments_directory = {}
    nodes_directory = {}

    def __init__(self):
        print('%%%%%%%%%%%%%%%  MAS-TLON  %%%%%%%%%%%%%%%%%')
        print('initial setup...')
        self._info_local_machine = get_info_local_machine()
        self._environment_directory = {}
        self._local_agents = {}
        self._agent_directory = {}
        self.get_instance()
        self._running = False
        #This shold be an unique Id agreed by all enviroments reachables (or not)

        self.cs = ControlSpace("TLÖN_WORLD_ControlSpace_UUID", self.get_instance())

        if not self._running:
            server_thread = Thread(target=self._initialize_server())
            server_thread.start()
            self._running = True

    def _initialize_server(self):
        try:
            c = Constants()
            world_server = ThreadedTCPServer(('', c.port), ClientThreadRequest)
            server_thread = Thread(target=world_server.serve_forever)
            server_thread.start()
        except socket.error as e:
            print("Connection error: %s" % e)
            sys.exit(0)

    @staticmethod
    def print_world():
        world = dict()
        world["Games Directory: "] = str(Environment.games_directory)
        world["Agent Directory: "] = str(Environment.agents_directory)
        world["Service Directory: "] = str(Environment.service_directory)
        world["Environments Directory: "] = str(Environment.environments_directory)
        world["Nodes Directory: "] = str(Environment.nodes_directory)

        return world, '\n'

    def get_instance(self):
        return self

    def get_games(self):
        games_directory = self.get_instance().games_directory
        print("def_get_games():", games_directory)
        return games_directory

    #######################################################################################
    # Used each time an client do a request to join de TLÖN World. It is defined by node_Id
    # that shloud be a MAC-ADDRES create_Control_Space(self, nodeId) -->
    #######################################################################################

    def create_control_space(self, node_id):
        print(self)
        cs = ControlSpace(node_id, self)
        print("create_control_space-->", cs)
        return cs

    def get_control_space(self):
        return self.cs

    @property
    def info_local_machine(self):
        return self._info_local_machine

    ###############################################################
    #                      Class REQUESTS
    ###############################################################


class Request(object):
    environment = Environment
    NODE_INFO = 'NODE_INFO'
    ACTIVE_NODES = 'ACTIVE_NODES'
    INFO_ACTIVE_NODES = 'INFO_ACTIVE_NODES'
    LOCAL_RESOURCES = 'LOCAL_RESOURCES'
    MIGRATE = 'MIGRATE'
    CLONE = 'CLONE'
    DISPERSE = 'DISPERSE'
    AGENTS_LOCATION = '../agent_factory/agents/foreign/'

    ###############################################################
    #                      A.L.F.R.E.D REQUESTS
    ###############################################################

    SET_ALFRED_DATA = 'SET_ALFRED_DATA'
    GET_ALFRED_DATA = 'GET_ALFRED_DATA'
    VIS_NET_TOPOLOGY = 'NET_TOPOLOGY'
    SET_GPSD = 'SET_GPSD'
    GET_GPSD = "GET_GPSD"

    ###############################################################
    #                       GAME REQUEST
    ###############################################################
    JOIN_GAME = 'JOIN'
    PLAY_GAME = 'PLAY'
    RESET_GAME = 'RESET'
    DO_WORK = 'WORK'
    PRINT_WORLD = "PRINT"

    def __init__(self):

        self.operation = {Request.NODE_INFO: self.node_info, Request.ACTIVE_NODES: self.active_nodes,
                          Request.INFO_ACTIVE_NODES: self.info_active_nodes, Request.CLONE: self.clone,
                          Request.GET_ALFRED_DATA: self.get_alfred_data, Request.SET_ALFRED_DATA: self.set_alfred_data,
                          Request.VIS_NET_TOPOLOGY: self.vis_net_topology,
                          Request.LOCAL_RESOURCES: self.get_resources_local_machine,
                          Request.JOIN_GAME: self.join_mas,
                          Request.RESET_GAME: self.reset_mas,
                          Request.PLAY_GAME: self.play_game,
                          Request.DO_WORK: self.work} # , Request.PRINT_WORLD: self.print_world}

        environment = Environment.get_instance(self)

    @staticmethod
    def solve(data):
        """Solve environment request"""
        request = Request()
        request_to_call = request.operation[data[0]]
        return request_to_call(data[1])

#####################################################################
    @dumps_json
    def node_info(self, data):
        try:
            return get_info_local_machine()
        except Exception as e:
            return '[ERROR] NODE_INFO: ' + str(e)

    @dumps_json
    def active_nodes(self, data):
        try:
            return get_active_nodes()
        except Exception as e:
            return '[ERROR] ACTIVE_NODES: ' + str(e)

    @dumps_json
    def info_active_nodes(self, data):
        try:
            return get_info_active_nodes()
        except Exception as e:
            return '[ERROR] INFO_ACTIVE_NODES: ' + str(e)

    @dumps_json
    def get_resources_local_machine(self, data):
        try:
            return get_resources_local_machine()
        except Exception as e:
            return '[ERROR] LOCAL_RESOURCES: ' + str(e)

    @dumps_json
    def clone(self, data):

        # f = open(Request.AGENTS_LOCATION + "__init__.py", 'a')
        # f.writelines("from ." + data[0].lower() + " import*\n")
        # f.close()

        try:
            file = open(Request.AGENTS_LOCATION + data[0].lower() + '.py', 'w')
            file.writelines(data[1])
            file.close()
            return "Agent -" + data[0] + "- cloned successfully into " + get_ipv6_interface()+"."
        except IOError as e:
            return "The agent could not be cloned! " + str(e)

    @dumps_json
    def migrate(self, data):
        # TODO complete this function :(
        pass

    @dumps_json
    def disperse(self, data):
        # TODO complete this function :(
        pass

#####################################################################
#                         A.L.F.R.E.D
#####################################################################

    @dumps_json
    def set_alfred_data(self, data):
        try:
            return set_alfred_data(data[0], data[1])
        except Exception as e:
            return '[ERROR]: SET_ALFRED_DATA ' + str(e)

    @dumps_json
    def get_alfred_data(self, data):
        try:
            return get_alfred_data(data[0])
        except Exception as e:
            return '[ERROR]: GET_ALFRED_DATA ' + str(e)

    @dumps_json
    def vis_net_topology(self, data):
        try:
            return vis_net_topology()
        except Exception as e:
            return '[ERROR]: VIS_NET_TOPOLOGY ' + str(e)

    @dumps_json
    def set_GPSD(self, data):
        # TODO complete this function :(
        pass

    @dumps_json
    def get_GPSD(self, data):
        # TODO complete this function :(
        pass

#####################################################################
#                   GAME FUNCTIONS
#####################################################################

    @dumps_json
    def join_mas(self, data):
        try:
            return join_mas(data,self.environment)
        except Exception as e:
            return '[ERROR]: ' + str(e)

    @dumps_json
    def reset_mas(self, data):
        try:
            return reset_mas(self.environment)
        except Exception as e:
            return '[ERROR]: ' + str(e)

    @dumps_json
    def play_game(self, data):
        try:
            return play_game(data,self.environment)
        except Exception as e:
            return '[ERROR]: ' + str(e)

    @dumps_json
    def work(self, data):
        try:
            return work(data, self.environment)
        except Exception as e:
            return '[ERROR]: ' + str(e)


def main():
    """
    ############################################################
    #               Environment - Initial Setup
    ############################################################
    """
    environment = Environment()
    print('Info-Local Machine : %s' % str(environment.info_local_machine))
    print('Waiting for new requests...')


if __name__ == "__main__":
    # execute only if run as a script
    main()
