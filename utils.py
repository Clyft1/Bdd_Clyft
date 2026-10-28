#Demander a lutilisateur de rentrer un texte et le champ ne doit pas etre vide 
        #Supprimer les espaces inutiles 
        #verifier que le texte nest pas vide 
# SI le texte est vide Afiicher une erreur et recommencer 
#sinon Retourner Le texte 
def demander_texte_non_vide(message):
    # Demande un texte et refuse les réponses vides
    while True:
        texte = input(message).strip()
        if texte:
            return texte
        print("Erreur : cette réponse ne peut pas être vide.")


def demander_nombre_entre(message, maximum):
    # Demande un nombre entre 1 et maximum
    while True:
        saisie = input(message)
        try:
            nombre = int(saisie)
        except ValueError:
            print("Erreur : vous devez saisir un nombre entier.")
            continue
        if 1 <= nombre <= maximum:
            return nombre
        print(f"Erreur : entre un nombre compris entre 1 et {maximum}.")

def decrire(combattant):
    return (f"{combattant.nom} - {combattant.attaque} ATK - "
            f"{combattant.defense} DEF - {combattant.pv} PV")


def afficher_equipe_actuelle(equipe):
    print("\n--- Ton équipe ---")
    if not equipe:
        print("(vide)")
    for numero, perso in enumerate(equipe, start=1):
        print(f"Personnage numero {numero} - {decrire(perso)}")




def afficher_personnages_disponibles(personnages):
    print("\n--- Personnages disponibles ---")
    for numero, perso in enumerate(personnages, start=1):
        print(f"{numero}. {decrire(perso)}")



def afficher_monstre(vague, monstre):
    print(f"\n========== VAGUE {vague} ==========")
    print(f"Un monstre apparaît : {decrire(monstre)}")


def afficher_attaque(attaquant, cible, degats):
    print(f"{attaquant.nom} attaque {cible.nom} : -{degats} PV "
          f"(reste {cible.pv} PV)")



def afficher_etat_equipe(equipe):
    etats = [f"{p.nom} {p.pv} PV" if p.est_vivant() else f"{p.nom} K.O."
             for p in equipe]
    print("Équipe : " + " | ".join(etats))


def afficher_victoire():
    print("Victoire ! Le monstre est vaincu.")



def afficher_defaite():
    print("Défaite... toute l'équipe est à terre.")



def afficher_score(joueur, vagues):
    print(f"\n{joueur}, tu as survécu à {vagues} vague(s).")


def afficher_classement(scores):
    print("\n=========== TOP 3 ===========")
    if not scores:
        print("Aucun score enregistré.")
    for place, score in enumerate(scores, start=1):
        print(f"{place}. {score['player_name']} - {score['waves']} vague(s)")


