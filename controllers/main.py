from models.main import Model
from views.main import View


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
    
    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        if self.model.realtime == "x":
            # self.view.switch("gui")
            # self.view.switch("test")
            self.view.switch("home")
            # self.view.switch("manual")
            # self.view.switch("realTime")
            # self.view.switch("advance")
            # self.view.switch("networkMonitoring")
        else:
            # self.view.switch("realtime")
            print("real time value is not x")

        self.view.start_mainloop()
