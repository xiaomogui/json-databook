
from mapper.BookshelfMapper import BookshelfMapper

bookshelfMapper = BookshelfMapper()

class BookshelfService:
    def __init__(self):
        print("BookshelfService")

    def list (self, wname):
        return bookshelfMapper.list(wname)

    def add (self, wname, name):
        return bookshelfMapper.add(wname, name)

    def info (self, wname, name):
        return bookshelfMapper.info(wname, name)

    def delete (self, wname, name):
        return bookshelfMapper.delete(wname, name)