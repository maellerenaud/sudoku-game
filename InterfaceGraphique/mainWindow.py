import tkinter as tk
from tkinter import ttk
from InterfaceGraphique.grid import Grid

# La classe MainWindow permet de créer une page dans la fenêtre tkinter identifiée par le root passé 
# en paramètre. Cette page est destinée à afficher une grille de jeu que le joueur peut tenter de résoudre.
# Des indications (difficulté de la grille, nombre d'indices restants) sont affichées. Des boutons ajoutent
# de nouvelles fonctionnalités : vérifier la validité des cases devinées par le joueur par rapport à la grille
# résolue, révéler une case inconnue, afficher la grille complète, recommencer la pertie, afficher les règles
# du jeu.

class MainWindow():

    def __init__(self, root, grid):
        self.root = root    # on reprend le root créé par la classe UploadImageWindow pour rester dans la même fenêtre
        self.canvas = tk.Canvas(self.root, height='485', width='500')
        self.gridObject = Grid(self.canvas, grid, False)    # Instance de la classe Grid (permettant d'afficher et de manipuler une grille de sudoku)
        self.labelTitle = None                              # Titre affiché en haut de la page
        self.labelHintLeft = None                           # Champ permettant d'afficher le nombre d'indices restants

    def structureWindow(self):
        self.root.geometry("500x550")   # Fixe la taille de la fenêtre en pixels pour pouvoir afficher l'intégralité du canvas
            # Frame regroupant les informations au dessus de la grille
        frameTop = tk.Frame(self.root)
        frameTop.grid(row=0, column=0)
        self.labelTitle = tk.Label(frameTop, text='Solve the sudoku !')
        self.labelTitle.grid(row=0, column=1)
        tk.Label(frameTop, text='Difficulty : ' + self.gridObject.difficulty, width='18', anchor='w').grid(row=0, column=0) # Affichage de la difficulté de la grille
        self.labelHintLeft = tk.Label(frameTop, text='You have '+ str(self.gridObject.nbHintLeft) +' hints left.', width='18', anchor='e')
        self.labelHintLeft.grid(row=0, column=2)
            # Canvas au centre de la page permettant d'afficher la grille (objet self.gridObject de la classe Grid)
        self.canvas.grid(row=1, column=0, sticky='ew')
        self.gridObject.drawCanvas()
        self.gridObject.displayGrid()
        self.gridObject.displayYellowBox()
        self.gridObject.bindEvents()
            # Frame regroupant tous les boutons : Check, Hint, Solve, Restart, Help
        frameButtons = tk.Frame(self.root)
        frameButtons.grid(row=2, column=0)
        buttonCheck = ttk.Button(frameButtons, text="Check", command=self.check)
        buttonCheck.grid(row=0, column=0)
        buttonHint = ttk.Button(frameButtons, text="Hint", command=self.hint)
        buttonHint.grid(row=0, column=1)
        buttonSolve = ttk.Button(frameButtons, text="Solve", command=self.solve)
        buttonSolve.grid(row=0, column=2)
        buttonRestart = ttk.Button(frameButtons, text="Restart", command=self.restart)
        buttonRestart.grid(row=0, column=3)
        buttonHelp = ttk.Button(frameButtons, text="Help", command=self.help)
        buttonHelp.grid(row=0, column=4)
        
    def check(self):
        """ Affiche les cases remplies par le joueur en vert ou rouge selon qu'elles correspondent ou non à la grille résolue"""
        for i in range(self.gridObject.sizeGrid):
            for j in range(self.gridObject.sizeGrid):
                if not(self.gridObject.inGridInit[i,j]) :
                    if self.gridObject.grid[i,j] == self.gridObject.solvedGrid[i,j] :
                        self.gridObject.nbColors[i][j] = 'green'
                    else:
                        self.gridObject.nbColors[i][j] = 'red'
        self.gridObject.displayGrid()
            # Affichage d'un message de félicitations si la grille est résolue
        if (self.gridObject.grid == self.gridObject.solvedGrid).all():
            self.labelTitle.config(text='Congratulations ! You solved it !')

    def hint(self):
        """ La valeur de la case jeune est révélée seulement si ce n'est pas une case de la grille de départ
        ou une case que le joueur a déjà correctement devinée et s'il reste des indices au joueur"""
        i = self.gridObject.iYellowBox
        j = self.gridObject.jYellowBox
        if self.gridObject.nbHintLeft > 0 and not(self.gridObject.inGridInit[i,j]) and self.gridObject.grid[i,j] != self.gridObject.solvedGrid[i,j] :
            self.gridObject.grid[i,j] = self.gridObject.solvedGrid[i,j]
            self.gridObject.nbColors[i][j] = 'green' # Affichage des cases indices en vert
            self.gridObject.displayGrid()
            self.gridObject.nbHintLeft -= 1
                # Mise à jour de l'affichage du nombre d'indices restants
            if self.gridObject.nbHintLeft == 1 or self.gridObject.nbHintLeft == 0 : 
                self.labelHintLeft.config(text='You have '+ str(self.gridObject.nbHintLeft) +' hint left.')
            else : 
                self.labelHintLeft.config(text='You have '+ str(self.gridObject.nbHintLeft) +' hints left.')
            # Si le joueur tente de révéler une case non devinée alors qu'il n'a plus d'indices, un message s'affiche dans une fenêtre annexe pour lui indiquer qu'il n'a plus d'indices
        elif self.gridObject.nbHintLeft == 0 and not(self.gridObject.inGridInit[i,j]) and self.gridObject.grid[i,j] != self.gridObject.solvedGrid[i,j] :
            top = tk.Toplevel(self.root)
            tk.Label(top, text="You don't have any hints left").grid()
    
    def solve(self):
        for i in range(self.gridObject.sizeGrid):
            for j in range(self.gridObject.sizeGrid):
                if self.gridObject.grid[i,j] == 0 or self.gridObject.grid[i,j] != self.gridObject.solvedGrid[i,j] :
                    self.gridObject.nbColors[i][j] = 'red' # Gestion du cas où on a fait un check juste avant, affichage de toutes les cases non devinées en rouge
        self.gridObject.grid = self.gridObject.solvedGrid
        self.gridObject.displayGrid()
    
    def restart(self):
            # Réinitialisation des cases non présentes dans la grille initiale à 0
        for i in range(self.gridObject.sizeGrid):
            for j in range(self.gridObject.sizeGrid):
                if not(self.gridObject.inGridInit[i,j]):
                    self.gridObject.grid[i,j] = 0
            # Génération d'une nouvelle instance de la classe Grid
        self.gridObject = Grid(self.canvas, self.gridObject.grid, False)
            # Affichage et commandes liés à cette nouvelle instance
        self.gridObject.drawCanvas()
        self.gridObject.displayGrid()
        self.gridObject.displayYellowBox()
        self.gridObject.bindEvents()
            # Mise à jour de l'affichage du nombre d'indices restants
        self.labelHintLeft.config(text='You have '+ str(self.gridObject.nbHintLeft) +' hints left.')
    
    def help(self):
        """ Affiche les règles du jeu et l'usage des boutons dans une fenêtre annexe Toplevel"""
        top = tk.Toplevel(self.root)
        top.title("Help")
        tk.Label(top, justify='left', text="""You must complete the grid without twice the same number in a line, a column or a block.
        \nMove the yellow box with the arrows of your keyboard to select a box.
        \nTyping a number on your keyboard will write it on the yellow box, if it is not on a box from the initial grid.
        \nPressing the return key will erase the number in the yellow box, if it is not a number from the initial grid.
        \n
        \nCheck : Click on the check button to check your guesses. The correct numbers are green, the false numbers are red.
        \nHint : Place the yellow box on the box you want to reveal and click on the hint button to reveal the correct number.
        \nSolve : Click on the solve button to reveal the entire grid.
        \n Restart : Click on the restart button to restart a game with the current grid.""").grid()

