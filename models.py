#representer les personnages et les monstres 

#creer un personnage 
# recevoir son nom , son attaque , sa defense et ses points de vie 

#Enregistrer ses caracteristiques 
# pouvoir verifier si le personnage est encore vivant 

#class 
class Personnage:

  def __init__(self, nom, attaque, defense, pv):
    self.nom = nom
    self.attaque = attaque
    self.defense = defense
    self.pv = pv


  def est_vivant(self):
    #verifier si le personnage possede encore des points de vie 
    return self.pv > 0 


  # creer un monstre 
  #recevoir le nom du monstre son attaque , sa defense 
  #enregistrer ses caracteristiques 
  #Permettre de verifier si le monstre est encore vivant 
  def calculer_degats(self,cible)




  def recevoir_degats



  def attaquer


  def 

  class Monstres: 

   def __init__(self, nom, attaque, defense, pv):
    self.nom = nom
    self.attaque = attaque
    self.defense = defense
    self.pv = pv

   