#coding:utf-8
#user

from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from services.BookshelfService import BookshelfService

bookshelfRoute = Blueprint('bookshelfRoute', __name__)
api = Api(bookshelfRoute)

bookshelfService = BookshelfService()

class Bookshelfs(Resource):
    def get(self, wname):
        return jsonify(bookshelfService.list(wname))

    def post(self, wname):
        data = request.get_json()
        name = data["name"]
        return bookshelfService.add(wname, name)

class Bookshelf(Resource):
    def get(self,wname, name):
        return bookshelfService.info(wname, name)

    def delete(self,wname, name):
        return bookshelfService.delete(wname, name)

    def put(self,wname, name):
        # 修改单条数据
        data = request.get_json()
        return 'put data %s: %s'%(name, data)

api.add_resource(Bookshelfs, '/workspaces/<wname>/bookshelfs/')
api.add_resource(Bookshelf, '/workspaces/<wname>/bookshelfs/<name>/')