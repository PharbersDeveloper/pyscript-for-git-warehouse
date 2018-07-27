# coding=utf-8
import json
import os
import sys
from upload import upload


class usersFilter():
    def readJson(self, path):
        with open(path, "r") as fr:
            data = fr.read()
            lst_tmp = data.split("},")
            lst = []
            for i in lst_tmp:
                if lst_tmp.index(i) < len(lst_tmp) - 1:
                    lst.append(json.loads(i + "}"))
                else:
                    lst.append(json.loads(i))
            return lst

    def check_user(self, lst, user):
        for i in lst:
            if i["name"] == user:
                return i["companies"]
        return []

    def check_barnch(self, lst, branch):
        if branch in lst:
            pass
        else:
            print("this user have no power")
            os.system('pause')
            sys.exit()

    def usersFilter(self, user, branch, local_repository):
        upload().check_localpath(local_repository, "users", "master")
        path = local_repository + "\\" + "master" + "\\" + "users.json"
        lst = self.readJson(path)
        companies = self.check_user(lst, user)
        if companies:
            self.check_barnch(companies, branch)
        else:
            print "no such user"
            os.system('pause')
            sys.exit()
