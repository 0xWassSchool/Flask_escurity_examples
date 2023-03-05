import requests
from flask import Flask, request, abort


app = Flask(__name__)
white_list = ()


@app.route("/")
def index():
    args = request.args.get("stock")
    if not args in white_list:
        return abort(400)  # metodo semplice ma efficace

    return str(requests.get(url=args).status_code)


app.run()
