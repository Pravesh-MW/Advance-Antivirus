from .manual import Manual
from .realTime import RealTime
class Model:
    def __init__(self):
        self.test = "x"
        self.manual = Manual()
        self.realtime = RealTime()

    def get_realtime(self):
        return self.realtime

    def get_manual(self):
        return self.manual

    def set_realtime(self, realtime):
        self.realtime = realtime

    def set_manual(self, manual):
        self.manual = manual