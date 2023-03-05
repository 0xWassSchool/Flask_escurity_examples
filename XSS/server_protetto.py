from flask import Flask, request, abort

app = Flask(__name__)

# -> Implementazione molto basica di una prevenzione di attacco XSS una maggiore protezione X-XSS-Protection: 1; mode=block
# more info https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection


@app.route("/content")
def index():
    args = request.args.get("co")

    if "script" in args:
        print(f"found xss: {args}")
        return abort(400)

    return f"<p>{args}</p>"


if __name__ == "__main__":
    app.run()
