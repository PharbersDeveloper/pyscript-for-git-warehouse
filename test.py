# coding=utf-8
import os
import chardet
import datetime
import json
import shutil
import xlrd
import pandas as pd
import codecs
import struct
from downloadFile import downloadFile
from usersFilter import usersFilter
import sys

path = "C:\\Users\\Administrator.PC-20180315FNLD\\Desktop\\pfizerdata\\Pfizer_201804_Gycx_20180716.xlsx"
# print datetime.datetime.now()
# file_path_utf8 = path2.decode('utf-8')
# workbooks = xlrd.open_workbook(file_path_utf8)
# sheet1 = workbooks.sheet_by_index(0)
# print datetime.datetime.now()
# head = sheet1.row_values(0)
# print(head)
# print datetime.datetime.now()
# print(1 == 1)
# file_path = r'/home/cui/Downloads/Astellas_201804_Offline_MaxResult_20180709.xlsx'
# print(os.path.isfile(file_path))
# file_path_utf8 = file_path.decode('utf-8')
# workbooks = xlrd.open_workbook(file_path_utf8)
# sheet1 = workbooks.sheet_by_index(0)
# head = sheet1.row_values(0)
# print(head)
# lst = [u'YM', u'MKT', u'ID', u'CATEGORY', u'IF_PANEL_ALL', u'HOSPITAL_COUNT', u'PRODUCT_COUNT', u'f_sales(offline)', u'f_units(offline)']
# flag = cmp(head, lst)
# print(flag)


# path = os.getcwd()
# files = os.listdir(path + "/data")
# print(files)
# os.system("cd /home/cui/妗岄潰/gitdata;git clone -b cui git@192.168.100.137:/mnt/config/data.git")
# os.system("pwd")
# os.system("git clone git@192.168.100.137:/mnt/config/data.git")

# path = r'E:\file_search\data\Astellas_201804_Offline_MaxResult_20180709.xlsx'
# path1 = r'E:\file_search\aaa'
# data1 = pd.read_excel(path)  # 璇诲叆鏁版嵁
# print("*****")
# print(os.popen('dir').read())
# data2 = data1.columns
# print data2
# for i in data2:
#     print i

# f = open(path, encoding='utf-8')
# f = open(path, 'rb').readline()
# f1 = struct.pack('c', f)
# print f1

#     fencoding = chardet.detect(f.read())
#     print fencoding
# f = codecs.open(path, 'r', 'utf-8')
# line = f.readline()

print datetime.datetime.now()
f = codecs.open(path, 'r')
content = f.read().decode("gb2312")
for i in content:
    line = f.readline()
    print line
f.close()
print datetime.datetime.now()


# with codecs.open(path, 'rb', 'ANSI') as f:
#     first_line = f.readline().rstrip()
#     print first_line
# path2 = "C:\\Users\\Administrator.PC-20180315FNLD\\Desktop\\pfizerdata\\Pfizer_201804_Gycx_20180716.xlsx"
# print datetime.datetime.now()
# data = pd.read_excel(path, header=0, nrows=0)
# print data
# data = pd.read_excel(path2)  # 读入数据
# titleIndex = data.columns
# print titleIndex
# print datetime.datetime.now()

# 异常值处理测试
# lst = ["aaa", "bbb", "ccc"]
# try:
#     lst.index("ddd")
# except ValueError, e:
#     print("aaa")


# lst = path.split("\\")
# len = len(lst)
# file = lst[len-1].split(".")
# filename = file[0]
# postfix = file[1]
# shutil.copyfile(path, path1 + "\\" + filename + "." + postfix)
# os.system('pause')

# downloadFile().downloadFile("E:\\pharbersdata", "pha_repository1804", "pfizer", "Pfizer_2018_IF_panel_all_INF_20180718.xlsx")
# lst = ["aaa", "bbb", "ccc"]
# if "aaa" in lst:
#     print True
# else:
#     print False


# with open("C:\\Windows\\cache\\users\\users.json", "r") as fr:
#     data = fr.read()
#     lst = data.split("},")
#     tmp = []
#     for i in lst:
#         if lst.index(i) < len(lst)-1:
#             tmp.append(json.loads(i + "}"))
#         else:
#             tmp.append(json.loads(i))
#     print tmp
#     for i in tmp:
#         print i["name"]
#         print i["companies"][0]
#     # r = json.loads(fr)
#     # print r
#     fr.close()


# if []:
#     print 1
# else:
#     print 2

# from usersFilter import usersFilter
# usersFilter().usersFilter("cui", "master", "C:\\Windows\cache")

# pathx = "C:\\Users\\Administrator.PC-20180315FNLD\\Desktop\\pfizer\\Pfizer_2018_If_panel_all_INF_20180718.xlsx"
# lst = pathx.split("\\")
# file_name = lst[len(lst)-1]
# print file_name
# lst1 = file_name.split("_")
# print lst1[2]
