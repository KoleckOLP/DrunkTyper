from flask import Flask, escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return("<p>Hello, World!</p><br>"+
           "<input></input>")

@app.route("/<name>")
def hello(name):
    return(f"Hello {escape(name)}!")