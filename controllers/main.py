from models.main import Model
from views.main import View

from .sidebar import SideBarController
from .manual import ManualController
from .realTime import RealTimeController
from .advance import AdvanceController
from .networkMonitoring import NetworkMonitoringController
from .home import HomeController

class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.home = HomeController(model, view)
        self.sidebar = SideBarController(model, view)
        self.manual = ManualController(model, view)
        self.realTime = RealTimeController(model, view)
        self.advance = AdvanceController(model, view)
        self.networkMonitoring = NetworkMonitoringController(model, view)
    
    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        if self.model.test == "x":
            # self.view.switch("gui")
            # self.view.switch("test")
            self.view.switch("home")
            # self.view.switch("sidebar")
            # self.view.switch("manual")
            # self.view.switch("realTime")
            # self.view.switch("advance")
            # self.view.switch("networkMonitoring")
        else:
            # self.view.switch("realtime")
            print("real time value is not x")

        self.view.start_mainloop()
