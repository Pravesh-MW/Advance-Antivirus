from models.main import Model
from views.main import View


class NetworkMonitoringController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["networkMonitoring"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_button.config(command=self.home)
        self.frame.shield_button.config(command=self.shield)
        self.frame.advance_button.config(command=self.advance)
        self.frame.Button_search.config(command=self.search)



    def home(self) -> None:
         self.view.switch("home")
         print("cleacked on home")

    def shield(self) -> None:
         self.view.switch("realTime")
         print("cleacked on shield")

    def advance(self) -> None:
         self.view.switch("advance")
         print("cleacked on advance")

    def search(self) -> None:
         url = self.frame.entry.get()
         if url == "":
          self.frame.output.config(text="")
         tag = self.model.network.predict(url)
         self.frame.output.config(text=tag)
     
