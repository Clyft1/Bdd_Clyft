"""Connexion à MongoDB + remplissage de la base (python db_init.py)."""
from pymongo import MongoClient

# Adresse du serveur et nom de la base
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "clyf_Bdd"

PERSONNAGES = [
    {"name": "Paladin", "attack": 20, "defense": 12, "hp": 120},
    {"name": "Chevalier", "attack": 22, "defense": 10, "hp": 110},
    {"name": "Berserker", "attack": 29, "defense": 6, "hp": 90},
    {"name": "Archer", "attack": 26, "defense": 7, "hp": 85},
    {"name": "Sorcier", "attack": 32, "defense": 4, "hp": 75},
    {"name": "Guerrier", "attack": 24, "defense": 8, "hp": 100},
    {"name": "Moine", "attack": 22, "defense": 9, "hp": 95},
    {"name": "Voleur", "attack": 28, "defense": 5, "hp": 80},
    {"name": "Chasseur", "attack": 23, "defense": 8, "hp": 90},
    {"name": "Druide", "attack": 21, "defense": 9, "hp": 100},
]

MONSTRES = [
    {"name": "Gobelin", "attack": 10, "defense": 6, "hp": 150},
    {"name": "Orc", "attack": 10, "defense": 8, "hp": 180},
    {"name": "Dragon", "attack": 10, "defense": 12, "hp": 200},
    {"name": "Zombie", "attack": 10, "defense": 7, "hp": 160},
    {"name": "Troll", "attack": 10, "defense": 10, "hp": 190},
    {"name": "Spectre", "attack": 24, "defense": 6, "hp": 170},
    {"name": "Golem", "attack": 21, "defense": 14, "hp": 210},
    {"name": "Vampire", "attack": 26, "defense": 9, "hp": 175},
    {"name": "Loup-garou", "attack": 24, "defense": 8, "hp": 185},
    {"name": "Squelette", "attack": 19, "defense": 7, "hp": 155},
]


def ouvrir_connexion():
    """Ouvre la connexion et vérifie que MongoDB répond."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    client.admin.command("ping")
    return client


def recuperer_base(client):
    return client[DB_NAME]


def fermer_connexion(client):
    client.close()


def remplir_collection(collection, documents):
    collection.drop()
    collection.insert_many(documents)


def initialiser_base(db):
    db.game_score.drop()
    remplir_collection(db.game_characters, PERSONNAGES)
    remplir_collection(db.game_monsters, MONSTRES)


def main():
    client = ouvrir_connexion()
    initialiser_base(recuperer_base(client))
    fermer_connexion(client)
    print("Base de données initialisée.")


if __name__ == "__main__":
    main()
