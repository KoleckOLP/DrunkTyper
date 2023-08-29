from flask import Flask, request, render_template, jsonify
from markupsafe import Markup
from time import time

app = Flask(__name__)

status = "True"
#text = "Cigarettes and tiny liquor bottles,\nJust what you'd expect inside her new Balenciaga.\nWild romance turned dreams into an empire.\nSelf-made success now she rolls with Rockefellers."
#text = "I am sitting\nIn the morning\nAt the diner\nOn the corner"
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque mollis volutpat condimentum. In posuere metus mi, volutpat sagittis quam interdum quis. Donec vulputate ornare nunc, et fringilla velit eleifend malesuada. Duis non lorem mattis, elementum dolor quis, tristique risus. Mauris tempor lacus massa, a dapibus lorem eleifend sit amet. Donec lacinia venenatis libero, vel dictum elit euismod nec. Aliquam tristique."

@app.route("/")
def index():
    logic()
    return render_template("index.html", text=Markup(text.replace("\n", "<br>")), status=status)

@app.route("/settings")
def settings():
    logic()
    return render_template("settings.html")

index_data = ""
settings_data = "nothing"

started = False
starttime = 0
endtime = 0
tooktime = 0
last_correct = 0

@app.route("/index_input", methods=["POST"])
def index_input():
    global index_data
    index_data = request.data.decode("utf-8")
    length, rettext, tooktime, settings_data = logic()
    return jsonify(status=status, number=length, text=Markup(rettext.replace("\n", "<br>")), took=tooktime, stopat=settings_data)

@app.route("/settings_input", methods=["POST"])
def settings_input():
    global settings_data
    settings_data = request.data.decode("utf-8")
    logic()
    #print("settings_input="+settings_data)
    return settings_data

def logic():
    global status
    global started
    global starttime
    global endtime
    global tooktime
    global last_correct

    global index_data
    global settings_data

    length = len(index_data)

    print("logic="+settings_data)

    if length == 1:
        started = True
        starttime = time()
    
    if length == len(text):
        if started:
            started = False
            endtime = time()
            tooktime = endtime - starttime

            wpm = (len(text.split()) / tooktime) * 60

            wpm5 = ((len(text) / 5) / tooktime ) * 60

            if tooktime < 60:
                tooktime = f"test took: {round(tooktime, 2)}s {round(wpm, 2)}rWPM {round(wpm5, 2)}aWPM"
            else:
                tooktime = f"test took: {int(tooktime/60)}min {round(tooktime%60, 2)}s {round(wpm, 2)}rWPM {round(wpm5, 2)}avgwWPM"
    else:
        tooktime = "finish a test to get a time"

    print(length, last_correct)

    if text[:length] == index_data:
        status = "True"
        rettext = f"<span id=\"correct\">{text[:length]}</span>{text[length:]}"
        last_correct = length
    else:
        status = "False"
        wrong_text = text[last_correct:length].replace(' ', '·')
        wrong_text = wrong_text.replace('\n', "↵\n")
        rettext = f"<span id=\"correct\">{text[:last_correct]}</span><span id=\"wrong\">{wrong_text}</span>{text[length:]}"

    return length, rettext, tooktime, settings_data

if __name__ == '__main__':
    app.run()
