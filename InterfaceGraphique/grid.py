import numpy as np
from math import sqrt
from Résolution import *

# La class InvalidGrid est une exeption soulevée si la grille présente deux fois le même chiffre 
# sur une ligne, une colonne ou dans un bloc. L'execption est répercutée dans la page VerifyWindow
# qui affiche alors un message d'erreur.

class InvalidGrid(Exception):
    pass


# La class Grid permet de gérer et d'afficher une grille de jeu. Elle est utilisée dans les pages
# VerifyWindow et MainWindow avec des spécificités contrôlées par l'attribut inVerifyWindow.
# Une case est affichée en jaune : le joueur peut la déplacer avec les flèches du clavier, y insérer
# un chiffre en le tapant ou supprimer un chiffre déjà présent en appuyant sur retour.

class Grid():

    def __init__(self, canvas, grid, inVerifyWindow):
        self.canvas = canvas                            # La grille est dessinée dans un canvas déjà créé pour mieux l'intégrer dans n'importe quelle page
        self.grid = grid                                # Tableau numpy des chiffres de la grille
        self.inVerifyWindow = inVerifyWindow            # Booléen indiquant si la grille se trouve dans la page VerifyWindow ou non
        self.difficulty = difficulte_sudoku(self.grid)  # Difficulté de la grille calculée à partir du nombre de cases à remplir
        self.sizeGrid = np.shape(self.grid)[0]
        self.inGridInit = self.calculateInGridInit()    # Tableau numpy de booléen : self.inGridInit[i,j] vaut True si la case [i,j] est déjà remplie dans la grille de jeu initiale
        self.nbColors = self.initNbColors()             # ! Liste de listes ! : self.nbColors[i,j] indique la couleur avec laquelle on doit écrire le nombre de la case [i,j]
        self.solvedGrid = self.calculateSolvedGrid()    # Grille résolue par le module Résolution
        self.idBoxes = []                               # Identifiants des cases pour changer éventuellement leur couleur au fil du jeu
        self.idTexts = []                               # Identifiants des textes dans les cases pour les actualiser au fil du jeu
        self.iYellowBox = 0                             # Indice de ligne de la case de sélection jaune
        self.jYellowBox = 0                             # Indice de colonne de la case de sélection jaune
        self.nbHintLeft = 5                             # Nombre d'indices (révélation d'une case inconnue) auxquels le joueur a le droit

    def calculateSolvedGrid(self):
        if self.inVerifyWindow:
            return None         # Pas besoin de calculer la grille résolue et ça fait planter le programme si la grille détectée est fausse et n'a pas de solution
        elif verify(self.grid): # Vérification si la grille est valide
            return resolution(np.copy(self.grid))   # Modifications par effets de bord donc nécessité de faire une copie de la grille
        else:
            raise InvalidGrid

    def calculateInGridInit(self):
        return self.grid != [[0]*self.sizeGrid]*self.sizeGrid # Si une case vaut 0 (case vide) à la création de l'objet Grid, elle n'est pas dans la grille initiale

    def initNbColors(self):
        if self.inVerifyWindow:
            # La grille initiale est affichée en noir. Dans la page inVerifyWindow, on vérifie la grille initiale donc toutes les modifications de chiffres sont écrites en noir.
            nbColors = [['black']*self.sizeGrid]*self.sizeGrid
        else:
            # On ne peut pas copier directement la grille, sinon les éléments ne sont pas indépendants
            lineNbColors = ['gray' for _ in range(self.sizeGrid)]
            nbColors = [ lineNbColors.copy() for _ in range(self.sizeGrid)]
            for i in range(self.sizeGrid):
                for j in range(self.sizeGrid):
                    if self.inGridInit[i,j]:    # Les chiffres de la grille initiale sont en noir, ceux rajoutés par le joueur pendant la partie restent en gris
                        nbColors[i][j] = 'black'
        return nbColors
    
    def drawCanvas(self):
        """ Dessine la grille en créant et affichant dans le canvas chaque case, pour le moment vide. """
            # Quadrillage interne, bordures des cases
        sizeBox = 450 / self.sizeGrid   # La grille est un carré de 450 pixels de côté.
        for i in range(self.sizeGrid):
            for j in range(self.sizeGrid):
                x0, y0 = j * sizeBox + 25, i * sizeBox + 15     # Décalage de la grille par rapport au bord du canvas
                x1, y1 = x0 + sizeBox , y0 + sizeBox
                box = self.canvas.create_rectangle((x0, y0), (x1, y1), outline='black', width=2)
                text = self.canvas.create_text(x0 + sizeBox/2, y0 + sizeBox/2, text='', fill='black', font=('Arial', '20', 'bold'))
                self.idBoxes.append(box)
                self.idTexts.append(text)
            # Bordures des blocs
        nbBlocks = int(sqrt(self.sizeGrid)) # La grille n = b² cases et b blocs de b cases sur chaque ligne et chaque colonne
                # 3 grands rectangles colonnes pour faires les bordures gauches et droites des blocs
        for j in range(nbBlocks):
            x0, y0 = j * nbBlocks * sizeBox + 25, 15    # Un bloc contient b cases, donc sa taille est nbBlocks * sizeBox
            x1, y1 = x0 + nbBlocks * sizeBox, self.sizeGrid * sizeBox + y0
            self.canvas.create_rectangle((x0, y0), (x1, y1), outline='black', width=4)
                # 3 grands rectangles lignes pour faires les bordures hautes et basses des blocs
        for i in range(nbBlocks):
            x0, y0 =25, i * nbBlocks * sizeBox + 15
            x1, y1 = self.sizeGrid * sizeBox + x0, y0 + nbBlocks * sizeBox
            self.canvas.create_rectangle((x0, y0), (x1, y1), outline='black', width=4)
    
    def displayGrid(self):
        """ Recopie tous les chiffres d'une grille dans les cases grâce aux self.idTexts, en utilisant les bonnes couleurs"""
        for i in range(self.sizeGrid):
            for j in range(self.sizeGrid):
                if self.grid[i,j] != 0:
                    self.canvas.itemconfig(self.idTexts[self.sizeGrid*i+j], text=self.grid[i,j], fill=self.nbColors[i][j])
                else:
                    self.canvas.itemconfig(self.idTexts[self.sizeGrid*i+j], text='')    # Une case contenant la valeur 0 est affichée vide
    
    def displayYellowBox(self):
        """ Affiche la case de sélecion en jaune et les autres en blanc ou en jaune très clair"""
        for i in range(self.sizeGrid):
            for j in range(self.sizeGrid):
                if i == self.iYellowBox or j == self.jYellowBox :   # Une case dans la ligne ou la colonne de la case jaune est légèrement colorée pour aider le joueur
                    self.canvas.itemconfig(self.idBoxes[self.sizeGrid * i + j], fill='#FCFAE1')
                else:
                    self.canvas.itemconfig(self.idBoxes[self.sizeGrid * i + j], fill='white')
        self.canvas.itemconfig(self.idBoxes[self.sizeGrid * self.iYellowBox + self.jYellowBox], fill='Yellow')

    def bindEvents(self):
        """ Relie toutes les actions sur le clavier à des actiosn sur la grille. """
            # Déplacements de la case jaune avec les flèches du clavier
        self.canvas.bind_all('<KeyPress-Left>', self.moveYellowBox)
        self.canvas.bind_all('<KeyPress-Right>', self.moveYellowBox)
        self.canvas.bind_all('<KeyPress-Up>', self.moveYellowBox)
        self.canvas.bind_all('<KeyPress-Down>', self.moveYellowBox)
            # Ecriture d'un nombre dans la case jaune
        for nb in range(1,10):
            self.canvas.bind_all('<KeyPress-' + str(nb) + '>', self.writeNbInYellowBox)
            # Suppression d'un nombre dans la case jaune
        self.canvas.bind_all('<KeyPress-BackSpace>', self.deleteNbInYellowBox)
    
    def moveYellowBox(self, event):
        """ Récupère la flèche sur laquelle le joueur a appuyé pour enregistrer le déplacement puis l'afficher"""
        if event.keysym == 'Up' and self.iYellowBox > 0:
            self.iYellowBox -= 1
        elif event.keysym == 'Down' and self.iYellowBox < self.sizeGrid - 1:
            self.iYellowBox += 1
        elif event.keysym == 'Left' and self.jYellowBox > 0:
            self.jYellowBox -= 1
        elif event.keysym == 'Right' and self.jYellowBox < self.sizeGrid - 1:
            self.jYellowBox += 1
        self.displayYellowBox()

    def writeNbInYellowBox(self, event):
        if self.inVerifyWindow:     # Dans la page VerifyWindow, le joueur peut modifier toutes les cases
            self.grid[self.iYellowBox, self.jYellowBox] = int(event.char)
            self.displayGrid()
        elif not(self.inGridInit[self.iYellowBox, self.jYellowBox]):    # Dans la page MainWindow, le joueur ne peut modifier que les cases qui ne sont pas dans la grille initiale
            self.grid[self.iYellowBox, self.jYellowBox] = int(event.char)
            self.nbColors[self.iYellowBox][self.jYellowBox] = 'gray'    # Gère le cas où la case a été affichée en vert ou rouge par un check et qu'on modifie sa valeur
            self.displayGrid()
    
    def deleteNbInYellowBox(self, event):
        if self.inVerifyWindow:     # Dans la page VerifyWindow, le joueur peut modifier toutes les cases
            self.grid[self.iYellowBox, self.jYellowBox] = 0
            self.displayGrid()
        elif not(self.inGridInit[self.iYellowBox, self.jYellowBox]):    # Dans la page MainWindow, le joueur ne peut modifier que les cases qui ne sont pas dans la grille initiale
            self.grid[self.iYellowBox, self.jYellowBox] = 0
            self.nbColors[self.iYellowBox][self.jYellowBox] = 'gray'
            self.displayGrid()
