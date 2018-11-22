from MaBase import *

#question 4
allée_alien = {(Alien.Nom, Cabine.NoAllee) for Alien in BaseAliens for Cabine in BaseCabines if Alien.NoCabine == Cabine.NoCabine }

print ("les allées correspondants aux aliens sont ",allée_alien)


#question 5
allée2 = {(Alien.Nom) for Alien in BaseAliens for Cabine in BaseCabines if Alien.NoCabine == Cabine.NoCabine if Cabine.NoAllee == '2' }

print ("les aliens dans l'allée 2 sont ",allée2)


#question 6

planetepair ={(Alien.Planete) for Alien in BaseAliens if Alien.NoCabine == '2'or'4'or'6'or'8'}

print ("voici les planete ou les aliens sont dans une cellule pair", planetepair)


#Question 7
AGT = {(Alien.Nom) for Agent in BaseAgents for Gardien in BaseGardiens for Alien in BaseAliens if Agent.Ville == 'Terminus' if Agent.Nom == Gardien.Nom if Gardien.NoCabine == Alien.NoCabine}

print( "les aliens surveillés par les agents venant de terminus sont ",AGT)


#Question 8

GAB = {(Gardien.Nom) for Miam in BaseMiams for Alien in BaseAliens for Gardien in BaseGardiens if Miam.Aliment == 'Bortsch' if Miam.NomAlien == Alien.Nom if Alien.Sexe == 'F' if Alien.NoCabine == Gardien.NoCabine}

print ("Voici les gardiens des aliens féminin mangeant du bortsch ",GAB)


#Question 9
CGT = {(Gardien.NoCabine ) for Agent in BaseAgents for Gardien in BaseGardiens  if Agent.Ville == 'Terminus' if Agent.Nom == Gardien.Nom }
CAF = {(Alien.NoCabine) for Alien in BaseAliens if Alien.Sexe == 'F'}

print ("les cabines dont les gardiens viennent de Terminus sont :",CGT,"les cabines dont les aliens sont des filles sont :" ,CAF,)


#Question 10

lettrealiment = {(Miam.Aliment) for }
