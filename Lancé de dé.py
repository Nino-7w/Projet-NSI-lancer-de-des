#######################################################################
#                     Projet : Lancé de dé                            #
#######################################################################

# Ce fichier simule le hasard d'un lancé de dé.
# Ajoute le chiffre obtenu à score.

import random

#Initialisation 

dés = {"Dé rouge" : 6,
       "Dé blanc" : 6,
       "Dé carré" : 4,
       "Dé pyramide" : 20,
       }


def lancer_de_dés():
    """fonction qui permet de simuler un lancer de dés"""
    resultat = []
    nb_dés = 5
    for i in range(nb_dés):
        choix_dé = random.choice(list(dés.keys()))
        res_dé = random.choice(list(dés.values()))
        resultat.append(random.randint(1,res_dé))
        print(choix_dé)
    return resultat

def score():
    """fonction qui ajoute le nombre retourné de la fonction lancer_de_dés en sa somme""" 
    return sum(lancer_de_dés())
