from models.main import Model
from views.main import View


class ManualController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["manual"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_button.config(command=self.home)
        self.frame.shield_button.config(command=self.shield)
        self.frame.advance_button.config(command=self.advance)
        self.frame.Folder_Button.config(command=self.Folder_Scan)
        self.frame.File_Button.config(command=self.File_Scan)



    def home(self) -> None:
         self.view.switch("home")
         print("cleacked on home")

    def shield(self) -> None:
         self.view.switch("realTime")
         print("cleacked on shield")

    def advance(self) -> None:
         self.view.switch("advance")
         print("cleacked on advance")
         
         
    def Folder_Scan(self):
         paths, files, malware = self.model.manual.start_scan()
         index = self.view.frames["manual"].table.index
         print("folder scan complete")
         try:
            self.view.frames["manual"].table.clear_data()
            for i in range(len(paths)):
               #  print(i+index)
                self.view.frames["manual"].table.Table.insert(parent='', index='end', iid=i+index, text='', values=(i, malware[i], files[i], paths[i]))
         except Exception as e:
            print("errror: ", str(e))
         self.view.frames["manual"].table.index = index+len(paths)
         print(self.view.frames["manual"].table.index)
         print("folder scan complete1")
    
    
    
    def File_Scan(self):
         paths, files, malware = self.model.manual.scan_file()
         index = self.view.frames["manual"].table.index
         print("file scan complete")
         try:
            self.view.frames["manual"].table.clear_data()
            for i in range(len(paths)):
               #  print(i+index)
                self.view.frames["manual"].table.Table.insert(parent='', index='end', iid=i+index, text='', values=(i, malware[i], files[i], paths[i]))
         except Exception as e:
            print("errror: ", str(e))
         self.view.frames["manual"].table.index = index+len(paths)
         print(self.view.frames["manual"].table.index)
         print("file scan complete1")
         

    # def update_view(self) -> None:
    #     current_user = self.model.auth.current_user
    #     if current_user:
    #         username = current_user["username"]
    #         self.frame.greeting.config(text=f"Welcome, {username}!")
    #     else:
    #         self.frame.greeting.config(text=f"")
