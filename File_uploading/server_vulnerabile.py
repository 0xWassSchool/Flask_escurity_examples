from flask import Flask, request, render_template, abort


app = Flask(__name__)

black_list = "py"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_files():
    print(request.files["file"])
    return "file upaloded"


if __name__ == "__main__":
    app.run()
