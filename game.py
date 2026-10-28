
# PRosceder 

  #Afficher les personnages disponibles
    #Créer une équipe de 3 personnages différents

    #Initialiser le nombre de vagues à 0

    #TANT QUE l'équipe possède au moins un personnage vivant

        #Sélectionner un monstre au hasard dans MongoDB
        #Afficher les caractéristiques du monstre

        #TANT QUE le monstre est vivant ET l'équipe est vivante

            #POUR chaque personnage vivant de l'équipe
                #Calculer les dégâts
                #Retirer les points de vie du monstre

                #SI le monstre est mort
                    ##FIN SI

            #SI le monstre est vivant ET l'équipe est vivante
                #Choisir un personnage vivant au hasard
                #Calculer les dégâts du monstre
                #Retirer les points de vie du personnage
            #FIN SI

            #Afficher l'état de l'équipe

        #FIN TANT QUE

        #SI le monstre est vaincu
           # Augmenter le nombre de vagues de 1
        #FIN SI

    #FIN TANT QUE

    #Afficher le nombre de vagues remportées
    #Enregistrer le score du joueur dans MongoDB

#FIN FONCTION


#FONCTION afficher_classement()

    #Récupérer les scores depuis MongoDB
    #Trier les scores par nombre de vagues décroissant
    #Sélectionner les 3 meilleurs scores
    #Afficher le classement

#FIN FONCTION



#recuperer personnages 


import random
from models import 
from utils import (afficher_monstre, afficher_attaque, afficher_etat_equipe,
                   afficher_victoire, afficher_defaite)


def recuperer_monstre_aleatoire(collection):
    # Tire un monstre au hasard dans MongoDB
    doc = next(collection.aggregate([{"$sample": {"size": 1}}]))
    return Monstre.depuis_document(doc)

def membres_vivants(equipe):
    return [perso for perso in equipe if perso.est_vivant()]


def equipe_vivante(equipe):
    return len(membres_vivants(equipe)) > 0

def tour_equipe(equipe, monstre):
    """Chaque personnage vivant attaque ; on s'arrête si le monstre meurt."""
    for perso in membres_vivants(equipe):
        degats = perso.attaquer(monstre)
        afficher_attaque(perso, monstre, degats)
        if not monstre.est_vivant():
            return

def tour_monstre(monstre, equipe):
    """Le monstre attaque un personnage vivant au hasard."""
    cible = random.choice(membres_vivants(equipe))
    degats = monstre.attaquer(cible)
    afficher_attaque(monstre, cible, degats)



def jouer_vague(equipe, monstre):
    """Combat jusqu'à la mort du monstre ou de l'équipe. True = victoire."""
    while monstre.est_vivant() and equipe_vivante(equipe):
        tour_equipe(equipe, monstre)
        if monstre.est_vivant():
            tour_monstre(monstre, equipe)
        afficher_etat_equipe(equipe)
    return equipe_vivante(equipe)


def lancer_partie(equipe, collection_monstres):
    """Enchaîne les vagues jusqu'à la défaite. Retourne les vagues gagnées."""
    vagues = 0
    while True:
        monstre = recuperer_monstre_aleatoire(collection_monstres)
        afficher_monstre(vagues + 1, monstre)
        if not jouer_vague(equipe, monstre):
            afficher_defaite()
            return vagues
        afficher_victoire()
        vagues += 1
