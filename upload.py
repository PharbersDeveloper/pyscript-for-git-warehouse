# coding=utf-8
import os
import pandas as pd
import sys
import shutil

from gitShell import gitShell
from checkTitle import checkTitle

class upload():
    # 遍历文件
    def checkFiles(self, path):
        print "start check file"
        self.checkPath(path)
        lst = []
        if os.path.isdir(path):
            files = os.listdir(path)
            for i in files:
                file = self.get_xmlsFile(path + "\\" + i)
                lst.append(file)
        else:
            file = self.get_xmlsFile(path)
            lst.append(file)
        return lst

    def get_xmlsFile(self, file):
        lst = file.split(".")
        extension = lst[len(lst) - 1]
        if extension == "xlsx":
            checkTitle().check_pfizerFiles(file)
            return file
        elif extension == "xls":
            checkTitle().check_pfizerFiles(file)
            return file
        else:
            print(file + " is not a excel file")
            os.system("pause")
            sys.exit()

    def copyFiles(self, file_path, local_repository, repository, branch):
        lst = file_path.split("\\")
        lenth = len(lst)
        file = lst[lenth - 1].split(".")
        filename = file[0]
        postfix = file[1]
        local_filePath = local_repository + "\\" + branch + "\\" + filename + "." + postfix
        self.check_localpath(local_repository, repository, branch)
        shutil.copyfile(file_path, local_filePath)

    def checkPath(self, path):
        if path == r"C:\Windows\cache\cachedata":
            if os.path.exists(path):
                pass
            else:
                os.makedirs(path)
        else:
            if os.path.exists(path):
                pass
            else:
                print("path" + path + "not exits")
                os.system('pause')
                sys.exit()

    def check_localpath(self, local_repository, repository, branch):
        if os.path.exists(local_repository + "\\" + branch):
            gitShell().pullFiles(local_repository + "\\" + branch)
        else:
            if os.path.exists(local_repository):
                pass
            else:
                os.makedirs(local_repository)
            gitShell().cloneFiles(local_repository, repository, branch)

    def upload(self, path, branch, repository, discription):
        file_lst = self.checkFiles(path)
        local_repository = "C:\\Windows\\cache\\cachedata\\" + repository
        for i in file_lst:
            self.copyFiles(i, local_repository, repository, branch)
        gitShell().pushFiles(local_repository, repository, discription, branch)
