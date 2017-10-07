from ...agent_factory.abstract_behavior import AbstractBehaviour
import time


class OneShotBehavior(AbstractBehaviour):
    """
    This behavior is only executed once. This model was based in
    the SPADE behaviors library. You can check it in https://pypi.python.org/pypi/SPADE
    """
    def __init__(self):
        AbstractBehaviour.__init__(self)
        self._first_time = True

    def _single_action(self):
        pass

    def _behave(self):
        self._single_action()
        return self._exit_code

    def done(self):
        if self._first_time is True:
            self._first_time = False
            return False
        return True

############################################################


class PeriodicBehaviour(AbstractBehaviour):
    """
    This behavior runs periodically with a period. This model was taken of
    the SPADE behaviors library. You can check it in https://pypi.python.org/pypi/SPADE
    """

    def __init__(self, period, time_start=None):
        AbstractBehaviour.__init__(self)
        self._period = period
        if time_start is None:
            self._next_activation = time.time()
        else:
            self._next_activation = time_start

    def get_period(self):
        return self._period

    def set_period(self, period):
        self._period = period

    def _behave(self):
        if time.time() >= self._next_activation:
            self._exit_code = self._on_tick()
            while self._next_activation <= time.time():
                self._next_activation += self._period
        else:
            t = self._next_activation - time.time()
            if t > 0:
                time.sleep(t)
        return self._exit_code

    def _on_tick(self):
        """
        This method is executed every period must be overridden
        """
        raise NotImplementedError

############################################################


class TimeOutBehaviour(PeriodicBehaviour):

    """
    This behavior is executed only once after a timeout. This model was taken of
    the SPADE behaviors library. You can check it in https://pypi.python.org/pypi/SPADE
    """
    def __init__(self, timeout):
        PeriodicBehaviour.__init__(self, timeout, time.time() + timeout)
        self.stop = False

    def get_time_out(self):
        return self.getPeriod()

    def done(self):
        return self.stop

    def _on_tick(self):
        if self.stop is False:
            self.time_out_action()
        self.stop = True

    def time_out_action(self):
        """
        This method is executed after the timeout must be overridden
        """
        raise NotImplementedError
