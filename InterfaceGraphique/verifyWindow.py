from InterfaceGraphique.mainWindow import *
from extractor.extractor import grabSudoku
from InterfaceGraphique.grid import Grid, InvalidGrid

# La classe VerifyWindow permet de créer une page dans la fenêtre tkinter identifiée par le root passé 
# en paramètre. Cette page est destinée à mettre en vis-à-vis l'image téléchargée et la grille de sudoku 
# détectée sur cette image par le réseaux de neuronnes. Le joueur doit ainsi vérifier la validité de 
# cette détection, et le cas écheant modifier les chiffres faux ou manquants (en déplaçant la case jaune).

class VerifyWindow():

    def __init__(self, root, imPath, imDisplay):
        """ Les objets tkinter à organiser sur la page sont initialisés à None pour être créés et directement
            placés dans la méthode structureWindow. """
        self.root = root                    # on reprend le root créé par la classe UploadImageWindow pour rester dans la même fenêtre
        self.globalFrame = None             # Frame englobant tous les éléments affichés sur la page VerifyWindow : destinée à être détruite afin de générer une nouvelle page dans la même fenêtre tkinter
            # Création de 2 canvas : l'un à gauche pour afficher l'image, l'autre à droite pour afficher voire modifier la grille python détectée
        self.canvasImageGrid = None
        self.canvasPythonGrid = None
        self.imPath = imPath                # Chemin d'accès à l'image choisie pour le téléchargement
        self.imDisplay = imDisplay          # Image téléchargée de type ImageTk, à placer en argument du canvas.create_image pour afficher l'image
        self.gridObject = None              # Refermera une instance de la classe Grid (permettant d'afficher et de manipuler une grille de sudoku en Python) une fois le canvas et le tableau numpy de la grille créés
        self.grid = self.getGridFromImage() # Tableau numpy de la grille détectée par le réseaux de neuronnes sur l'image
    
    def getGridFromImage(self):
        return grabSudoku(self.imPath)
        
    def structureWindow(self):
        """ Crée et place tous les widgets tkinter sur la page"""
        self.root.geometry("1000x550")  # Fixe la taille de la fenêtre en pixels pour pouvoir afficher l'intégralité des canvas
        self.globalFrame = tk.Frame(self.root)
        self.globalFrame.grid()
            # Instructions pour le joueur
        tk.Label(self.globalFrame, text="Verify that the grids match.\nChange numbers on the game grid with the yellow box if it is not the case.").grid(row=0, column=0)
            # Frame pour regrouper les deux canvas
        canvasFrame = tk.Frame(self.globalFrame)
        canvasFrame.grid(row=1, column=0)
                # Canvas avec l'image
        self.canvasImageGrid = tk.Canvas(canvasFrame, height='485', width='500')
        self.canvasImageGrid.grid(row=0, column=0)
        self.canvasImageGrid.create_image(250, 250, image=self.imDisplay)
                # Canvas avec la grille détectée + affichage de la grille par les méthodes de l'objet Grid
        self.canvasPythonGrid = tk.Canvas(canvasFrame, height='485', width='500')
        self.canvasPythonGrid.grid(row=0, column=1)
        self.gridObject = Grid(self.canvasPythonGrid, self.grid, True)
        self.gridObject.drawCanvas()
        self.gridObject.displayGrid()
        self.gridObject.displayYellowBox()
        self.gridObject.bindEvents()    # Relie les actions sur le clavier aux déplacements de la case jaune ou à l'écriture et la suppression des chiffres dans les cases
            # Bouton permettant de valider les éventuelles modifications et de lancer la partie
        buttonVerify = ttk.Button(self.globalFrame, text="The grids match. Let's play!", command=self.initGame)
        buttonVerify.grid(row=2, column=0)
    
    def initGame(self):
        """ Lance la partie si la grille est valide en créant une page MainWindow"""
        try :
            mainWindowObject = MainWindow(self.root, self.grid) # Soulèvement éventuel de l'exeption InvalidGrid si la grille présente deux fois le même chiffre sur une ligne, une colonne ou dans un bloc
            self.globalFrame.destroy()  # Destruction des éléments de la page actuelle (Label d'instructions, 2 canvas, bouton play) pour générer la page suivante
            mainWindowObject.structureWindow()
        except InvalidGrid :
                # Si la grille modifiée est invalide, une nouvelle fenêtre annexe Toplevel pop un message invitant le joueur à vérifier sa saisie
            top = tk.Toplevel(self.root)
            top.title("Invalid grid")
            tk.Label(top, text='The grid is invalid ! Please check and change the wrong numbers.').grid()



