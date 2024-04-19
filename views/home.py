from tkinter import Frame, Label, Button, PhotoImage
from .sidebar import SideBar  # Import the SideBar class

class HomeView(SideBar):  # Inherit from SideBar
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = Label(self.content_frame, text="this is home page", width=20, height=5)
        # self.label.grid(row=0, column=0, sticky="nsew", justify="center")
        self.label.place(x=100, y=200)
        # self.label.pack()