from flask import *
import sys
import time
import json
import jinja2
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/hello")
def hello():
    return app.send_static_file("form.html")

def print_hello(name):
    data = "<b>Hello "+ name + "</b>. Nous somme le " + time.strftime("%d/%m/%Y")
    return data

@app.route("/test/<name>")
def hello_name(name):
    return print_hello(name)

@app.route("/after_form")
def after_form():
    prenom = request.args.get('input_prenom')
    return print_hello(prenom)

@app.route('/perso_miserables')
def miserables_characters():
    with open('static/miserables.json') as f:
        data = json.load(f)
        characters = set([n['name'] for n in data['nodes']]) #data['nodes'] est une liste qui contient pour chaque entrée un dictionnaire n dont on veut les données associées à la clé 'name'
        #characters est ma liste de personnages. On fabrique maintenant une chaine de caractères avec l'ensemble des noms (un nom par ligne en html)
        print(type(characters))
        print(characters)
        sep = "<br>\n" 
        return sep.join(characters)

@app.route('/miserables')
def miserables():
    error = request.args.get('error')
    perso_list = ["Président", "Tintin", "Babet", "Napoleon", "Myriel"]
    return render_template("form2.html", character_list = perso_list,  hasError = error)


@app.route('/after_miserables')
def after_miserables():
    prenom = request.args.get('input_prenom')
    prenom_ok = False
    perso = request.args.get('perso')
    perso_ok = False
    with open('static/miserables.json') as f:
        liste_perso = []
        data = json.load(f)
        for i in data['nodes']:
            liste_perso.append(i['name'])

    if prenom == "":
        prenom_ok = True
    
    for i in liste_perso:
        if i == prenom:
            prenom_ok = True
        if i == perso:
            perso_ok = True
    
    if prenom_ok and perso_ok:
        return "<p> Ce sont des personnages du roman"
    elif prenom_ok and not perso_ok:
        return redirect(url_for('miserables', error="Mauvaise saisie dans la liste"))
    elif not prenom_ok and perso_ok:
        return redirect(url_for('miserables', error="Mauvaise saisie dans le champ de texte"))
    else:
        return redirect(url_for('miserables', error="Mauvaise saisie dans les deux champs"))