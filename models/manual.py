from tkinter.filedialog import askdirectory, askopenfilename
import os
from .Hash.signatureBased import MalwareDetector
from .ML.PE import PE
class Manual():
    def __init__(self):
        """
        Initialize the manual engine with an empty list of files and paths.
        """
        # super().__init__("md5")
        self.files = []
        self.paths = []
        self.malware = []
        self.path = "."
        self.Output = []
        self.engine = MalwareDetector()
        self.ml_model = PE()
        
    # def malware_scan_md5(self):
    #     return self.engine.malware_checker_md5(self.file)
    #     # return 

    def Path(self):
        self.path = askdirectory()
    
    def ML_scan(self, file_path):
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension == ".exe":
            if self.ml_model.predict(file_path) == 0 :
                return "malware"
        else:
            return "safe"
    def scan_file(self):
        self.file = askopenfilename()
        self.paths.clear()
        self.files.clear()
        self.malware.clear()
        self.paths.append(self.file)
        self.files.append(self.file.split("/")[-1])
        self.engine.path = self.file
        try:
            tag = self.engine.malware_checker_md5(self.engine.path)
            print(tag, "tag")
            if tag == "malware":
                self.malware.append("malware")
            elif tag == "safe":
                self.malware.append("safe")
        except:
            pass

        self.malware.append("error")
        return self.paths, self.files, self.malware
   
   
    def scan_full(self):
        # self.path = "C:\\Users\\Asus\\Documents\\Major Project\\Advance-Antivirus\\test"
        self.path = "C:\\Users\\Asus\\Pictures"
        
        self.paths.clear()
        self.files.clear()
        self.malware.clear()
        self._scan_dir(self.path)
        # print(self.files)
        return self.paths, self.files, self.malware
        
    def start_scan(self):
        self.Path()
        self.paths.clear()
        self.files.clear()
        self.malware.clear()
        self._scan_dir(self.path)
        # print(self.files)
        return self.paths, self.files, self.malware
    
    def _scan_dir(self, path):
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    self.paths.append(file_path)
                    self.files.append(filename)
                    
                    try:
                        tag = self.engine.malware_checker_md5(file_path)
                        print(tag)
                        if tag == "malware":
                            self.malware.append("malware")
                            continue
                        elif tag == "safe":
                            self.malware.append("safe")
                    except:
                        pass
                    try:
                        tag = self.engine.malware_checker_sha256(file_path)
                        print(tag)
                        if tag == "malware":
                            self.malware.append("malware")
                            continue
                        elif tag == "safe":
                            self.malware.append("safe")
                    except:
                        pass

                for dirname in dirnames:
                    self._scan_dir(os.path.join(dirpath, dirname))
            return self.paths, self.files, self.malware
        except Exception as e:
            print(e)
        print(self.virusHashCyPy, self.virusPath)


# if __name__ == "__main__":
#     directory = Manual()
#     # print(directory.path)
#     directory.Directory()
#     print(directory.path)
#     directory.start_scan()