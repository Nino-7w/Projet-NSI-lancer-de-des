import pygame
import random
from dice import lancer_des, relancer_des, calcul_score

# --- SONS SÉCURISÉS ---
pygame.mixer.init()
def charger_son(path):
    try: return pygame.mixer.Sound(path)
    except: return None
Musique = charger_son("assets/sounds/musique.mp3")
SON_LANCER = charger_son("assets/sounds/dice_roll.mp3")
SON_DEFAITE = charger_son("assets/sounds/lose.mp3")
SON_CLIC = charger_son("assets/sounds/click.mp3")
SON_VICTOIRE = charger_son("assets/sounds/win.mp3")

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.players = ["Joueur", "IA"]
        self.score_total = [0, 0] # Scores de la manche actuelle
        self.manches = [0, 0]     # Nombre de manches gagnées
        self.obj_victoire = 3
        self.rejouer() # Initialise le reste
        self.volume = 0.3
        pygame.mixer.music.set_volume(self.volume)
        

    def rejouer(self):
        """Réinitialise tout pour une nouvelle MANCHE"""
        self.current_player = 0
        self.resultats = []
        self.selection = [False, False, False]
        self.relances = 1
        self.lancer_termine = False
        self.attendre_ia = False
        self.gagnant_tour = None
        self.gagnant_partie = None

    def lancer(self):
        if SON_LANCER: SON_LANCER.play()
        self.resultats = lancer_des()
        self.selection = [False, False, False]
        self.relances = 1
        self.lancer_termine = False
        self.gagnant_tour = None

    def toggle(self, index):
        if not self.lancer_termine and self.resultats:
            if SON_CLIC: SON_CLIC.play()
            self.selection[index] = not self.selection[index]

    def relancer(self):
        """
        Cette fonction permet au joueur de relancer les dés
        """
        if self.relances > 0 and any(self.selection):
            if SON_LANCER: SON_LANCER.play()
            indices = [i for i, v in enumerate(self.selection) if v]
            self.resultats = relancer_des(self.resultats, indices)
            self.relances -= 1
            self.selection = [False, False, False]
        
        # Si plus de relances ou si on valide sans sélectionner (any=False)
        if self.relances == 0 or not any(self.selection):
            self.score_total[self.current_player] = calcul_score(self.resultats)
            self.lancer_termine = True
            if self.current_player == 0: 
                self.attendre_ia = True
    
    def jouer_ia(self, ia_selectionnee):
        """
        Gère le tour de jeu de l'IA.
        """
        self.current_player = 1
        self.lancer()
        valeurs = [d["valeur"] for d in self.resultats]
        if ia_selectionnee == ["ia_mauvaise"]:
            # Stratégie : jouer au hasard
            hasard = random.randint(0, 2)
            self.selection[hasard] = True
        elif ia_selectionnee == ["ia_moyenne"]:
            # Stratégie : relancer si la somme est à moins de 10
            if sum(valeurs) < 10: 
                self.selection = [v < 12 for v in valeurs]
        elif ia_selectionnee == ["ia_forte"]:
            # Stratégie : relancer si la somme est à moins de 20
            if sum(valeurs) < 20: 
                self.selection = [v < 12 for v in valeurs]
            
        
        # Si l'IA a choisi de relancer
        if any(self.selection):
            self.relancer()
        else:
            self.score_total[1] = calcul_score(self.resultats)
            self.lancer_termine = True
    
        # --- DÉTERMINATION DU VAINQUEUR DE LA MANCHE ---
        if self.score_total[0] > self.score_total[1]:
            self.manches[0] += 1
            self.gagnant_tour = "Vous gagnez la manche !"
        elif self.score_total[1] > self.score_total[0]:
            self.manches[1] += 1
            self.gagnant_tour = "L'IA gagne la manche !"
        else:
            self.gagnant_tour = "Égalité sur cette manche !"
        
        # Victoire finale ?
        if self.manches[0] >= self.obj_victoire: self.gagnant_partie = "JOUEUR"
        if self.gagnant_partie == "JOUEUR" :
            SON_VICTOIRE.play()
        elif self.manches[1] >= self.obj_victoire: 
            self.gagnant_partie = "IA"
            SON_DEFAITE.play()
        
        self.attendre_ia = False

    def draw(self, font):
        """
        Affiche à l'écran toutes les informations de jeu
        """
        larg = self.screen.get_width()
        
        # 1. Scores globaux (Manches)
        txt_m = font.render(f"Manches: J {self.manches[0]} | IA {self.manches[1]}", True, (255, 255, 255))
        self.screen.blit(txt_m, (20, 20))

        #1.5. Instructions global
        txt_nreplay = font.render("N pour Rejouer", True, (0, 200, 255))
        self.screen.blit(txt_nreplay, (920, 20))
        
        # 2. Dés et Bonus
        y = 170
        for i, d in enumerate(self.resultats):
            texte = f"{d['nom']} : {d['valeur']} (+{d['bonus']})"
            if self.selection[i]: texte += " [RELANCE]"
            couleur = (255, 0, 0) if self.selection[i] else (255, 255, 0)
            self.screen.blit(font.render(texte, True, couleur), (100, y))
            y += 110

        # 2.5 Score total
        textescore = font.render(f"Score Joueur : {self.score_total[0]}", True, (255, 255, 255))
        self.screen.blit(textescore, (830, 200))

        textescoreia = font.render(f"Score IA : {self.score_total[1]}", True, (255, 255, 255))
        self.screen.blit(textescoreia, (830, 250))

        # 3. Messages de transition
        if self.gagnant_partie:
            msg = font.render(f"VICTOIRE FINALE : {self.gagnant_partie} !", True, (255, 215, 0))
            self.screen.blit(msg, (larg//2 - msg.get_width()//2, 550))
        elif self.gagnant_tour:
            msg = font.render(self.gagnant_tour, True, (0, 255, 255))
            self.screen.blit(msg, (larg//2 - msg.get_width()//2, 500))
            inst = font.render("ENTREE pour manche suivante", True, (255, 255, 255))
            self.screen.blit(inst, (larg//2 - inst.get_width()//2, 550))
        elif self.attendre_ia:
            inst = font.render("ENTREE pour laisser jouer l'IA", True, (255, 165, 0))
            self.screen.blit(inst, (20, 730))
        elif self.current_player == 0 and not self.lancer_termine:
            inst = font.render("ENTREE: Lancer dés | 1,2,3: Choisir dés | R: Relancer", True, (0, 255, 0))
            self.screen.blit(inst, (20, 730))

    
    def increase_volume(self):
        """
        Fonction qui permet d'augmenter le volume de la musique
        """
        if self.volume < 1.0:
            self.volume += 0.05
            pygame.mixer.music.set_volume(self.volume) # augmente le volume

    def decrease_volume(self):
        """
        Fonction qui permet de diminuer le volume de la musique
        """
        if self.volume > 0.0:
            self.volume -= 0.05
            pygame.mixer.music.set_volume(self.volume) # baisse le volume


