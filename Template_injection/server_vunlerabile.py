from flask import Flask, request, render_template_string


app = Flask(__name__)

# http://127.0.0.1:5000/?comment={{app.__class__}} 
@app.route("/")
def index():
    return render_template_string(f"<h1>{request.args.get('comment')}</h1>")


if __name__ == "__main__":
    app.run()
