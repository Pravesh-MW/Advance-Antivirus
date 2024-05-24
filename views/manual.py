from tkinter import Frame, Label, Button, PhotoImage
from .sidebar import SideBar  # Import the SideBar class
from .table import ScrollTable
from PIL import Image, ImageTk
import os


# Get the current file's directory
current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)
class ManualView(SideBar, ScrollTable):  # Inherit from SideBar
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = "every thing is fine  f{parent_directory}\\assets\\manual\\button_4.png self.button5 = f{parent_directory}\\assets\\manual\\button_5.png self.button6 = f{parent_directory}\\assets\\manual\\button_6.png self.image_1 = f{parent_directory}\\assets\\realTime\\image_1.png self.image_2 = f{parent_directory}\\assets\\realTime\\image_2.png self.image_3 = f{parent_directory}\\assets\\realTime\\image_3.png se"
        
        self.table = ScrollTable(self.content_frame)
        # self.update()
        
        # Initialize the arrow image
        self.button4 = f"{parent_directory}\\assets\\manual\\button_4.png"
        self.button5 = f"{parent_directory}\\assets\\manual\\button_5.png"
        self.button6 = f"{parent_directory}\\assets\\manual\\button_6.png"
        self.image_1 = f"{parent_directory}\\assets\\realTime\\image_1.png"
        self.image_2 = f"{parent_directory}\\assets\\realTime\\image_2.png"
        self.image_3 = f"{parent_directory}\\assets\\realTime\\image_3.png"
        self.image_4 = f"{parent_directory}\\assets\\realTime\\image_4.png"

        # Initialize the image labels
        self.image_label1 = self.create_image_label(self.image_1, x=28, y=114)
        self.image_label2 = self.create_image_label(self.image_2, x=5, y=10)
        self.image_label3 = self.create_image_label(self.image_3, x=300, y=20)
        # self.image_label4 = self.create_image_label(self.image_4, x=28, y=310)
        self.image_label3.config(bg='#D9D9D9')
        
        # Initialize the button image
        # self.button_image = self.create_image_label(self.arrow, 300, 330)

        # Initialize the buttons
        # self.Full_Button = self.create_button(self.button4, lambda: print("Full Scan"), x=66, y=230, width=160, hight=30)
        # self.File_Button = self.create_button(self.button5, lambda: print("File Scan"), x=315, y=230, width=150, hight=30)
        self.File_Button = self.create_button(self.button5, lambda: print("File Scan"), x=200, y=230, width=150, hight=30)
        # self.Folder_Button = self.create_button(self.button6, lambda: print("Folder Scan"), x=543, y=230, width=145, hight=30)
        self.Folder_Button = self.create_button(self.button6, lambda: print("Folder Scan"), x=430, y=230, width=145, hight=30)
        
        self.Heading = self.create_text_label("Manual Scan", x=48, y=124)
        self.Suspicious = self.create_text_label("Suspicious files", x=48, y=321)
        self.Text = self.create_text_label("Manual Scan Scan selected file or folder and find suspicious files.", x=48, y=172, color="#FFFFFF")
        self.Text.config(wraplength=600)
        self.Text.config(justify="left")
        
        # self.OUTPUT = self.create_text_label(self.result, x=56, y=355)
        # self.OUTPUT.config(width=60, height=9)
        # self.OUTPUT.config(background="white")
        # self.OUTPUT.config(justify="left")
        # self.OUTPUT.config(wraplength=800)
        # self.OUTPUT.config()
        # self.OUTPUT.config()
        
        
        
        
    def create_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.content_frame, image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        return label, photo
    
    def create_text_label(self, text, x, y, color="black"):
        lable =  Label(self.content_frame, text=text, font=("Helvetica", 14), fg=color, bg="#D9D9D9")
        lable.place(x=x, y=y)
        return lable
    
    def create_image_label(self, image_path, x, y):
        label, photo = self.create_image(image_path)
        label.place(x=x, y=y)
        return label

    def create_button(self, image_path, command, x, y,width=56, hight=56):
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
        button.place(x=x, y=y, width=width, height=hight)
        return button