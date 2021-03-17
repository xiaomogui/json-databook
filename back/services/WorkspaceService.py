
from mapper.WorkspaceMapper import WorkspaceMapper

workspaceMapper = WorkspaceMapper()

class WorkspaceService:
    def __init__(self):
        print("WorkspaceService")

    def list (self):
        return workspaceMapper.list()

    def add (self, name):
        return workspaceMapper.add(name)

    def info (self, name):
        return workspaceMapper.info(name)

    def delete (self, name):
        return workspaceMapper.delete(name)