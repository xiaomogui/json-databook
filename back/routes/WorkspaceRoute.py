#coding:utf-8
#user

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from services.WorkspaceService import WorkspaceService

workspaceRoute = Blueprint('workspaceRoute', __name__)
api = Api(workspaceRoute)

workspaceService = WorkspaceService()

class Workspaces(Resource):
    def get(self):
        return jsonify(workspaceService.list())

    def post(self):
        data = request.get_json()
        name = data["name"]
        return workspaceService.add(name)

class Workspace(Resource):
    def get(self,name):
        return workspaceService.info(name)

    def delete(self,name):
        return workspaceService.delete(name)

    def put(self, name):
        # 修改单条数据
        data = request.get_json()
        return 'put data %s: %s'%(name, data)

api.add_resource(Workspaces, '/workspaces/')
api.add_resource(Workspace, '/workspaces/<name>/')