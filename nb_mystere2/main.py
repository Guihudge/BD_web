from flask import *
import sys
import time
import json
import jinja2
import random
import configparser

from secure_input import *
app = Flask(__name__)

nb = 0
compteur = 0

max_coup = 10
nb_min = 0
nb_max = 100

@app.route("/")
def startup():
    global max_coup, nb_min, nb_max
    config = configparser.ConfigParser()
    while True:
        try:
            f = open("static/config.ini")
            config.read("static/config.ini")
            break
        except:
            config['value'] = {"borne_min" : 0, "borne_max" : 100, "nb_coup" : 10}
            f = open("static/config.ini", "w")
            config.write(f)
            f.close()
    print(config)
    max_coup = int(config['value']["nb_coup"])
    nb_min = int(config['value']["borne_min"])
    nb_max = int(config['value']["borne_max"])

    return redirect(url_for("start"))

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/config")
def config():
    return render_template("config.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/config_save")
def config_save():
    nb_coup_web, nb_coup_ok = secure_input(request.args.get("nb_coup"))
    borne_min_web, borne_min_ok = secure_input(request.args.get("borne_min"))
    borne_max_web, borne_max_ok = secure_input(request.args.get("borne_max"))
    if nb_coup_ok and borne_min_ok and borne_max_ok:
        config = configparser.ConfigParser()
        config['value'] = {"borne_min" : borne_min_web, "borne_max" : borne_max_web, "nb_coup" : nb_coup_web}
        f = open("static/config.ini", "w")
        config.write(f)
        f.close()
        return redirect(url_for("startup"))
    else:
        return render_template("error.html", error_cause = "Valeur invalide en paramètre")

@app.route("/affichage")
def affichage ():
    trouver = False
    result = request.args.get("result")
    if result == "Trouver":
        return render_template("win.html", compteur = compteur)
    elif result == "perdu":
        return render_template("lose.html", nb = nb)
    else:
        return render_template("form.html", result = result, compteur = compteur, borne_min = nb_min, borne_max = nb_max)

@app.route("/processe")
def processe():
    global compteur # à changer
    state = ""
    nombre_user, ok = secure_input(request.args.get("nombre"))
    if ok:
        if compteur >= max_coup:
            state = "perdu"
        elif nombre_user == nb:
            state = "Trouver"
        elif nombre_user > nb :
            state = "Plus petit"
        else:
            state = "Plus grand"
        
        compteur += 1
        
        return redirect(url_for("affichage", result = state))
    else:
        return render_template("error.html", error_cause = "Valeur invalide en paramètre")

@app.route("/reset")
def reset():
    global nb, compteur # à changer
    compteur = 0
    print(type(nb_min), type(nb_max))
    nb = random.randint(nb_min, nb_max)
    return redirect(url_for("affichage"))