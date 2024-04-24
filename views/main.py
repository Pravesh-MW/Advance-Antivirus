from typing import TypedDict

from .root import Root
from .home import HomeView
from .test import TestView
from .realTime import RealTimeView
from .manual import ManualView
from .networkMonitoring import NetworkMonitoringView
from .Advance import AdvanceView

class Frames(TypedDict):
    home: HomeView
    test: TestView
    realTime: RealTimeView
    manual: ManualView
    networkMonitoring: NetworkMonitoringView
    advance: AdvanceView

class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(HomeView, "home")
        self._add_frame(TestView, "test")
        self._add_frame(RealTimeView, "realTime")
        self._add_frame(ManualView, "manual")
        self._add_frame(NetworkMonitoringView,"networkMonitoring")
        self._add_frame(AdvanceView,"advance")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
