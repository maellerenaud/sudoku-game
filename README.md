### Lancement du fichier executable
Télécharger le fichier play suduko.zip 

Puis le dézipper.

Lancer le fichier play.exe dans le dossier dézippé. La fenêtre de résolution s'ouvre alors.

### Introduction de la grille à résoudre
Cliquer sur upload.

Selectionner la photo du sudoku à résoudre.

### Vérification de la reconnaissance de la grille
Si la photo est de basse qualité, l'algorithme de reconnaissance peut faire des erreurs.
C'est pourquoi il est demandé de vérifier que la grille affichée est bien celle de la photo.
Si la valeur d'une grille n'est pas celle de la photo, placer la case jaune sur cette case et entrer le bon chiffre (celui de la photo).

Faites ceci pour toutes les cases fausses, puis cliquer sur "It matches".

Une fenêtre de jeu s'ouvre alors.

### Interface de jeu

La fenêtre suivante s'ouvre :

![CaptureEcranInterfaceGraphique](https://user-images.githubusercontent.com/58704043/111867708-1405c200-8976-11eb-9df5-f840478f05b6.png)

La difficulté de la grille va de "easy" à "ultrahard". Elle est basée sur le nombre de case laissée vide. Plus il y a de cases vides, plus c'est difficile. 

Ce n'est pas le seul critère de difficulté, mais c'est le seul que nous prenons en compte içi.
Pour jouer, il y a 7 commandes possibles.

**Pour remplir une case** : déplacer la case jaune avec les flèches directionnelles sur la case à remplir, puis entrer le chiffre (entre 1 et 9) voulu.

**Pour supprimer le contenu d'une case** : déplacer la case jaune avec les flèches directionnelles sur la case à remplir, puis appuyer sur la touche retour.

**Pour vérifier la valeur des cases rentrées par le joueur** : cliquer sur "check" : les chiffres deviennent verts s'ils sont bons, rouges sinon.

**Pour avoir un indice** : déplacer la case jaune avec les flèches directionnelles sur la case à afficher, puis appuyer sur le bouton "Hint". Si le chiffre avait été bien deviné par le joueur, cette action ne consomme par d'indice.

**Pour avoir la grille solution entière** : appuyer sur "Solve".

**Pour afficher la grille de départ** : appuyer sur "Restart" : la partie commence.

**Pour avoir de l'aide sur les règles du jeu ou le fonctionnement des boutons** : cliquer sur "Help".

