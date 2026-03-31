import random

des = {
    "Dé classique": {"faces": 6, "poids": 80, "bonus": 0},
    "Dé chance": {"faces": 12, "poids": 10, "bonus": 5},
    "Dé démon": {"faces": 20, "poids": 5, "bonus": 10},
    "Dé ange": {"faces": 30, "poids": 3, "bonus": 15},
    "Dé mythique": {"faces": 50, "poids": 1, "bonus": 30},
}

def choisir_de():
    """
    lister les noms, les poids, du dé dans la variable et génère un dé aléatoire avec une probabilité de son poids
    obtenir le nombre de face du dé et le nombre de bonus et renvoyer

    """
    noms = list(des.keys())
    poids = [des[n]["poids"] for n in noms]
    nom = random.choices(noms, weights=poids, k=1)[0]
    faces = des[nom]["faces"]
    bonus = des[nom]["bonus"]
    return nom, faces, bonus

def lancer_des():
    """
    Pendant trois fois, on obtiens les trois dés choisis au hasard et on génère sa valeur aléatoire 
    entre 1 et son nombre de faces on ajouter au
    

    Paramètres : Aucun
    Retour :

    Préconditions :

    Post-conditions :
    
    """

    resultats = []
    for i in range(3):
        nom, faces, bonus = choisir_de()
        valeur = random.randint(1, faces)
        resultats.append({
            "nom": nom,
            "faces": faces,
            "valeur": valeur,
            "bonus": bonus
        })
    return resultats

# Tests unitaires 

assert 

# relancer certains dés
def relancer_des(resultats, indices):
    for i in indices:
        nom, faces, bonus = choisir_de()
        valeur = random.randint(1, faces)
        resultats[i] = {
            "nom": nom,
            "faces": faces,
            "valeur": valeur,
            "bonus": bonus
        }
    return resultats

def calcul_score(resultats):
    valeurs = [d["valeur"] for d in resultats]
    bonus_total = sum(d["bonus"] for d in resultats)
    
    # 1. Calcul du score de base selon les combinaisons (type Yams simplifié)
    score_combinaison = 0
    if valeurs[0] == valeurs[1] == valeurs[2]:
        score_combinaison = sum(valeurs) * 3  # Brelan
    elif valeurs[0] == valeurs[1] or valeurs[0] == valeurs[2] or valeurs[1] == valeurs[2]:
        score_combinaison = sum(valeurs) * 1.5 # Paire (on arrondit à l'entier plus bas)
    else:
        score_combinaison = sum(valeurs)      # Rien de spécial
        
    # 2. Ajout du bonus des dés (le côté "mythique")
    score_final = int(score_combinaison) + bonus_total
    
    return score_final
