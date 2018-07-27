# coding=utf-8
import os
import pandas as pd
import sys
import shutil

from gitShell import gitShell  # 读文件的第一行并检查


def readFileHead(file_path):
    data = pd.read_excel(file_path)  # 读入数据
    titleIndex = data.columns
    titlelst = []
    for i in titleIndex:
        titlelst.append(i)
    # lst = ["YM", "MKT", "ID", "CATEGORY", "IF_PANEL_ALL", "HOSPITAL_COUNT", "PRODUCT_COUNT", "f_sales(offline)",
    #        "f_units(offline)"]
    print titlelst
    lst = ["HOSP_ID", "PHA_HOSP_NAME", "PHA_HOSP_ID", "MARKET", "IF_PANEL_ALL"]
    flag = cmp(titlelst, lst)
    if flag == 0:
        pass
    else:
        print("\033[1;31m file " + file_path + " error")
        os.system("pause")
        sys.exit()


# 遍历文件
def checkFiles(path):
    print "start check file"
    checkPath(path)
    lst = []
    if os.path.isdir(path):
        files = os.listdir(path)
        for i in files:
            file = get_xmlsFile(path + "\\" + i)
            lst.append(file)
    else:
        file = get_xmlsFile(path)
        lst.append(file)
    return lst


def get_xmlsFile(file):
    lst = file.split(".")
    extension = lst[len(lst)-1]
    if extension == "xlsx":
        readFileHead(file)
        return file
    elif extension == "xls":
        readFileHead(file)
        return file
    else:
        print(file + " is not a excel file")
        os.system("pause")
        sys.exit()


def copyFiles(file_path, local_repository, repository, branch):
    lst = file_path.split("\\")
    lenth = len(lst)
    file = lst[lenth - 1].split(".")
    filename = file[0]
    postfix = file[1]
    local_filePath = local_repository + "\\" + branch + "\\" + filename + "." + postfix
    check_localpath(local_repository, repository, branch)
    shutil.copyfile(file_path, local_filePath)


def checkPath(path):
    if path == r"C:\Windows\pharbersdata\data":
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


def check_localpath(local_repository, repository, branch):
    if os.path.exists(local_repository + "\\" + branch):
        gitShell().pullFiles(local_repository + "\\" + branch)
    else:
        if os.path.exists(local_repository):
            pass
        else:
            os.makedirs(local_repository)
        gitShell().cloneFiles(local_repository, repository, branch)


def update(path, branch, repository, discription):
    file_lst = checkFiles(path)
    local_repository = "C:\\Windows\\pharbersdata\\" + repository
    for i in file_lst:
        copyFiles(i, local_repository, repository, branch)
    gitShell().pushFiles(local_repository, repository, discription, branch)


if __name__ == '__main__':
    path = "C:\Users\Administrator.PC-20180315FNLD\Desktop\pfizer"
    branch = "pfizer"
    repository = "pharbersdata1804"
    discription = "commit"
    update(path, branch, repository, discription)
