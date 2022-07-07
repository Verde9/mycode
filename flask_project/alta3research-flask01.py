#!/usr/bin/python3

from flask import Flask 
from flask import redirect
from flask import url_for
from flask import request
from flask import request 
from flask import render_template
from flask import jsonify
import random

app = Flask(__name__)

yoMama = [
    {
        "joke": "Yo mamma so fat I took a picture of her last Christmas and its still printing"
    },
    {
        "joke": "Yo mama's so ugly, she threw a boomerang and it refused to come back."
    },
    {
        "joke": "Yo mama's teeth are so yellow when she smiles at traffic, it slows down."
    },
    {
        "joke": "Yo mama's cooking so nasty, the flys got together and fixed the hole in the window screen."
    },
    {
        "joke": "Yo mama's so ugly, she looked out the window and was arrested for mooning"
    },
    {
        "joke": "Yo mama's so stupid, she put airbags on her computer in case it crashed"
    },
    {
        "joke": "Yo mama's so stupid, she put lipstick on her forehead to make up her mind"
    },
    {
        "joke": "Yo mama's so fat, when she sits around the house, she SITS AROUND the house"
    },
    {
        "joke": "Yo mama's so ugly, she made a blind kid cry"
    },
    {
        "joke": "Yo mama's so poor, the ducks throw bread at her"
    }
    ]

yoDaddy = [
    {
        "joke": "I'm afraid for the calendar. Its days are numbered."
    },
    {
        "joke": "My wife said I should do lunges to stay in shape. That would be a big step forward."
    },
    {
        "joke": "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!"
    },
    {
        "joke": "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera."
    },
    {
        "joke": "What do a tick and the Eiffel Tower have in common? They're both Paris sites."
    },
    {
        "joke": "What do you call a fish wearing a bowtie? Sofishticated."
    },
    {
        "joke": "How do you follow Will Smith in the snow? You follow the fresh prints."
    },
    {
        "joke": "If April showers bring May flowers, what do May flowers bring? Pilgrims."
    },
    {
        "joke": "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along."
    },
    {
        "joke": "What do you call a factory that makes okay products?" "A satisfactory."
    }
    ]

@app.route("/")
def route():
    return render_template("yomama.html")      

@app.route("/yomama")
def yomama():
    number = random.randrange(0,10)

    return yoMama[number]["joke"]

@app.route("/yodaddy")
def yodaddy():
    number = random.randrange(0,10)

    return yoDaddy[number]["joke"]

@app.route("/yomama/json")
def yomamaJSON():
    return jsonify(yoMama)

@app.route("/yodaddy/json")
def yodaddyJSON():
    return jsonify(yoDaddy)    

     
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

  
 
