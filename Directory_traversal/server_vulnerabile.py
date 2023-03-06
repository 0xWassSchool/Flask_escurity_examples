import os
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    args = request.args.get('file')
    return open(os.getcwd() + "\\" + args, 'r').read()


if __name__ == "__main__":
    app.run()
