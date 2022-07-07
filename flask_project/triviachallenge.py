#!/usr/bin/python3

from flask import Flask 
from flask import redirect
from flask import url_for
from flask import request
from flask import request 
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/start")
def start():
    return render_template("trivia.html")


@app.route("/correct")
def correct():
    return "That's correct!"

@app.route("/incorrect")
def incorrect():
    return "That's incorrect!"    


@app.route("/login", methods = ["POST", "GET"])
def login():  

    if request.method == "POST":
        if request.form.get("nm") == "Supplies":
            return redirect(url_for("correct"))
        else:
            return redirect(url_for("incorrect"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)