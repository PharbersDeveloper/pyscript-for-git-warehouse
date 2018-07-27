# coding=utf-8

# 克隆仓库
import os

import shutil

import sys

from gitShell import gitShell
from upload import upload


class downloadFile():
    def checkPath(self, path):
        if os.path.isdir(path):
            pass
        else:
            print("path" + path + "is not a directory")

    def downloadFile(self, path, repository, branch, filename):
        repository_path = "C:\\Windows\\cache\\cachedata\\" + repository
        flag = os.path.exists(path)
        if flag:
            self.checkPath(path)
            upload().check_localpath(repository_path, repository, branch)
            self.copy_files(repository_path + "\\" + branch, path, filename)
        else:
            print("path " + path + " not exit")
            os.system('pause')
            sys.exit()

    def copy_files(self, repository_path, target_path, filename):
        shutil.copyfile(repository_path + "\\" + filename, target_path + "\\" + filename)
