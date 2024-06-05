from models.main import Model
from views.main import View


class RealTimeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["realTime"]
        self.on = "C:\\Users\\Asus\\Documents\\Major_Project\\Advance-Antivirus\\controllers\\__pycache__\\Turn_on.png"
        self.off = "C:\\Users\\Asus\\Documents\\Major_Project\\Advance-Antivirus\\views\\assets\\realtime\\button_4.png"
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_button.config(command=self.home)
        self.frame.shield_button.config(command=self.shield)
        self.frame.advance_button.config(command=self.advance)
        self.frame.On_Of_button.config(command=self.Start_Scan)
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

    def Start_Scan(self):
         print(f"{self.model.realtime.watch_dir} being monitored")
         self.frame.On_Of_button.config(command=self.Stop_Scan)
         try :
            self.model.realtime.run = True
            self.model.threading.add_task(self.model.worker.start())
            self.model.threading.run_tasks()
         except Exception as e:
            print("error: ", str(e))
    #      self.model.worker.start()
    #  #     index = self.view.frames["runtime"].table.index
     #     try:
     #      #   self.view.frames["runtime"].table.clear_data()
     #        for i in range(len(paths)):
     #            print(i+index)
     #            self.view.frames["runtime"].table.Table.insert(parent='', index='end', iid=i+index, text='', values=(i, malware[i], files[i], paths[i]))
     #     except Exception as e:
     #        print("errror: ", str(e))
     #     self.view.frames["runtime"].table.index = index+len(paths)
    
    
    
    
    def Stop_Scan(self):
         print(f"{self.model.realtime.watch_dir} monitering end")
         self.model.realtime.run = False
         self.model.realtime.observer.stop()
         
         print(self.model.worker.is_alive())
         
         self.frame.On_Of_button.config(command=self.Start_Scan)
         
         
    def Remove_Malware(self):
         try:
            for i in range(len(self.paths)):
               if self.malware[i] == 'malware':
                    print(self.paths[i]," deleted")
            self.view.frames["manual"].table.clear_data()
         except Exception as e:
            print("errror: ", str(e))
