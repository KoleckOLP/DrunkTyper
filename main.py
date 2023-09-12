from flask import Flask, request, render_template, jsonify
from markupsafe import Markup
import random

app = Flask(
    __name__, static_url_path="", static_folder="static/", template_folder="templates/"
)

text = ""
wcount = 50

with open("english200.txt", "r") as file:
    words = file.read().splitlines()


def textgen(wcount):
    text = ""
    lastword = ""
    for i in range(wcount):
        word = random.choice(words)
        if (word == lastword):  # makes sure 2 words don't repeat
            word = random.choice(words)
        if i == wcount - 1:
            text = text + word
        else:
            text = text + word + " "
        lastword = word
    return text


@app.route("/", methods=["GET"])
def index():
    global text
    repeat = request.args.get("repeat")
    if repeat != "yes" or text == "":
        text = textgen(wcount)
    return render_template("index.html", text=Markup(text.replace("\n", "<br>")))


@app.route("/settings")
def settings():
    return render_template("settings.html")


index_data = ""
stopat = "nothing"

started = False
ended = False
starttime = 0
endtime = 0
tooktime = 0
last_correct_length = 0


@app.route("/index_input", methods=["POST"])
def index_input():
    global index_data
    index_data = request.data.decode("utf-8")
    return 0  # placeholder


@app.route("/settings_input", methods=["POST"])
def settings_input():
    global stopat
    global wcount
    stopat = request.json["stopat"]
    wcount = int(request.json["wcount"])
    return "small dick"  # no idead what to return


@app.route("/settings_status", methods=["POST"])
def settings_status():
    global stopat
    settings_status = request.data.decode("utf-8")
    if settings_status == "gib status":
        data = {"stopat": stopat, "wcount": wcount}
        return jsonify(data)


if __name__ == "__main__":
    app.run()
