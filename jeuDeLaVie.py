#################### - Le Jeu De La Vie - ####################

'''
Ce jeu de la vie est aléatoire (on ne place pas les cellules à la souris).

Néanmoins, afin de ne pas etre limité par le cadre, j'utilise ici
un tableau torique. Cela permet par exemple qu'une structure mouvante partant vers l'extreme
droite se retrouvera à gauche pour continuer son mouvement (idéal pour étudier les planeurs)

On a donc les entrées de la hauteur et de la largeur au début

Une fois les valeurs entrées, on a donc l'interface qui montre la table avec les cellules mortes et vivantes évoluant dans l'environnement.
On pourra avoir plusieurs résultats comme des structures stables (un carré de 2x2 cellules) ou instables (comme le clignotant ou le planeur,
un peu plus complexe).

Ici, on utilise l'interface intégrée tkinter, parce que dans ce TP/Projet, les librairies externes ne sont pas autorisées. On n'utilisera donc pas
pygame, et de toute façon il ne serait pas très efficace pour le jeu de la vie.

Le programme est commenté et trié, n'utilisant donc pas de variables globales, et utilisant des raccourcis Python mineurs (notamment
pour la création des matrices) afin d'atténuer la longueur du code.

On a en premier les deux importations, puis toutes les définitions des fonctions et procédures, pour enfin finir par le "MAIN", ou juste la partie
principale où l'on trouve les appels de fonctions.
'''

#Importations de tkinter pour l'interface et de random (ici on veut juste randrange) pour l'aléatoire
from tkinter import *
import random
from random import randrange

########## - FONCTIONS ET PROCEDURES - ##########
NEGATIF = 3
POSITIF = 2  # L'état vivant est définit à 1 (comme le binaire, en "True")
NEUTRE = 1  # L'état mort est définit à 0 (comme en binaire, en "False")
AUCUN = 0

#Calcule et dessine le nouveau tableau
def tableau():
    calculer()
    draw()
    window.after(1, tableau)

#Initialisation
def initialisation():
    for y in range(hauteur):
        for x in range(largeur):
            #on met les cellules mortes d'abord, et la variable temporaire à morte aussi.
            state[x][y] = AUCUN
            temp[x][y] = AUCUN
            cellule[x][y] = canvas.create_rectangle((x*cote, y*cote,(x+1)*cote, (y+1)*cote), outline="gray", fill="white") #création des rectangles blancs

    #On placeau hasard environ 25% de cellules en vie (permet d'éviter qu'il n'y aie qu'1 seule cellule, et donc de ne rien produire)
    # for i in range(1):
    #     state[randrange(largeur)][randrange(hauteur)] = NEGATIF

    # for i in range(1):
    #     state[randrange(largeur)][randrange(hauteur)] = POSITIF

    for i in range(1):
        state[randrange(largeur)][randrange(hauteur)] = NEUTRE


