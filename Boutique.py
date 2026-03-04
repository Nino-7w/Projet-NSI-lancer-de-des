Python 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Liste des objets disponibles dans la boutique
... Objets = {
...     "Dé chanceux": {"prix": 500, "bonus": 1},
...     "Dé doré": {"prix": 1500, "bonus": 2},
...     "Trèfle magique": {"prix": 3000, "bonus": 3},
...     "👑 Couronne d’or": {"prix": 100, "bonus": 1.5},
...     "bourse magique": {"prix": 250, "type": "bonus_pieces"}
... }
... 
... def boutique(pieces, inventaire, bonus_total):
...     print("\n===== BOUTIQUE =====")
...     print("Vous avez", pieces, "pièces\n")
... 
...     # Affichage des objets
...     for nom, infos in Objets.items():
...         print(f"{nom} - {infos['prix']} pièces (Bonus +{infos['bonus']})")
... 
...     choix = input("\nQue voulez-vous acheter ? (tape 'quitter' pour sortir) : ")
... 
...     if choix == "quitter":
...         return pieces, bonus_total
... 
...     if choix in Objets:
...         prix = Objets[choix]["prix"]
...         bonus = Objets[choix]["bonus"]
... 
...         if pieces >= prix:
...             pieces -= prix
...             inventaire.append(choix)
...             bonus_total += bonus
...             print(f"✅ {choix} acheté ! Bonus total maintenant : +{bonus_total}")
...         else:
...             print("❌ Pas assez de pièces !")
...     else:
...         print("Objet invalide.")
... 
