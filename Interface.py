import pygame, sys, random

#Initialisation

pygame.init()
Longueur, Largeur = 800, 500
screen = pygame.display.set_mode((Longueur, Largeur))
pygame.display.set_caption("Mon Jeu")
clock = pygame.time.Clock()
running = True

print("Start -->")

#Charge menu
img = pygame.image.load('launch.png')
img = pygame.transform.scale(img, (Longueur, Largeur))

# Police
font = pygame.font.Font("Police.ttf", 40)

# Etat du jeu
etat = "menu"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Si on est dans le menu
        if etat == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    etat = "jeu"

    screen.fill((0, 0, 0))

    # ---------- MENU ----------
    if etat == "menu":
        screen.blit(img, (0, 0))

        texte = font.render("Appuie sur ESPACE pour commencer", True, (255, 255, 255))
        rect = texte.get_rect(center=(Longueur//2, Largeur - 50))
        screen.blit(texte, rect)

    # ---------- JEU ----------
    elif etat == "jeu":
        screen.fill((30, 30, 30))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
print("End -->")
sys.exit()
    
