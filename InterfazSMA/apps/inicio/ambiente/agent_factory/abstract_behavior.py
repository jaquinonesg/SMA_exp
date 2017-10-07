import threading


class AbstractBehaviour(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(False)
        self.my_owner = None
        self._force_kill = threading.Event()
        self._exit_code = 0

    def _behave(self):
        """
        main loop
        must be overridden
        """
        pass

    def on_start(self):
        """
        This method runs when the behavior starts
        """
        pass

    def on_end(self):
        """
        this method runs when the behavior stops
        """
        pass

    def set_agent(self, agent):
        """
        Sets the agent which controls the behavior
        """
        self.my_owner = agent

    def done(self):
        """
        returns True if the behavior has finished
        else returns False
        """
        return False

    def run(self):
        self.on_start()
        try:
            while (not self.done()) and (not self._force_kill.is_set()):
                self._exit_code = self._behave()
        except Exception as e:
            print('[ERROR] ' + str(e))
        self.on_end()
