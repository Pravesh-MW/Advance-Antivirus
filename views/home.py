from tkinter import Frame, Label, Button, PhotoImage, Canvas
from.sidebar import SideBar  # Import the SideBar class
from PIL import Image, ImageTk
import os

# Get the current file's directory
current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)
class HomeView(SideBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the label
        # self.label = Label(self.content_frame, text="this is home page", width=20, height=5)
        # self.label.place(x=100, y=200)

        # Initialize the arrow image
        self.arrow = f"{parent_directory}\\assets\\frame0\\ArrowButton.png"
        self.SRectangle = f"{parent_directory}\\assets\\frame0\\smallRectangle.png"
        self.LRectangle = f"{parent_directory}\\assets\\frame0\\largeRectangle.png"
        self.NITJ_Logo = f"{parent_directory}\\assets\\frame0\\NITJ.png"

        # Initialize the image labels
        self.image_label1 = self.create_image_label(self.SRectangle, 50, 250)
        self.image_label2 = self.create_image_label(self.SRectangle, 400, 250)
        self.image_label3 = self.create_image_label(self.SRectangle, 50, 400)
        self.image_label4 = self.create_image_label(self.SRectangle, 400, 400)
        self.image_label5 = self.create_image_label(self.LRectangle, 12, 20)
        self.image_label6 = self.create_image_label(self.NITJ_Logo, 22, 40)
        
        # Initialize the button image
        # self.button_image = self.create_image_label(self.arrow, 300, 330)

        # Initialize the buttons
        self.Button_1 = self.create_button(self.arrow, lambda: print("Button 1 clicked"), 300, 330)
        self.Button_2 = self.create_button(self.arrow, lambda: print("Button 2 clicked"), 650, 330)
        self.Button_3 = self.create_button(self.arrow, lambda: print("Button 3 clicked"), 300, 480)
        self.Button_4 = self.create_button(self.arrow, lambda: print("Button 4 clicked"), 650, 480)

        self.Text_1 = self.create_text_label("Real Time Protection",70, 270)
        self.Text_1 = self.create_text_label("Manual Scan",420, 270)
        self.Text_1 = self.create_text_label("Network Monitering", 70, 420)
        self.Text_1 = self.create_text_label("Advance Protection", 420, 420)
        
        
    def create_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.content_frame, image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        return label, photo
    
    def create_text_label(self, text, x, y):
        lable =  Label(self.content_frame, text=text, font=("Helvetica", 14), fg="black", bg="#D9D9D9")
        lable.place(x=x, y=y)
        return lable
    
    def create_image_label(self, image_path, x, y):
        label, photo = self.create_image(image_path)
        label.place(x=x, y=y)
        return label

    def create_button(self, image_path, command, x, y):
        label, photo = self.create_image(image_path)
        button = Button(
            self.content_frame,
            image=photo,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            bg="#D9D9D9",
            relief="flat"
        )
        button.place(x=x, y=y, width=56.0, height=56.0)
        return button