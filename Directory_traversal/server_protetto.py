import os
from flask import Flask, request, abort


app = Flask(__name__)
black_list = []

@app.route("/")
def index():
    args = request.args.get('file')
    if black_list in [*args]:
        return abort(400)

    return open(os.getcwd() + "\\" + args, 'r').read()


if __name__ == "__main__":
    app.run()
