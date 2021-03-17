from flask import Flask, request
from flask_cors import CORS
from routes.WorkspaceRoute import workspaceRoute
from routes.BookshelfRoute import bookshelfRoute
from routes.DatabookRoute import databookRoute

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
CORS(app, resources=r'/*')

@app.route('/')
def index():
    path = request.args.get("path")
    print(path)
    return "it's a directory"


@app.route('/get-chess')
def getChess():
    path = request.args.get("path")

    return "getChess"

@app.route('/img/upload', methods=['POST'])
def send_img():
    f = request.files['file']
    imgData = f.read()

    return imgData

app.register_blueprint(workspaceRoute)
app.register_blueprint(bookshelfRoute)
app.register_blueprint(databookRoute)

if __name__ == '__main__':
    app.run(host="0.0.0.0")