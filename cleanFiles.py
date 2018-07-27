# coding = utf-8
import shutil
import os

class cleanFiles():
    def clean(self):
        path = "C:\\Windows\\cache\\cachedata\\"
        if os.path.exists(path):
            os.system("rd /s /q " + path)
            print("clean finished")
        else:
            print("nothing")
