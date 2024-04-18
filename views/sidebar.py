from tkinter import Tk, Frame, Label, Button, PhotoImage, Frame
import os

# Get the current file's directory
current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)



class SideBar(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Create left sidebar frame
        self.sidebar_frame = Frame(self, bg="#333333", width=150, height=600)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # Create main content frame
        self.content_frame = Frame(self, bg="#DDDDDD", width=750, height=600)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        
        
        # Load icons (replace with your actual image paths)
        self.icon_paths = {
            "home.png": f"{parent_directory}\\button_1.png",
            "shield.png": f"{parent_directory}\\button_2.png",
            "advance.png": f"{parent_directory}\\button_3.png",
        }
        self.icons = {}
        self.load_icons()

        # Create icon buttons with placeholders for button clicks
        self.create_icon_buttons()

    def load_icons(self):
        for icon_name, path in self.icon_paths.items():
            # print(path)
            self.icons[icon_name] = PhotoImage(file=path)

    def create_icon_buttons(self):
        button_y = 50  # Starting position for buttons

        # Home button
        home_button = Button(
            self.sidebar_frame,
            image=self.icons["home.png"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Home Button Clicked"),  # Replace with actual function
            bg="#333333",
            relief="flat"
        )
        home_button.place(x=47, y=button_y, width=56, height=51)
        button_y += 80  # Adjust spacing between buttons

        # Shield button
        shield_button = Button(
            self.sidebar_frame,
            image=self.icons["shield.png"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Shield Button Clicked"),  # Replace with actual function
            bg="#333333",
            relief="flat"
        )
        shield_button.place(x=47, y=button_y, width=56, height=56)
        button_y += 80  # Adjust spacing between buttons

        # Advance button
        advance_button = Button(
            self.sidebar_frame,
            image=self.icons["advance.png"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Advance Button Clicked"),  # Replace with actual function
            bg="#333333",
            relief="flat"
        )
        advance_button.place(x=47, y=button_y, width=56, height=50)


if __name__ == "__main__":
    text_app = SideBar()
    text_app.mainloop()