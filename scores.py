def enregistrer_score(collection, joueur, vagues):
    collection.insert_one({"player_name": joueur, "waves": vagues})


def recuperer_meilleurs_scores(collection, nombre=3):
    # Tri par nombre de vagues décroissant, on garde les 3 premiers
    return list(collection.find().sort("waves", -1).limit(nombre))

