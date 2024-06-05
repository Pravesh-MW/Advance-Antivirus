import hashlib, os


class MalwareDetector:
    def __init__(self):
        self.current_file_path = os.path.abspath(__file__)
        self.parent_directory = os.path.dirname(self.current_file_path)
        self.read_DB()
        self.path = self.parent_directory

    def read_DB(self):
        # with open(f"{self.parent_directory}\\virusHash.txt", "r") as malware_hashes_file:
        #     self.malware_hashes_MD5 = list(malware_hashes_file.read().split('\n'))
        # with open(f"{self.parent_directory}\\virusInfo.txt", "r") as virusInfo_file:
        #     self.virusInfo_MD5 = list(virusInfo_file.read().split('\n'))
        # with open(f"{self.parent_directory}\\virusHash.txt", "r") as malware_hashes_file:
        #     self.malware_hashes_SHA256 = list(malware_hashes_file.read().split('\n'))
        # with open(f"{self.parent_directory}\\virusInfo.txt", "r") as virusInfo_file:
        #     self.virusInfo_SHA256 = list(virusInfo_file.read().split('\n'))
        with open(
            f"{self.parent_directory}\\DataBase\\HashDataBase\\Md5\\md5HashOfVirus.unibit",
            "r",
        ) as i:
            self.malware_hashes_MD5 = i.readlines()
            i.close()
        with open(
            f"{self.parent_directory}\\DataBase\\HashDataBase\\Sha256\\virusHash.unibit",
            "r",
        ) as i:
            self.malware_hashes_SHA256 = i.readlines()
            i.close()
        
        self.malware_hashes_MD5.sort()
        self.malware_hashes_SHA256.sort()
        print(len(self.malware_hashes_MD5),"hiloo bhai")

    def md5_hash(self, filename):
        with open(filename, "rb") as f:
            bytes = f.read()
            md5hash = hashlib.md5(bytes).hexdigest()
        return md5hash

    def sha256_hash(self, filename):
        with open(filename, "rb") as f:
            bytes = f.read()
            md5hash = hashlib.sha256(bytes).hexdigest()
        return md5hash

    def malware_checker_md5(self, pathOfFile):
        hash_malware_check = self.md5_hash(pathOfFile)
        left, right = 0, len(self.malware_hashes_MD5) - 1
        count = 1
        try:
            while left <= right:
                mid = (left + right) // 2
                if self.malware_hashes_MD5[mid] == hash_malware_check:
                    print(self.malware_hashes_MD5[mid], " malware")
                    # index = self.malware_hashes_MD5.index(hash_malware_check)
                    # print("virus type: ", self.virusInfo_MD5[index])
                    return "malware"
                elif self.malware_hashes_MD5[mid] < hash_malware_check:
                    left = mid + 1
                else:
                    right = mid - 1
                count = count+1
            print("file MD5 hash: ", hash_malware_check)
            print("no of iteration: ", count)
            return "safe"
        except Exception as e:
            # print("virus type: not find")
            print("file MD5 hash: ", hash_malware_check)
            print(e)
            return "safe"
    # def malware_checker_md5(self, pathOfFile):
    #     hash_malware_check = self.md5_hash(pathOfFile)
    #     x = 0
    #     print(len(self.malware_hashes_MD5))
    #     print(self.malware_hashes_MD5[0])
    #     try:
    #         for check in self.malware_hashes_MD5:
    #             # print(check)
    #             if check == hash_malware_check:
    #                 print(check, " malware")
    #                 # index = self.malware_hashes_MD5.index(hash_malware_check)
    #                 # print("virus type: ", self.virusInfo_MD5[index])
    #                 return "malware"
    #             # break
    #     # try :
    #     # for i in len(self.malware_hashes_MD5):
    #     #     if self.malware_hashes_MD5[i] == hash_malware_check:
    #     #         # index = self.malware_hashes_MD5.index(hash_malware_check)
    #     #         # print("virus type: ", self.virusInfo_MD5[index])
    #     #         x=i
    #     #         print(x)
    #     #         return "malware"
    #     except Exception as e:
    #         # print("virus type: not find")
    #         print("file MD5 hash: ", hash_malware_check)
    #         print(e)
    #         return "safe"

    def malware_checker_sha256(self, pathOfFile):
        hash_malware_check = self.sha256_hash(pathOfFile)
        left, right = 0, len(self.malware_hashes_SHA256) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.malware_hashes_SHA256[mid] == hash_malware_check:
                print(self.malware_hashes_SHA256[mid], " malware")
                # index = self.malware_hashes_SHA256.index(hash_malware_check)
                # print("virus type: ", self.virusInfo_SHA256[index])
                return "malware"
            elif self.malware_hashes_SHA256[mid] < hash_malware_check:
                left = mid + 1
            else:
                right = mid - 1
        print("file SHA256 hash: ", hash_malware_check)
        return "safe"

    # def malware_checker_sha256(self, pathOfFile):
    #     hash_malware_check = self.sha256_hash(pathOfFile)
    #     for check in self.malware_hashes_SHA256:
    #         if check == hash_malware_check:
    #             # index = self.malware_hashes_SHA256.index(hash_malware_check)
    #             # print("virus type: ", self.virusInfo_SHA256[index])
    #             return "malware"

    #     # print("virus type: not find")
    #     print("file MD5 hash: ", hash_malware_check)
    #     return "safe"

    

# #### main (Output section) ##########
# detector = MalwareDetector()
# print("**************start***************\n\n")


# print("Code: ", detector.malware_checker_sha256(f"{detector.parent_directory}\\engine.py"))
# print("Hash of file: ", detector.md5_hash(f"{detector.parent_directory}\\engine.py"))


# print("\n\n**************end******************")

# # virusshare.com/hashes
# # hash database
