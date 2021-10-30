from pybricks.tools import StopWatch

TIMER = StopWatch()
class Logger():
    i = 0
    def time(self):
        print(str(self.i) + " " + str(TIMER.time()))
        self.i += 1
LOGGER = Logger()