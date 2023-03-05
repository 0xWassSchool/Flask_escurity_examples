from flask import Flask, request, render_template, abort


app = Flask(__name__)

black_list = ("py")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    print(request.files["file"].filename.split(".")[1])
    if request.files["file"].filename.split(".")[1] in black_list:
        return abort(400)
    return "x"


if __name__ == "__main__":
    app.run()
