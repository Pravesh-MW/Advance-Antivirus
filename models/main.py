from .manual import Manual
from .realTime import RealTime
from multiprocessing import Process
# from .Hash.signatureBased import MalwareDetector
from .Threading import WorkerPool
import time
import threading


class Model:
    def __init__(self):
        self.test = "x"
        self.manual = Manual()
        self.realtime = RealTime()
        self.Master = Process
        self.realTimeProcess = None
        # self.engine = MalwareDetector()
        # self.manual.malware_scan_md5= self.engine.malware_checker_md5
        self.worker = threading.Thread(target=self.realtime.start_runTime, args=())
        # self.worker.start()
        self.threading = WorkerPool()
    def get_realtime(self):
        return self.realtime

    def get_manual(self):
        return self.manual

    def set_realtime(self, realtime):
        self.realtime = realtime

    def set_manual(self, manual):
        self.manual = manual
