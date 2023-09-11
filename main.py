from flask import Flask, request, render_template
from markupsafe import Markup
import random

app = Flask(
    __name__, static_url_path="", static_folder="static/", template_folder="templates/"
)

status = "True"

text = ""
wcount = 50

with open("english200.txt", "r") as file:
    words = file.read().splitlines()

for i in range(49):
    text = text + random.choice(words) + " "
    if i == 48:
        text = text + random.choice(words)


@app.route("/")
def index():
    global text
    text = ""
    for i in range(wcount - 1):
        text = text + random.choice(words) + " "
    if i == wcount - 2:
        text = text + random.choice(words)
    return render_template(
        "index.html", text=Markup(text.replace("\n", "<br>")), status=status
    )


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
    # logic()
    return "small dick"  # no idead what to return


@app.route("/settings_status", methods=["POST"])
def settings_status():
    global stopat
    settings_status = request.data.decode("utf-8")
    if settings_status == "gib status":
        return stopat
    else:
        return "stuff is very wrong"


if __name__ == "__main__":
    app.run()
