from tkinter import filedialog
from PIL import Image, ImageTk
from InterfaceGraphique.verifyWindow import *

# La classe UploadImageWindow permet de générer l'ouverture d'une fenêtre tkinter destinée à télécharger 
# une image de grille de sudoku sauvegardée sur l'ordinateur.


class UploadImageWindow():

    def __init__(self):
        """ Les objets tkinter à organiser sur la page sont initialisés à None pour être créés et directement
            placés dans la méthode structureWindow. """
        self.root = tk.Tk()     # Génération et ouverture de la fenêtre tkinter
        self.globalFrame = None # Frame englobant tous les éléments affichés sur la page UploadImageWindow : destinée à être détruite afin de générer une nouvelle page dans la même fenêtre tkinter
        self.canvas = None
        self.imPath = None      # Chemin d'accès à l'image choisie pour le téléchargement
        self.imDisplay = None   # Image téléchargée de type ImageTk, à placer en argument du canvas.create_image pour afficher l'image
        
    def structureWindow(self):
        self.root.title("Sudoku")
        self.root.geometry("500x550")   # Fixe la taille de la fenêtre en pixels pour pouvoir afficher l'intégralité du canvas
        self.globalFrame = tk.Frame(self.root)
        self.globalFrame.grid()
        buttonUpload = ttk.Button(self.globalFrame, text='Upload your grid', command=self.upload)
        buttonUpload.grid(row=0, column=0)
        self.canvas = tk.Canvas(self.globalFrame, height='485', width='500')
        self.canvas.grid(row=1, column=0)

    def upload(self):
        self.imPath = filedialog.askopenfilename(filetypes=[('jpg files', '.jpg'), ('png files', '.png')])  # Ouverture d'un explorateur de fichiers et sauvegarde du chemin du fichier sélectionné
        imObject = Image.open(self.imPath)  # Objet de type Image, devant être appelé pour adapter la taille de l'image affichée (ligne suivante)
        imObject = imObject.resize((490,490), Image.ANTIALIAS)
        self.imDisplay = ImageTk.PhotoImage(imObject)
        self.canvas.create_image(250, 250, image=self.imDisplay)
        buttonContinue = ttk.Button(self.globalFrame, text='Continue with this grid', command=self.verify)
        buttonContinue.grid(row=2, column=0)
    
    def verify(self):
        self.globalFrame.destroy()  # Destruction des éléments de la page actuelle (bouton upload, canvas affichant l'image, bouton continue) pour générer la page suivante
        w = VerifyWindow(self.root, self.imPath, self.imDisplay)
        w.structureWindow() # Affichage de la page suivante dans la fenêtre tkinter, objet VerifyWindow


