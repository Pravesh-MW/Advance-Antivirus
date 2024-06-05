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
        self.frame.Full_Button.config(command=self.Full_Scan)
        self.frame.Remove_malware.config(command=self.Remove_Malware)



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
         self.paths, self.files, self.malware = self.model.manual.start_scan()
         index = self.view.frames["manual"].table.index
         print("folder scan complete")
         try:
            self.view.frames["manual"].table.clear_data()
            for i in range(len(self.paths)):
               #  print(i+index)
                self.view.frames["manual"].table.Table.insert(parent='', index='end', iid=i+index, text='', values=(i, self.malware[i], self.files[i], self.paths[i]))
         except Exception as e:
            print("errror: ", str(e))
         self.view.frames["manual"].table.index = index+len(self.paths)
         print(self.view.frames["manual"].table.index)
         print("folder scan complete1")
    
    
    
    def File_Scan(self):
         self.paths, self.files, self.malware = self.model.manual.scan_file()
         index = self.view.frames["manual"].table.index
         print("file scan complete")
         try:
            self.view.frames["manual"].table.clear_data()
            for i in range(len(self.paths)):
               #  print(i+index)
                self.view.frames["manual"].table.Table.insert(parent='', index='end', iid=i+index, text='', values=(i, self.malware[i], self.files[i], self.paths[i]))
         except Exception as e:
            print("errror: ", str(e))
         self.view.frames["manual"].table.index = index+len(self.paths)
         print(self.view.frames["manual"].table.index)
         print("file scan complete1")
         
    def Full_Scan(self):
         self.paths, self.files, self.malware = self.model.manual.scan_full()
         index = self.view.frames["manual"].table.index
         print("file scan complete")
         try:
            self.view.frames["manual"].table.clear_data()
            for i in range(len(self.paths)):
               #  print(i+index)
                self.view.frames["manual"].table.Table.insert(parent='', index='end', iid=i+index, text='', values=(i, self.malware[i], self.files[i], self.paths[i]))
         except Exception as e:
            print("errror: ", str(e))
         self.view.frames["manual"].table.index = index+len(self.paths)
         print(self.view.frames["manual"].table.index)
         print("file scan complete1")
         

    def Remove_Malware(self):
         try:
            for i in range(len(self.paths)):
               if self.malware[i] == 'malware':
                    print(self.paths[i]," deleted")
            self.view.frames["manual"].table.clear_data()
         except Exception as e:
            print("errror: ", str(e))