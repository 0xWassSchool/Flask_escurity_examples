from flask import Flask, request


app = Flask(__name__)


@app.route("/content")
def index():
    args = request.args.get("co")

    return f"<p>{args}</p>"


if __name__ == "__main__":
    app.run()
