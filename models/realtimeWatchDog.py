import watchdog.events
import watchdog.observers
import time
from os import path
class FileEventHandler(watchdog.events.FileSystemEventHandler):
    # def on_created(self, event):
    #     print(f"New file created: {event.src_path}")
    def __init__(self) -> None:
        super().__init__()
        self.OUTPUT = []
        
    def on_created(self, event):
        file_path = event.src_path
        file = path.basename(file_path).split('/')[-1]
        # print(f"New file created: {path}")
        self.OUTPUT.append({operation: "created",filename: file, dir: file_path})
        # print(self.OUTPUT)
        
        
    def on_modified(self, event):
        file_path = event.src_path
        file = path.basename(file_path).split('/')[-1]
        # print(f"New file created: {path}")
        # print(f"File modified: {event.src_path}")
        # self.OUTPUT.append(("modified",f"filename: {file}", f"dir: {file_path}"))
        # print(self.OUTPUT)
    
if __name__ == "__main__":
    # Choose the directory you want to monitor (avoid system-critical directories)
    watch_dir = "C:\\Users\\Asus\\Downloads"
    event_handler = FileEventHandler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, watch_dir, recursive=True)  # Monitor subdirectories
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    for operation, filename, dir  in event_handler.OUTPUT:
        print(f"{operation} is preformed on {filename} in directory {dir}")
