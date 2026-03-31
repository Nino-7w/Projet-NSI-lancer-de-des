import pygame  # Import de la bibliothèque pygame (graphismes, sons, etc.)
import sys  # Permet de quitter proprement le programme
from game import Game  # Classe qui gère toute la logique du jeu
from settings import Settings  # Classe qui gère les paramètres (volume, résolution)

settings = Settings()  # Création de l'objet paramètres

pygame.init()  # Initialise tous les modules pygame

LONGUEUR, LARGEUR = 1280, 800  # Dimensions de la fenêtre (largeur, hauteur)

screen = pygame.display.set_mode((LONGUEUR, LARGEUR))  # Création de la fenêtre (Surface principale)

pygame.display.set_caption("Yamdeck")  # Titre de la fenêtre

clock = pygame.time.Clock()  # Horloge pour limiter les FPS

# Assets (images + police)
menu_img = pygame.transform.scale(pygame.image.load("assets/image/launch.png"), (LONGUEUR, LARGEUR))  # Image du menu 
poker_img = pygame.transform.scale(pygame.image.load("assets/image/poker.png"), (LONGUEUR, LARGEUR))  # Image du jeu 

font = pygame.font.Font("assets/police/Police.ttf", 51)  # Chargement de la police personnalisée

# Audio
pygame.mixer.init()  # Initialisation du système audio  mixer = module de pygame et # music = partie de mixer dédiée à la musique

pygame.mixer.music.load("assets/sounds/musique.mp3")  # Chargement de la musique
# dans les paramètres
pygame.mixer.music.play(-1)  # Lecture en boucle infinie

son_lancer = pygame.mixer.Sound("assets/sounds/dice_roll.mp3")  # Son de lancer
son_victoire = pygame.mixer.Sound("assets/sounds/win.mp3")  # Son de victoire
son_défaite = pygame.mixer.Sound("assets/sounds/lose.mp3")  # Son de défaite
son_clic = pygame.mixer.Sound("assets/sounds/click.mp3")  # Son de clic

# Initialisation du jeu
game = Game(screen)  # Création du jeu avec la surface écran

etat = "menu"  # État initial (menu / jeu / settings)
running = True  # Boucle principale active
compteur_menu = 0  # Compteur pour animations du menu

# Boucle principale du jeu
while running:
    compteur_menu += 1  # Incrémentation du compteur à chaque frame

    for event in pygame.event.get():  # Récupération des événements
        if event.type == pygame.QUIT:  # Si on ferme la fenêtre
            running = False  # On arrête la boucle

        # ================= MENU =================
        if etat == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # Appui sur ESPACE
                game.manches = [0, 0]  # Reset score
                game.rejouer()  # Nouvelle partie
                etat = "selection"  # Passage en mode jeu

            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:  # Appui sur P
                etat = "settings"  # Passage en paramètres

        elif etat == "settings":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:       # augmente le volume
                game.increase_volume()      # Appel de la classe game et de la fonction
                pygame.mixer.music.set_volume(game.volume)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:   # diminue le volume
                game.decrease_volume()
                pygame.mixer.music.set_volume(game.volume)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:# Échap retourne au menu
                etat = "menu"

        # ================= JEU =================
        elif etat == "selection":
            ia = ["ia_mauvaise","ia_moyenne","ia_forte"]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                ia_selectionnee = ["ia_mauvaise"]
                etat = "jeu"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                ia_selectionnee = ["ia_moyenne"]
                etat = "jeu"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                ia_selectionnee = ["ia_forte"]
                etat = "jeu"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                etat = "menu"

        elif etat == "jeu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:  # Nouvelle partie
                    game.manches = [0, 0]
                    game.rejouer()

                if event.key == pygame.K_RETURN:  # Touche principale d'action
                    if game.gagnant_partie:  # Fin de partie
                        etat = "menu"
                    elif game.gagnant_tour:  # Fin de manche
                        game.rejouer()
                    elif game.attendre_ia:  # Tour de l'IA
                        game.jouer_ia(ia_selectionnee)
                    elif not game.resultats:  # Premier lancer
                        game.lancer()
                    elif not game.lancer_termine:  # Validation score
                        game.relances = 0
                        game.relancer()

                # Sélection des dés
                if game.current_player == 0 and not game.lancer_termine:
                    if event.key == pygame.K_1:
                        game.toggle(0)
                    if event.key == pygame.K_2:
                        game.toggle(1)
                    if event.key == pygame.K_3:
                        game.toggle(2)
                    if event.key == pygame.K_r: game.relancer()

    # ================= AFFICHAGE =================

    if etat == "menu":
        screen.blit(menu_img, (0, 0))  # Affiche fond menu

        if (compteur_menu // 30) % 2 == 0:  # Texte clignotant
            txt = font.render("ESPACE POUR COMMENCER", True, (255, 255, 255))
            screen.blit(txt, (LONGUEUR//2 - txt.get_width()//2, 700))

    elif etat == "jeu":
        screen.blit(poker_img, (0, 0))  # Fond du jeu
        game.draw(font)  # Dessine le jeu

    elif etat == "settings":
        screen.fill((30, 30, 30))  # Fond gris foncé
        
        txt = font.render("TEST PARAMETRES", True, (255, 255, 255))
        # Instructions pour revenir au menu
        txt_revenir = font.render("Appuie sur ESPACE pour revenir ", True, (200, 200, 200))
        txt_instruction = font.render("HAUT monter le volume | BAS baisser le volume", True, (200, 200, 200))
        screen.blit(txt_revenir, (200, 500))
        screen.blit(txt_instruction, (25, 300))
    

    elif etat == "selection":
        screen.fill((30, 30, 30))  # Fond gris foncé
        texte = font.render("1 IA facile | 2 IA moyenne | 3 IA difficile", True, (255, 255, 255))
        screen.blit(texte, (100, 200))
    
    # Rafraîchissement écran
    pygame.display.update()  # Met à jour l'affichage
    clock.tick(60)  # Limite à 60 FPS

# Fermeture propre
pygame.quit()  # Quitte pygame
sys.exit()  # Quitte le programme Python
