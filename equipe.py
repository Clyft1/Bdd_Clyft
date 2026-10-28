"""Création de l'équipe du joueur."""
from models import Personnage
from utils import (demander_nombre_entre, afficher_equipe_actuelle,
                   afficher_personnages_disponibles)


def recuperer_personnages(collection):
    # Récupère les personnages depuis MongoDB
    return [Personnage.depuis_document(doc) for doc in collection.find()]


def choisir_personnage(disponibles):
    numero = demander_nombre_entre("Ton choix : ", len(disponibles))
    return disponibles.pop(numero - 1)  # retiré de la liste : choix unique




def choisir_equipe(personnages):
    """Fait choisir 3 personnages différents."""
    disponibles = list(personnages)
    equipe = []
    while len(equipe) < TAILLE_EQUIPE:
        afficher_equipe_actuelle(equipe)
        afficher_personnages_disponibles(disponibles)
        equipe.append(choisir_personnage(disponibles))
    afficher_equipe_actuelle(equipe)
    return equipe
