from tkinter import Tk


class Root(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("900x600")
        self.configure(bg = "#FFFFFF")
        self.title("NITJ Shield")
        self.resizable(False, False)
        
# # Usage example
# if __name__ == "__main__":
#     app = Root()
#     app.mainloop()