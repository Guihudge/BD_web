import json
with open('static/miserables.json') as f:
    liste_perso = []
    data = json.load(f)
    for i in data['nodes']:
        liste_perso.append(i['name'])

print(liste_perso)