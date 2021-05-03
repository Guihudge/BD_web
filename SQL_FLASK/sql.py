import psycopg2
import psycopg2.extras

db = "dragon"
db_user = "guillaume"
connexion = None


def error(raison, conn=None, curr=None):
    if conn is not None:
        conn.close()
    if curr is not None:
        curr.close()

    exit(raison)


def connect_database(user, db):
    print("connexion à la base de donnée")
    try:
        conn = psycopg2.connect(dbname=db, user=user)
    except Exception as e:
        raison = "connexion impossible à la base de donnée : " + str(e)
        error(raison)

    print("connecté à la base de donné")
    return conn


def create_cursor(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cur


def init_db():
    global connexion, cursor
    connexion = connect_database(db_user, db)
    cursor = create_cursor(connexion)
    print("connexion et initialisation effectué")


def exit_database():
    connexion.close()
    cursor.close()
    print("Connexion à la base de donnée fermé")


def execute_query_taille(nom_dragon):
    command = "SELECT * FROM Dragons WHERE Dragon=%s"
    print("requete : ", command, [nom_dragon])

    try:
        cursor.execute(command, [nom_dragon])
    except Exception as e:
        raison = "error when running: " + command + " : " + str(e)
        error(raison, connexion, cursor)

    return cursor.fetchone()


def format_query_taille(result):
    dictionary = {"nom": result[0], "Sexe": result[1], "Longueur": result[2],
                  "Ecailles": result[3], "CracheFeu": result[4], "EnAmour": result[5]}
    return dictionary


def execute_query_nourriture(nom_dragon):
    command = "SELECT produit FROM Repas WHERE Dragon=%s"

    print("requete : ", command, [nom_dragon])

    try:
        cursor.execute(command, [nom_dragon])
    except Exception as e:
        raison = "error when running: " + command + " : " + str(e)
        error(raison, connexion, cursor)

    return cursor.fetchall()


def execute_query_amours(nom_dragon):
    command = "SELECT DragonAimant FROM Amours WHERE DragonAime=%s"

    print("requete : ", command, [nom_dragon])

    try:
        cursor.execute(command, [nom_dragon])
    except Exception as e:
        raison = "error when running: " + command + " : " + str(e)
        error(raison, connexion, cursor)

    return cursor.fetchall()


def format_query_fetchall(result):
    out = []
    for d in result:
        out.append(d[0])
    return out


def get_dragon_list():
    command = "SELECT dragon FROM Dragons"

    print("requete : ", command)

    try:
        cursor.execute(command)
    except Exception as e:
        raison = "error when running: " + command + " : " + str(e)
        error(raison, connexion, cursor)

    result = cursor.fetchall()
    list_dragon = []
    for d in result:
        list_dragon.append(d[0])

    return list_dragon


def check_db_connection():
    if connexion is None:
        init_db()