#On applique les règles
def calculer():
    for y in range(hauteur):
        for x in range(largeur):
            direction = random.randint(1,4)#Droite
            if state[x][y] == NEUTRE:
                match direction:
                    case 1:
                        #Droite
                        if x < largeur-1:
                            state[x+1][y] = NEUTRE
                            state[x][y]=AUCUN
                    case 2:
                        if y < hauteur-1:
                            state[x][y+1] = NEUTRE
                            state[x][y] = AUCUN
                    case 3:
                        # Gauche
                        state[x-1][y] = NEUTRE
                        state[x][y] = AUCUN
                    case 4:
                        state[x][y-1] = NEUTRE
                        state[x][y] = AUCUN
                


    # # BAS
    # state[1][1] = POSITIF
    # state[1][0] = AUCUN

    # #Déplacement à gauche
    # state[0][1] = NEGATIF
    # state[1][1] = AUCUN

    # # Deplacement HAUT
    # state[0][0] = NEGATIF
    # state[0][1] = AUCUN

    # for y in range(hauteur):
    #     for x in range(largeur):
    #         deplacementValue =random.randint(1,4) #on appelle la fonction permettant de connaître le nombre de voisins
    #         DROITE = 1
    #         BAS = 2
    #         GAUCHE = 3
    #         HAUT = 4
    #         state[x-1][y] = AUCUN
    #         temp[x][y] = POSITIF
            # match 1:
            #     case 1:
            #         state[x-1][y] = AUCUN
            #         temp[x][y] = POSITIF
            #     case 2:
            #         state[x][y-1] = AUCUN
            #         temp[x][y] = POSITIF
                # case 3:
                #     if(state[x+1]):
                #         state[x+1][y] = AUCUN
                #         temp[x][y] = POSITIF
                # case 4:
                #     state[x][y+1] = AUCUN
                #     temp[x][y] = POSITIF

            # if state[x-1][y] == POSITIF:
            #     state[x][y] = AUCUN
            # else:
            #     state[x][y] == POSITIF


    # for y in range(hauteur):
    #     for x in range(largeur):
    #         if state[(x - 1) % largeur][(y) % hauteur] == 1:
    #             state[x][y] = temp[x][y] #l'état prend la valeur de la variable temporaire, définis par les tests des quatre règles ci-dessus



#On compte les voisins en vie (tableau torique, voir plus haut)
def compte_voisins(x,y):
    nombre_voisins = 0 #compteur du nombre de voisins à 0

    #on teste si chaque cellule à un voisin selon les 8 directions

    #diagonale haut-gauche
    if state[(x-1)%largeur][(y+1)%hauteur] == 1:
        nombre_voisins += 1

    #haut
    if state[x][(y+1)%hauteur] == 1:
        nombre_voisins += 1

    #Diagonale haut-droite
    if state[(x+1)%largeur][(y+1)%hauteur] == 1:
        nombre_voisins += 1

    #gauche
    if state[(x-1)%largeur][y] == 1:
        nombre_voisins += 1

    #droite
    if state[(x+1)%largeur][y] == 1:
        nombre_voisins += 1

    #Diagonale bas-gauche
    if state[(x-1)%largeur][(y-1)%hauteur] == 1:
        nombre_voisins += 1

    #bas
    if state[x][(y-1)%hauteur] == 1:
        nombre_voisins += 1

    #diagonale bas-droite
    if state[(x+1)%largeur][(y-1)%hauteur] == 1:
        nombre_voisins += 1

    return nombre_voisins #on retourne la valeur du nombre de voisins

#On dessine toute les cellules
def draw():
    couleur = "white"
    for y in range(hauteur):
        for x in range(largeur):
            match state[x][y]:
                case 0:
                    couleur = "white"
                case 1:
                    couleur = "black"
                case 2:
                    couleur = "green"
                case 3:
                    couleur = "red"
            canvas.itemconfig(cellule[x][y], fill=couleur) #application du changement de couleur

########## - MAIN - ##########

#Définitions des variables
# hauteur = int(input("Entrez le nombre de cellules à la verticale : ")) #Hauteur du tableau (fait donc varier le nombre de cellules à la verticale, plus il y en a, plus c'est lent)
# largeur = int(input("Entrez le nombre de cellules à l'horizontale : ")) #Largeur du tableau (fait donc varier le nombre de cellules à l'horizontale, plus il y en a, plus c'est lent)
hauteur = 50
largeur = 50
cote = 10  #Taille d'une cellule (fixe, car il ne sert à rien de la modifier)


#Créer les matrices
cellule = [[0 for row in range(hauteur)] for col in range(largeur)] #utilisation des raccourcis python (non obligatoire mais pratique)
state = [[NEUTRE for row in range(hauteur)] for col in range(largeur)]
temp = [[NEUTRE for row in range(hauteur)] for col in range(largeur)]


#Rassemblement des fonctions et procédures pour faire le programme
window = Tk()
window.title("Jeu de la vie")
canvas = Canvas(window, width=cote*largeur, height=cote*hauteur, highlightthickness=0)
canvas.pack()

initialisation()
tableau()

window.mainloop()
