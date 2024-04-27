from models.main import Model
from views.main import View


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_button.config(command=self.home)
        self.frame.shield_button.config(command=self.shield)
        self.frame.advance_button.config(command=self.advance)
        self.frame.Button_1.config(command=self.realTime)
        self.frame.Button_2.config(command=self.manual)
        self.frame.Button_3.config(command=self.networkMonitoring)
        self.frame.Button_4.config(command=self.advance)
        



    def home(self) -> None:
         self.view.switch("home")
         print("cleacked on home")

    def shield(self) -> None:
         self.view.switch("realTime")
         print("cleacked on shield")

    def advance(self) -> None:
         self.view.switch("advance")
         print("cleacked on advance")

    def realTime(self) -> None:
         self.view.switch("realTime")
         print("cleacked on realTime")

    def manual(self) -> None:
         self.view.switch("manual")
         print("cleacked on manual")

    def networkMonitoring(self) -> None:
         self.view.switch("networkMonitoring")
         print("cleacked on networkMonitoring")


    # def update_view(self) -> None:
    #     current_user = self.model.auth.current_user
    #     if current_user:
    #         username = current_user["username"]
    #         self.frame.greeting.config(text=f"Welcome, {username}!")
    #     else:
    #         self.frame.greeting.config(text=f"")
