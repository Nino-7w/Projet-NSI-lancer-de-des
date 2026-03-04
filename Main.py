#######################################################################
#                     Projet : Lancé de dé                            #
#######################################################################

# Ce fichier lance et organise le programme afin d'excécuter toutes les instructions dans le bon ordre.
# Ce fichier sera donc celui à éxécuter afin de jouer au jeu

# =========================
# 🎲 Lancer une main
# =========================

main_actuelle = []

def nouvelle_main():
    global main_actuelle
    main_actuelle = []
    for _ in range(5):
        nom, de = choisir_de()
        valeur = random.randint(1, de["faces"])
        main_actuelle.append((nom, valeur, de))
    afficher_main()
    
# =========================
# 🔄 Relance
# =========================    

def relancer():
    if joueur["relances"] > 0:
        joueur["relances"] -= 1
        nouvelle_main()    


# =========================
# ☠️ Game Over
# =========================

def game_over():

    
def jeu_principale():
    return score():
