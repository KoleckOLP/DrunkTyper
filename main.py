from flask import Flask, request, render_template, jsonify
from markupsafe import Markup
from time import time

app = Flask(__name__)

status = "True"
#text = "Cigarettes and tiny liquor bottles,\nJust what you'd expect inside her new Balenciaga.\nWild romance turned dreams into an empire.\nSelf-made success now she rolls with Rockefellers."
text = "I am sitting\nIn the morning\nAt the diner\nOn the corner"
#ext = "I am sitting in the morning at the diner on the corner"
#text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque mollis volutpat condimentum. In posuere metus mi, volutpat sagittis quam interdum quis. Donec vulputate ornare nunc, et fringilla velit eleifend malesuada. Duis non lorem mattis, elementum dolor quis, tristique risus. Mauris tempor lacus massa, a dapibus lorem eleifend sit amet. Donec lacinia venenatis libero, vel dictum elit euismod nec. Aliquam tristique."

#region index
@app.route("/")
def index():
    logic()
    return render_template("index.html", text=Markup(text.replace("\n", "<br>")), status=status)
#endregion

#region settings
@app.route("/settings")
def settings():
    logic()
    return render_template("settings.html")
#endregion

index_data = ""
settings_data = "nothing"

started = False
ended = False
starttime = 0
endtime = 0
tooktime = 0
last_correct_length = 0

#region index_input
@app.route("/index_input", methods=["POST"])
def index_input():
    global index_data
    index_data = request.data.decode("utf-8")
    length, rettext, tooktime, settings_data, rows = logic()
    return jsonify(status=status, number=length, text=Markup(rettext.replace("\n", "<br>")), took=tooktime, stopat=settings_data, rows=rows)
#endregion

#region settings_input
@app.route("/settings_input", methods=["POST"])
def settings_input():
    global settings_data
    settings_data = request.data.decode("utf-8")
    logic()
    return settings_data
#endregion

#region logic
def logic():
    global status
    global started
    global ended
    global starttime
    global endtime
    global tooktime
    global last_correct_length
    global last_correct

    global index_data
    global settings_data

    length = len(index_data)
    rows = len(text.split("\n"))+1

    #region Time and WPM caltulation
    if length == 1:
        started = True
        starttime = time()

    if length == len(text)-1:
        ended = True
    
    if length == len(text):
        if status == "True" and started == False and ended == False:
            tooktime = "no pasting cheater"
        elif started and ended: # prevents pasting the text
            started = False
            ended = False
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
    #endregion

    #region text coloring
    if text[:length] == index_data:
        status = "True"
        rettext = f"<span id=\"correct\">{text[:length]}</span>{text[length:]}"
        last_correct_length = length
    else:
        status = "False"
        wrong_text = text[last_correct_length:length].replace(' ', '·')
        wrong_text = wrong_text.replace('\n', "↵\n")
        rettext = f"<span id=\"correct\">{text[:last_correct_length]}</span><span id=\"wrong\">{wrong_text}</span>{text[length:]}"
    #endregion

    return length, rettext, tooktime, settings_data, rows
#endregion

if __name__ == '__main__':
    app.run()
