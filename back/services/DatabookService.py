
from mapper.DatabookMapper import DatabookMapper

databookMapper = DatabookMapper()

class DatabookService:
    def __init__(self):
        print("DatabookService")

    def list (self, wname, bName):
        return databookMapper.list(wname, bName)

    def add (self, wname, bName, name):
        return databookMapper.add(wname, bName, name)

    def info (self, wname, bName, name):
        return databookMapper.info(wname, bName, name)

    def delete (self, wname, bName, name):
        return databookMapper.delete(wname, bName, name)