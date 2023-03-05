from flask import Flask, request, render_template_string, abort


app = Flask(__name__)

# http://127.0.0.1:5000/?comment={{app.__class__}} 
@app.route("/")
def index():
    args = request.args.get('comment')
    if eval(args.strip("{ }")):
        return abort(400)
    
    return render_template_string(f"<h1>{args}</h1>")


if __name__ == "__main__":
    app.run()
