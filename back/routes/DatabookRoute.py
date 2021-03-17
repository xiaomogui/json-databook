#coding:utf-8
#user

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from services.DatabookService import DatabookService

databookRoute = Blueprint('databookRoute', __name__)
api = Api(databookRoute)

databookService = DatabookService()

class Databooks(Resource):
    def get(self, wname, bName):
        return jsonify(databookService.list(wname, bName))

    def post(self, wname, bName):
        data = request.get_json()
        name = data["name"]
        return databookService.add(wname, bName, name)

class Databook(Resource):
    def get(self,wname, bName, name):
        return databookService.info(wname, bName, name)

    def delete(self,wname, bName, name):
        return databookService.delete(wname, bName, name)

    def put(self,wname, bName, name):
        # 修改单条数据
        data = request.get_json()
        return 'put data %s: %s'%(name, data)

api.add_resource(Databooks, '/workspaces/<wname>/bookshelfs/<bName>/databooks/')
api.add_resource(Databook, '/workspaces/<wname>/bookshelfs/<bName>/databooks/<name>/')