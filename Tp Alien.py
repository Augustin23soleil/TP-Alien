
from MaBase import *

#question 4
allée_alien = {(Alien.Nom, Cabine.NoAllee) for Alien in BaseAliens for Cabine in BaseCabines if Alien.NoCabine == Cabine.NoCabine }

print ( "4) les allées correspondants aux aliens sont ",allée_alien)


#question 5
allée2 = {(Alien.Nom) for Alien in BaseAliens for Cabine in BaseCabines if Alien.NoCabine == Cabine.NoCabine if Cabine.NoAllee == '2' }

print ("5) les aliens dans l'allée 2 sont ",allée2)


#question 6

planetepair ={(Alien.Planete) for Alien in BaseAliens if Alien.NoCabine == '2'or'4'or'6'or'8'}

print ("6) voici les planete ou les aliens sont dans une cellule pair", planetepair)


#Question 7
AGT = {(Alien.Nom) for Agent in BaseAgents for Gardien in BaseGardiens for Alien in BaseAliens if Agent.Ville == 'Terminus' if Agent.Nom == Gardien.Nom if Gardien.NoCabine == Alien.NoCabine}

print( "7) les aliens surveillés par les agents venant de terminus sont ",AGT)


#Question 8

GAB = {(Gardien.Nom) for Miam in BaseMiams for Alien in BaseAliens for Gardien in BaseGardiens if Miam.Aliment == 'Bortsch' if Miam.NomAlien == Alien.Nom if Alien.Sexe == 'F' if Alien.NoCabine == Gardien.NoCabine}

print ("8) Voici les gardiens des aliens féminin mangeant du bortsch ",GAB)


#Question 9
#cgt = cabine dont les gardiens viennent de terminus
#caf = cabine alien sont filles
CGT = {(Gardien.NoCabine ) for Agent in BaseAgents for Gardien in BaseGardiens  if Agent.Ville == 'Terminus' if Agent.Nom == Gardien.Nom }
CAF = {(Alien.NoCabine) for Alien in BaseAliens if Alien.Sexe == 'F'}

print ("9) les cabines dont les gardiens viennent de Terminus sont :",CGT,"les cabines dont les aliens sont des filles sont :" ,CAF,)


#Question 10
#la = lettre aliment

la = {(Miam.Aliment, Gardien.Nom, Alien.Nom) for Alien in BaseAliens for Gardien in BaseGardiens for Miam in BaseMiams if Miam.NomAlien == Alien.Nom if Alien.NoCabine == Gardien.NoCabine if Gardien.Nom[0] == Miam.Aliment[0]}

print ("10) voici la liste des aliments commencent par la même lettre que le nom du gardien qui surveille l'alien qui les manges :" ,la)


#Question 11
#ae = alien originaire d'euterpe
ae = {(Alien.Nom, Alien.Planete) for Alien in BaseAliens if Alien.Planete == 'Euterpe'}

print ("11) voici la liste des aliens originaires d'euterpe :" ,ae)


#Question 12
#xna = si il y a un x dans tout les noms des aliens

xna = {(Alien.Nom) for Alien in BaseAliens if 'x' in Alien.Nom }
an = 'Alien.Nom'
k = an.count('x')
if (k==9):
    print("12) tout les aliens ont des x dans leur noms",xna)

else :
    print("12) tout les aliens n'ont pas de x dans leur noms, voici ceux qui en ont :", xna)


#question 13
#agt = alien qui ont un x dans leur nom et dont le gardien viens de terminus

agt = {(Alien.Nom, Agent.Nom) for Alien in BaseAliens for Gardien in BaseGardiens for Agent in BaseAgents if 'x' in Alien.Nom if Agent.Ville == 'Terminus' if Agent.Nom == Gardien.Nom if Gardien.NoCabine == Alien.NoCabine}

if (xna == agt):
    print("13) tout les aliens qui ont un x dans leur nom ont des gardiens qui viennent de Terminus, les voici :", agt)

else :
    print("13) tout les aliens qui ont un x dans leur nom n'ont pas des gardiens venant de Terminus, les voici :", agt)


#question 14
#zy = alien masculin originaire de Trantor qui mange du bortsch
#zz = alien masculin originaire de Trantor qui a un gardien venant de terminus

zy = {(Alien.Nom) for Alien in BaseAliens for Miam in BaseMiams if Alien.Sexe == 'M' if Alien.Planete == 'Trantor' if Alien.Nom == Miam.NomAlien if Miam.Aliment == 'Bortsch'}
zz = {(Alien.Nom) for Alien in BaseAliens for Gardien in BaseGardiens for Agent in BaseAgents if Alien.Sexe == 'M' if Alien.Planete == 'Trantor' if Alien.NoCabine == Gardien.NoCabine if Gardien.Nom == Agent.Nom if Agent.Ville == 'Terminus'}

if (zy == zz) :
    print ("14) il(s) existe(s) un alien(s) masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Termnius, le(s) voici :", zz)

else :
    print ("14) il existe un alien masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Terrminus, le voici :", zy, zz)
