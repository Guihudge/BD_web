from flask import *
import sql

# import sys
# import time
# import json
# import jinja2

app = Flask(__name__)


@app.route("/")
def init():
    sql.init_db()
    return redirect(url_for("home"))


@app.route("/home")
def home():
    sql.check_db_connection()
    liste_dragon = sql.get_dragon_list()
    # print(liste_dragon)
    return render_template("home.html", liste_dragon=liste_dragon)


@app.route("/dragon_after")
def dragon_after():
    sql.check_db_connection()
    nom_dragon = request.args.get("dragon_name")
    alimentation = request.args.get("alimentation")
    amours = request.args.get("amours")
    print(nom_dragon, alimentation, amours)
    dragon = sql.format_query_taille(sql.execute_query_taille(nom_dragon))
    if alimentation == "on":
        alimentation_data = sql.format_query_fetchall(sql.execute_query_nourriture(nom_dragon))
    else:
        alimentation_data = None

    if amours == "on":
        amours_data = sql.format_query_fetchall(sql.execute_query_amours(nom_dragon))
    else:
        amours_data = None

    return render_template("out.html", dragon=dragon, alimentation=alimentation, alimentation_data=alimentation_data,
                           amours=amours, amours_data=amours_data)
