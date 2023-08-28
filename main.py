from flask import Flask, request, render_template, jsonify
from markupsafe import Markup
from time import time

app = Flask(__name__)

status = "True"
#text = "Cigarettes and tiny liquor bottles,\nJust what you'd expect inside her new Balenciaga.\nWild romance turned dreams into an empire.\nSelf-made success now she rolls with Rockefellers."
text = "I am sitting\nIn the morning\nAt the diner\nOn the corner"

@app.route("/")
def index():
    return render_template("index.html", text=Markup(text.replace("\n", "<br>")), status=status)

started = False
starttime = 0
endtime = 0
tooktime = 0

@app.route("/get_input", methods=["POST"])
def get_input():
    global text
    global status
    global started
    global starttime
    global endtime
    global tooktime
    
    data = request.data.decode("utf-8")
    length = len(data)

    if length == 1:
        started = True
        starttime = time()
    
    if length == len(text):
        if started:
            started = False
            endtime = time()
            tooktime = endtime - starttime
            if tooktime < 60:
                tooktime = f"test took: {int(tooktime)}s"
            else:
                tooktime = f"test took: {int(tooktime/60)}min {int(tooktime%60)}s"
    else:
        tooktime = "finish a test to get a time"

    if text[:length] == data:
        status = "True"
        rettext = f"<span id=\"correct\">{text[:length]}</span>{text[length:]}"
    else:
        status = "False"

    #print(data, length, status)
    return jsonify(status=status, number=length, text=Markup(rettext.replace("\n", "<br>")), took=tooktime)

if __name__ == '__main__':
    app.run()
