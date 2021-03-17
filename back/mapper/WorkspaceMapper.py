
import os
from config.config import jsonDataPath
from utils.CommonUtils import formatTime, formatByte

class WorkspaceMapper:
    def __init__(self):
        print("WorkspaceMapper")

    def list (self):
        filepath = jsonDataPath

        workspaces = []
        files = os.listdir(filepath)
        for fi in files:
            fi_d = os.path.join(filepath,fi)
            if os.path.isdir(fi_d):
                workspaces.append(fi)

        return workspaces

    def add (self, name):
        filepath = jsonDataPath

        fi_d = os.path.join(filepath, name)            
        if os.path.exists(fi_d):
            return u'数据空间[%s]已存在'%name

        os.mkdir(fi_d)

        return name

    def info (self, name):
        filepath = jsonDataPath

        fi_d = os.path.join(filepath, name)            
        if os.path.exists(fi_d) == False:
            return u'数据空间[%s]不存在'%name

        info = {}
        folderinfo = os.stat(fi_d)
        info["size"] = formatByte(folderinfo.st_size)
        info["createtime"] = formatTime(folderinfo.st_atime)
        info["updatetime"] = formatTime(folderinfo.st_mtime)
        info["statustime"] = formatTime(folderinfo.st_ctime)
        return info

    def delete (self, name):
        filepath = jsonDataPath

        fi_d = os.path.join(filepath, name)            
        if os.path.exists(fi_d) == False:
            return u'数据空间[%s]不存在'%name

        files = os.listdir(fi_d)

        if (len(files)):
            return u'数据空间[%s]里存在数据，不能删除'%name

        os.rmdir(fi_d)

        return name