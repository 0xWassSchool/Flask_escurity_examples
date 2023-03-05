import requests
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    args = request.args.get("stock")
    response = requests.get(url=args).status_code

    # Basta cambiare il sito della richiesta con un host interno e si possono mandare richieste http
    
    return str(response)

app.run()