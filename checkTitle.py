# coding=utf-8
import pandas as pd
import os
import sys


class checkTitle():
    def check_pfizerFiles(self, file_path):
        fileMark = self.getMark(file_path)
        lst = self.get_title(fileMark)
        data = pd.read_excel(file_path)  # 读入数据
        titleIndex = data.columns
        titlelst = []
        for i in titleIndex:
            titlelst.append(i)
        # lst = ["YM", "MKT", "ID", "CATEGORY", "IF_PANEL_ALL", "HOSPITAL_COUNT", "PRODUCT_COUNT", "f_sales(offline)",
        #        "f_units(offline)"]
        # lst = ["HOSP_ID", "PHA_HOSP_NAME", "PHA_HOSP_ID", "MARKET", "IF_PANEL_ALL"]
        flag = cmp(titlelst, lst)
        if flag == 0:
            pass
        else:
            print("file " + file_path + " error")
            os.system("pause")
            sys.exit()

    def get_title(self, file_name):
        if file_name == "cpa" or file_name == "gycx":
            lst = ["CITY", "YEAR", "MONTH", "HOSP_ID", "MOLE_NAME", "PRODUCT_NAME", "PACK_DES", "PACK_NUMBER", "VALUE",
                   "STANDARD_UNIT", "DOSAGE", "DELIVERY_WAY", "CORP_NAME"]
            return lst

    def getMark(self, file_path):
        pathlst = file_path.split("\\")
        file_name = pathlst[len(pathlst) - 1]
        fileMark = file_name.split("_")[2]
        if fileMark == "CPA":
            return "cpa"
        elif fileMark == "Gycx":
            return "gycx"
        else:
            print "not cpa or gycx"
            os.system("pause")
            sys.exit()
