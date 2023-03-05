import subprocess
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    args = request.args.get("stock")
    stock = subprocess.check_output(args, shell=True)

    return f"stock = {stock}"


if __name__ == "__main__":
    app.run()