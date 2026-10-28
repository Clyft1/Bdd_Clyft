
from pymongo.errors import PyMongoError
from db_init import ouvrir_connexion, recuperer_base, fermer_connexion
from equipe import recuperer_personnages, choisir_equipe
from scores import enregistrer_score, recuperer_meilleurs_scores
from utils import (demander_texte_non_vide, demander_nombre_entre,
                   )

# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
#

#def main 
#Afficher un message de bienvenue au lancement du jeu 
#Je cree une variable Choix et jy mets une chaine vide 
#Je reste dans la boucle tant que le joueur ne choisi pas 1 
#jaffiche le menu pour montrer les options disponibles 
# je recupere un choix valide entre 1 et 3 
# si le joueur tape 1 je demarre le jeux 
#si il tape 2 le claasement 

#quand le choix vaut 3 la boucle sarrete et on dit "au revoir"


#Proceder 

#Afficher un message de bienvenu 
#Rester dans la boucle jusqua ce que le joueur choisisse 1
#Afficher MENU
#Recuperer un choix valide 

#Si le choix vaut 1 
#demander le nom du joueur 
#Lancer une partie 

#SI le choix vaut 2 
#Afficher les 3 meilleures scores 

#Si le choix vaut 3
#Afficher un message d'au revoir 
#Quitter la boucle 

# EN CAS DERREUR Afficher un message .

MENU = ["Lancer le jeu", "Afficher les scores", "Quitter"]


def afficher_menu():
    print("\n================= MENU PRINCIPAL =================")
    for numero, element in enumerate(MENU, start=1):
        print(f"{numero}. {element}")
    print("====================================================")


def recuperer_choix():
    return demander_nombre_entre("Ton choix : ", len(MENU))


def demarrer_jeu(db):
    joueur = demander_texte_non_vide("Entre ton nom de joueur : ")
    equipe = choisir_equipe(recuperer_personnages(db.game_characters))
    vagues = lancer_partie(equipe, db.game_monsters)
    enregistrer_score(db.game_score, joueur, vagues)
    afficher_score(joueur, vagues)
    afficher_classement(recuperer_meilleurs_scores(db.game_score))


def afficher_scores(db):
    afficher_classement(recuperer_meilleurs_scores(db.game_score))


def executer_choix(choix, db):
    if choix == 1:
        demarrer_jeu(db)
    elif choix == 2:
        afficher_scores(db)


def boucle_menu(db):
    choix = 0
    while choix != 3:
        afficher_menu()
        choix = recuperer_choix()
        executer_choix(choix, db)


def main():
    print("Bienvenue dans mon jeu de bagarre")
    client = ouvrir_connexion()
    try:
        boucle_menu(recuperer_base(client))
    finally:
        fermer_connexion(client)
    print("Au revoir")

