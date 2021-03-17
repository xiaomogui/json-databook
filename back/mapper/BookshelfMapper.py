
import os
from config.config import jsonDataPath
from utils.CommonUtils import formatTime, formatByte

class BookshelfMapper:
    def __init__(self):
        print("BookshelfMapper")

    def list (self, wname):
        filepath = os.path.join(jsonDataPath, wname)

        bookshelfs = []
        files = os.listdir(filepath)
        for fi in files:
            fi_d = os.path.join(filepath,fi)
            if os.path.isdir(fi_d):
                bookshelfs.append(fi)

        return bookshelfs

    def add (self, wname, name):
        filepath = os.path.join(jsonDataPath, wname)

        fi_d = os.path.join(filepath, name)            
        if os.path.exists(fi_d):
            return u'书架[%s]已存在'%name

        os.mkdir(fi_d)

        return name

    def info (self, wname, name):
        filepath = os.path.join(jsonDataPath, wname)

        fi_d = os.path.join(filepath, name)            
        if os.path.exists(fi_d) == False:
            return u'书架[%s]不存在'%name

        info = {}
        folderinfo = os.stat(fi_d)
        info["size"] = formatByte(folderinfo.st_size)
        info["createtime"] = formatTime(folderinfo.st_atime)
        info["updatetime"] = formatTime(folderinfo.st_mtime)
        info["statustime"] = formatTime(folderinfo.st_ctime)
        return info

    def delete (self, wname, name):
        filepath = os.path.join(jsonDataPath, wname)

        fi_d = os.path.join(filepath, name)            
        if os.path.exists(fi_d) == False:
            return u'书架[%s]不存在'%name

        files = os.listdir(fi_d)

        if (len(files)):
            return u'书架[%s]里存在数据，不能删除'%name

        os.rmdir(fi_d)

        return name