from models.main import Model
from views.main import View


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model