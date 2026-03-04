#######################################################################
#                     Projet : Lancé de dé                            #
#######################################################################

# Ce fichier simule le hasard d'un lancé de dé.
# Ajoute le chiffre obtenu à score.

import random

# =========================
# 🎲 Définition des dés
# =========================

des = {
    "Dé rouge": {"faces": 6, "poids": 10},
    "Dé blanc": {"faces": 6, "poids": 10},
    "Dé carré": {"faces": 4, "poids": 10},
    "Dé Vieux": {"faces": 3, "poids": 12},

    "Dé ténèbres": {"faces": 16, "poids": 8},
    "Dé lettres": {"faces": 9, "poids": 8},
    "Dé pyramide": {"faces": 20, "poids": 7},
    "Dé boudchou": {"faces": 40, "poids": 6},
    "Dé Géant": {"faces": 60, "poids": 5},
    "Dé Vitré": {"faces": 45, "poids": 5},

    "Dé Chromatique": {"faces": 150, "poids": 3},
    "Dé Monstrueux": {"faces": 500, "poids": 2},
    "Dé Casino": {"faces": 777, "poids": 2},
    "Dé Démon": {"faces": 666, "poids": 2},

    "Dé Ange": {"faces": 1000, "poids": 1},
    "Dé Gargantua": {"faces": 2000, "poids": 1},
    "Dé Archange": {"faces": 4000, "poids": 1},
    "Dé Infini": {"faces": 500000, "poids": 0.2},

    "Dé surprise": {"faces": random.randint(1, 100), "poids": 4}
}

# =========================
# 🎲 Sélection d'un dé pondéré
# =========================

def choisir_de():
    noms = list(des.keys())
    poids = [des[nom]["poids"] for nom in noms]
    nom_choisi = random.choices(noms, weights=poids, k=1)[0]
    return nom_choisi, des[nom_choisi]["faces"]

# =========================
# 🎲 Lancer de plusieurs dés
# =========================

def lancer_des(nombre=5):
    resultats = []

    for _ in range(nombre):
        nom, faces = choisir_de()
        valeur = random.randint(1, faces)

        resultats.append({
            "nom": nom,
            "faces": faces,
            "valeur": valeur
        })

    return resultats

# =========================
# 🧮 Calcul du score total
# =========================

def calcul_score(resultats):
    return sum(de["valeur"] for de in resultats)
        
