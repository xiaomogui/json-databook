
import os
import json
from config.config import jsonDataPath
from utils.CommonUtils import formatTime, formatByte

class DatabookMapper:
    def __init__(self):
        print("DatabookMapper")

    def list (self, wname, bName):
        filepath = os.path.join(jsonDataPath, wname, bName)

        bookshelfs = []
        files = os.listdir(filepath)
        for fi in files:
            fi_d = os.path.join(filepath,fi)
            if os.path.isdir(fi_d):
                bookshelfs.append(fi)

        return bookshelfs

    def add (self, wname, bName, name):
        filepath = os.path.join(jsonDataPath, wname, bName)

        fi_d = os.path.join(filepath, name + ".json")            
        if os.path.exists(fi_d):
            return u'数据本[%s]已存在'%name

        fd = open(fi_d, mode="w", encoding="utf-8")
        fd.close()

        return name

    def info (self, wname, bName, name):
        filepath = os.path.join(jsonDataPath, wname, bName)

        fi_d = os.path.join(filepath, name + ".json")            
        if os.path.exists(fi_d) == False:
            return u'数据本[%s]不存在'%name

        fd = open(fi_d, mode="r", encoding="utf-8")
        info = fd.read()
        fd.close()

        return json.loads(info) if len(info) else ""

    def delete (self, wname, bName, name):
        filepath = os.path.join(jsonDataPath, wname, bName)

        fi_d = os.path.join(filepath, name + ".json")            
        if os.path.exists(fi_d) == False:
            return u'数据本[%s]不存在'%name

        fd = open(fi_d, mode="r", encoding="utf-8")
        info = fd.read()
        fd.close()

        if (len(info)):
            return u'数据本[%s]里存在数据，不能删除'%name

        os.remove(fi_d)

        return name