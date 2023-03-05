import subprocess
from flask import Flask, request, abort


app = Flask(__name__)
stock_types = []


@app.route("/")
def index():
    args = request.args.get("stock")
    stock = subprocess.check_output(args, shell=True)

    if stock not in stock_types:
        return abort(400)

    return f"stock = {stock}"


if __name__ == "__main__":
    app.run()
