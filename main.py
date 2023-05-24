import random

nb_portes = 3 # Nombre de portes dans le jeu
nb_jeux = 10000 # Nombre de jeux à effectuer
aleatoire_presentateur = True # Le présentateur choisit-il aléatoirement la porte à ouvrir ?
joueur_change = True # Le joueur change-t-il de porte après que le présentateur ait ouvert une porte ?

# Créer le tableau de portes
def init_portes(nb_portes):
    portes = []
    for i in range(nb_portes):
        portes.append(i+1)
    return portes

def init_porte_gagnante(nb_portes):
    return random.randint(1,nb_portes)

def choix_joueur(portes_restantes):
    return random.choice(portes_restantes)

def choix_presentateur(portes_restantes, porte_gagnante, choix_joueur, aleatoire_presentateur):
    if aleatoire_presentateur:
        while True: # La porte peut être la porte gagnante
            choix = random.choice(portes_restantes)
            if choix != choix_joueur:
                return choix
    else:
        while True:
            choix = random.choice(portes_restantes)
            if choix != porte_gagnante and choix != choix_joueur:
                return choix

def jeu(nb_portes, nb_jeux, joueur_change, aleatoire_presentateur):
    defaites = 0
    victoires = 0
    for i in range(nb_jeux):
        portes = init_portes(nb_portes)
        porte_gagnante = init_porte_gagnante(nb_portes)
        choix = choix_joueur(portes)
        presentateur = choix_presentateur(portes, porte_gagnante, choix, aleatoire_presentateur)
        if presentateur == porte_gagnante:
            defaites += 1
            continue
        if joueur_change:
            portes.remove(presentateur) # On enlève la porte choisie par le présentateur puisqu'on considère que la porte choisie par le présentateur est une défaite au jeu
            choix = choix_joueur(portes) # Le joueur choisit à nouveau une porte
        if choix == porte_gagnante:
            victoires += 1
        else:
            defaites += 1
    print("\t> Défaites : " + str(defaites) + " (" + str(round(defaites/(defaites+victoires)*100,2)) + "%)")
    print("\t> Victoires : " + str(victoires) + " (" + str(round(victoires/(defaites+victoires)*100,2)) + "%))")

# Programme principal
print("Nombre de jeux : " + str(nb_jeux) + " - Nombre de portes : " + str(nb_portes))
print("\nJeu sans changement de porte et sans choix aléatoire du présentateur :")
jeu(nb_portes, nb_jeux, False, False)
print("\nJeu avec changement de porte et sans choix aléatoire du présentateur :")
jeu(nb_portes, nb_jeux, True, False)
print("\nJeu sans changement de porte et avec choix aléatoire du présentateur :")
jeu(nb_portes, nb_jeux, False, True)
print("\nJeu avec changement de porte et avec choix aléatoire du présentateur :")
jeu(nb_portes, nb_jeux, True, True)