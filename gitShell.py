# coding=utf-8
import os


class gitShell():
    def pushFiles(self, path, repository, discription, branch):
        os.system("cd " + path + "\\" + branch + " && git add -A")
        os.system("cd " + path + "\\" + branch + " && git commit -m \"" + discription + "\"")
        os.system("cd " + path + "\\" + branch + " && git push git@192.168.100.137:/mnt/config/pha_repositories/" + repository + ".git")
        os.system("attrib +h +r +s C:\\Windows\\cache")

    def pullFiles(self, path):
        os.system("cd " + path + " && git pull")
        os.system("attrib +h +r +s C:\\Windows\\cache")

    def cloneFiles(self, path, repository, branch):
        os.system(
            "cd " + path + " && git clone -b " + branch + " git@192.168.100.137:/mnt/config/pha_repositories/" + repository + ".git " + branch)
        os.system("attrib +h +r +s C:\\Windows\\cache")
