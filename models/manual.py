from tkinter.filedialog import askdirectory
import os
class Manual:
    def __init__(self):
        self.files = []
        self.paths = []
        self.malware = []
        self.path = "."

    def Path(self):
        self.path = askdirectory()

    def start_scan(self):
        self.Path()
        self.paths.clear()
        self.files.clear()
        self.malware.clear()
        self._scan_dir(self.path)
        print(self.files)
        return self.paths, self.files, self.malware
    
    def _scan_dir(self, path):
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    self.paths.append(os.path.join(dirpath, filename))
                    self.files.append(filename)
                    self.malware.append("error")
                for dirname in dirnames:
                    self._scan_dir(os.path.join(dirpath, dirname))
            return self.paths, self.files, self.malware
        except Exception as e:
            print(e)


# if __name__ == "__main__":
#     directory = Manual()
#     # print(directory.path)
#     directory.Directory()
#     print(directory.path)
#     directory.start_scan()