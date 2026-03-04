#######################################################################
#                     Projet : Lancé de dé                            #
#######################################################################

# Ce fichier simule le hasard d'un lancé de dé.
# Ajoute le chiffre obtenu à score.

import random

#Initialisation 

dés = {"Dé rouge" : 6, "Dé surprise" : random.randint(1,100) , "Dé Casino" : 777 ,
       "Dé blanc" : 6, "Dé ténébres" : 16, "Dé Chromatique" : 150 , "Dé Archange" : 4000 , 
       "Dé carré" : 4, "Dé lettres" : 9 , "Dé Démon" : 666, "Dé Infini" : 500000 , 
       "Dé pyramide" : 20, "Dé boudchou" : 40 , "Dé Ange" : 1000  , "Dé Monstrueux" : 500 , 
       "Dé Géant" : 60 , "Dé Vitré" : 45 , "Dé Gargantua" : 2000 , "Dé Vieux" : 3 , 
       } 


def lancer_de_dés():
    """fonction qui permet de simuler un lancer de dés"""
    resultat = []
    nb_dés = 5
    for i in range(nb_dés):
        choix_dé = random.choice(list(dés.items()))
        nom , faces = choix_dé
        resultat.append(random.randint(1,faces))
    return resultat


def score():
    """fonction qui ajoute le nombre retourné de la fonction lancer_de_dés en sa somme""" 
    return sum(lancer_de_dés())
        
