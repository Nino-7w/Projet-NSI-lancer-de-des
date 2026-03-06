import pygame
import sys
from game import Game
from settings import Settings
settings = Settings()

pygame.init()
LONGUEUR, LARGEUR = 800, 500
screen = pygame.display.set_mode((LONGUEUR, LARGEUR))
pygame.display.set_caption("Yamde")
clock = pygame.time.Clock()

# Assets
menu_img = pygame.transform.scale(pygame.image.load("assets/image/launch.png"), (LONGUEUR, LARGEUR))
poker_img = pygame.transform.scale(pygame.image.load("assets/image/poker.png"), (LONGUEUR, LARGEUR))
font = pygame.font.Font("assets/police/Police.ttf", 35)

pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/musique.mp3")
pygame.mixer.music.set_volume(0.13) 
pygame.mixer.music.play(-1)
son_lancer = pygame.mixer.Sound("assets/sounds/dice_roll.mp3")
son_victoire = pygame.mixer.Sound("assets/sounds/win.mp3")
son_défaite = pygame.mixer.Sound("assets/sounds/lose.mp3")
son_clic = pygame.mixer.Sound("assets/sounds/click.mp3")


game = Game(screen)
etat = "menu"
running = True
compteur_menu = 0

while running:
    compteur_menu += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if etat == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.manches = [0, 0]
                game.rejouer()
                etat = "jeu"
                txt_param = font.render("Appuie sur P pour Paramètres", True, (200, 200, 200))
                screen.blit(txt_param, (50, 450))
                # Gestion du changement d'état
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    etat = "settings"

        elif etat == "settings":
            if event.key == pygame.K_RETURN:
                settings.res_index = (settings.res_index + 1) % len(settings.resolutions)
                w, h = settings.get_res()
                screen = pygame.display.set_mode((w, h))
                # Important : Recalculer les échelles
                menu_img = pygame.transform.scale(pygame.image.load("assets/image/launch.png"), (w, h))
                poker_img = pygame.transform.scale(pygame.image.load("assets/image/poker.png"), (w, h))

            if event.key == pygame.K_UP:
                settings.volume = min(1.0, settings.volume + 0.1)
                pygame.mixer.music.set_volume(settings.volume)
            if event.key == pygame.K_DOWN:
                settings.volume = max(0.0, settings.volume - 0.1)
                pygame.mixer.music.set_volume(settings.volume)
            if event.key == pygame.K_ESCAPE:
                etat = "menu"

        elif etat == "jeu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    game.manches = [0, 0]
                    game.rejouer()

                # LOGIQUE DE LA TOUCHE ENTREE (La clé du problème)
                if event.key == pygame.K_RETURN:
                    if game.gagnant_partie: # Si le jeu est fini
                        etat = "menu"
                    elif game.gagnant_tour: # Si la manche est finie
                        game.rejouer()
                    elif game.attendre_ia: # Si c'est au tour de l'IA
                        game.jouer_ia()
                    elif not game.resultats: # Premier lancer
                        game.lancer()
                    elif not game.lancer_termine: # Valider son score
                        game.relances = 0
                        game.relancer()

                # Sélections
                if game.current_player == 0 and not game.lancer_termine:
                    if event.key == pygame.K_1: game.toggle(0)
                    if event.key == pygame.K_2: game.toggle(1)
                    if event.key == pygame.K_3: game.toggle(2)
                    if event.key == pygame.K_r: game.relancer()

    # Affichage
    # 1. Dessine le fond (Menu ou Jeu)
    if etat == "menu":
        screen.blit(menu_img, (0, 0))
        if (compteur_menu // 30) % 2 == 0:
            txt = font.render("ESPACE POUR COMMENCER", True, (255, 255, 255))
            screen.blit(txt, (LONGUEUR//2 - txt.get_width()//2, 430))
    elif etat == "jeu":
        screen.blit(poker_img, (0, 0))
        game.draw(font)

    # 2. Dessine le carré SETTINGS (AU-DESSUS DE TOUT)
    if etat == "settings":
        # On remplit le rectangle avec une couleur vive (Rouge) 
        # pour vérifier s'il s'affiche enfin
        pygame.draw.rect(screen, (255, 0, 0), (200, 100, 400, 300))
        
        # Test de texte
        txt = font.render("TEST PARAMETRES", True, (255, 255, 255))
        screen.blit(txt, (250, 150))

    # 3. Mettre à jour l'affichage UNE SEULE FOIS
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
