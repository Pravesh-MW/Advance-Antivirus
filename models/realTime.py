import watchdog.events
import watchdog.observers
import time
from os import path
class RealTime(watchdog.events.FileSystemEventHandler):
    def __init__(self) -> None:
        # self.watch_dir = "C:\\Users\\Asus\\Documents\\Major Project\\Advance-Antivirus"
        self.watch_dir = "C:\\Users\\Asus\\Downloads"
        self.OUTPUT = []
        self.observer = watchdog.observers.Observer()
        # self.event_handler = FileEventHandler()
    
    def on_created(self, event):
        file_path = event.src_path
        file = path.basename(file_path).split('/')[-1]
        print(f"New file created: {path}")
        self.OUTPUT.append(("created",file, file_path))

    def on_modified(self, event):
        file_path = event.src_path
        file = path.basename(file_path).split('/')[-1]
        print(f"New file modified: {path}")
        self.OUTPUT.append(("modified",file, file_path))
        
        
    def on_deleted(self, event):
        file_path = event.src_path
        file = path.basename(file_path).split('/')[-1]
        print(f"New file deleted: {path}")
        self.OUTPUT.append(("deleted",file, file_path))

    def on_moved(self, event):
        file_path = event.src_path
        file = path.basename(file_path).split('/')[-1]
        print(f"New file moved: {path}")
        self.OUTPUT.append(("moved",file, file_path))
        
    def start_runTime(self):    
        self.observer.schedule(self, self.watch_dir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
    
    def stop_runtime(self):
        self.observer.stop()
        self.observer.join()
    
    
# if __name__ == "__main__":
#     real = RealTime()
#     real.start_runTime()
    