# La fonction à créer est une fonction prenant en entrée un  tableau de taille 9*9
# cE tableau est rempli d'entiers entre 0 et 9
# 0 représente une case vide alors que les entiers 1 à 9 représente la valeur d'une case.
import numpy as np
import random
# cette fonction renvoie un résultat cohérent seulemnt lorsque la case à cette endroit est vide

#L=[ [ random.randint ( 0,9) for i in range (9) ] for j in range (9)]
#print (np.array(L))
Testlist=[ [ 0,0,0,4,0,0,8,7,0] ,[ 0,4,7,0,9,2,0,5,0], [2,0,0,6,0,0,0,3,0],[9,7,0,5,0,0,2,7,3] ,[5,0,8,0,2,4,7,0,6],[6,0,4,0,0,7,0,8,5],[0,9,0,3,0,8,0,0,7],[0,0,3,2,4,0,1,6,0],[0,1,2,0,0,0,0,9,0]]
Testnp = np.array(Testlist)

# ce tableau est un tableau
testfinal=[[0,1,0,0,2,5,0,7,0],[0,0,5,0,1,7,0,6,9],[7,8,9,0,3,0,0,0,0],[0,5,0,0,0,0,0,0,0],[0,6,3,1,9,2,7,4,5],[0,0,0,0,0,6,1,3,2],[0,0,1,0,7,0,0,5,0],[2,0,0,0,5,1,9,8,7],[5,0,8,3,0,0,2,1,0]]


T=np.array(testfinal)


def nombreDePossibilite(tableau,ligne,colonne):
    "cette fonction prend en entrée un tableau et des coordonnées d'une case vide, cela permet de calculer le nombre de valeur possible pour cette case"
    Liste_possible=[ i for i in range (1,10)]
    'cette liste est une liste des entiers de 1 à 9 et va être modifié en remplaçant par un 0, l entier qui ne peut pas être sur la case voulu '
    for i in range (9):
        x=tableau[i,colonne]
        if x!=0:
            Liste_possible[x-1]=0
    'cette étape nous permet de tester toutes les valeurs sur la colonne'
    for j in range(9):
        x=tableau[ligne,j]
        if x!= 0 :
            Liste_possible[x-1]=0
    'cette étape nous permet de tester toutes les valeurs sur la ligne'
    positionL= ligne%3
    positionC= colonne%3
    'on veut donc maintenant tester la boite de 3*3 dans laquelle la cases vides se trouve'
    'Il faut pour cela regarder ou se situe la case par rapport à la boite'
    'La congruence par rapport à 3 nous permet de '
    if positionL== 0 :
        if positionC==0:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==1:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==2:
            x=tableau[ligne+1,colonne-1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne-2]
            if x!= 0 :
                Liste_possible[x]=0
    if positionL == 1 :
        if positionC==0:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==1:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==2:
            x=tableau[ligne-1,colonne-1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
    if positionL==2:
        if positionC==0:
            x=tableau[ligne-2,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==1:
            x=tableau[ligne-2,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==2:
            x=tableau[ligne-1,colonne-1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
    return  9 - Liste_possible.count(0)


def ordreRemplissage(tableau):
    "cette fonction prend en entrée un tableau et renvoie une liste des coordonées de toutes les box vides classées dans l'ordre des priorités "
    L=[ [] for j in range(9)]

    for i in range (9):
        for j in range(9):
            if tableau[i,j]== 0:
                x= nombreDePossibilite (tableau,i,j)

                L[x-1].append( [i,j] )
    Ordre= []
    for i in range (9):
        Ordre+=L[i]
    return Ordre




def Liste_Valeur(tableau,box):
    "cette fonction prend en entrée un tableau et une liste [i,j] de coordonées et renvoie les valeurs possibles pour cette box"
    ligne= box[0]
    colonne=box[1]
    Liste_possible=[ i for i in range (1,10)]

    for i in range (9):
        x=tableau[i,colonne]
        if x!=0 and i!=ligne:
            Liste_possible[x-1]=0
    for j in range(9):
        x=tableau[ligne,j]
        if x!= 0 and j!=colonne :
            Liste_possible[x-1]=0
    positionL= ligne%3
    positionC= colonne%3
    if positionL== 0 :
        if positionC==0:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==1:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==2:
            x=tableau[ligne+1,colonne-1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+2,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
    if positionL == 1 :
        if positionC==0:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==1:
            x=tableau[ligne+1,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==2:
            x=tableau[ligne-1,colonne-1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne+1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
    if positionL==2:
        if positionC==0:
            x=tableau[ligne-2,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+2]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==1:
            x=tableau[ligne-2,colonne+1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne+1]
            if x!= 0 :
                Liste_possible[x-1]=0
        if positionC==2:
            x=tableau[ligne-1,colonne-1]
            if x != 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-1,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne-1]
            if x!= 0 :
                Liste_possible[x-1]=0
            x=tableau[ligne-2,colonne-2]
            if x!= 0 :
                Liste_possible[x-1]=0
    return SupprimerZero(Liste_possible)

def SupprimerZero(L):
    """
    SupprimerZero(L) permet de supprimer les zeros d'une liste L
    """
    while 0 in L:#tant que il existe un 0 dans la liste L
        L.remove(0) #supprimer la valeur 0
        #L.remove(val) génére une exception si la valeur val n'existe pas dans la liste L

    return L
def test(tableau,ligne,colonne,chiffre):
    "cette fonction prend en entrée le tableau modifié, une box que l'ont a rempli avec une valeur, elle renvoie alors true si le chiffre est impossible et false sinon"
    
    return chiffre in Liste_Valeur(tableau,[ligne,colonne])

def resolution(tableau):
    'cette fonction prend en argument le tableau en numpy coorespondant au sudoku à résoudre'
    'Il renvoie une des solutions possibles sous forme de tableau ayant le même format'
    ordre= ordreRemplissage(tableau)
    'ordre est une liste contenant les coordonées des cases vides classées par ordre de priorité'

    compteur = [ 0 for box in ordre]
    'compteur est une liste de la même taille que la liste ordre, elle stocke les valeurs attribué à chaque cases vides'

    i=0
    'i est l indice de backtracking'
    compteurFinal = [9 for box in ordre]
    while compteur != compteurFinal and (0 in tableau) :
        ' tant que le tableau n est pas résolu on continue la boucle'
        compteur[i]+=1
        ' on impose à la ième case d essayer le chiffre suivant'
        while not(test(tableau,ordre [i][0],ordre[i][1],compteur[i] )) and compteur[i]<=9:
            'tant que le chiffre ne peut pas être placé à cette endroit on augmente de plus 1 la valeur'
            'De plus, si la valeur du compteur est 10 alors on s    arrête , cela signifie qu on doit revenir à la case précèdente et en modifier la valeur'
            compteur[i]+=1

        if compteur[i]==10:
            'si le compteur est aller jusqu à 10, on le réinitialise à 0, on reviens un cran en arrière et on enlève la case posé precedemment'
            compteur[i]=0
            i-=1
            tableau[ordre[i][0],ordre[i][1]]= 0

        else:
            'si le test est possible alors le chiffre est donc possible à ce niveau et l on peut avancé au rang d git après'
            tableau[ordre[i][0],ordre[i][1]]= compteur[i]
            i+=1
    return tableau



def verify (tableau):
    'cette fonction prend en entrée un tableau et vérifie si le tableau est valide, ce qui signifie si deux chiffre sont oui ou non sur la même ligne la même colonne ou la même boîte'
    for i in range (9):
        for j in range(9):
            if tableau[i,j]!=0 :
                
                if not(test(tableau, i,j, tableau[i,j])):
                    return False
    return True



def difficulte_sudoku(tableau):
    S=0
    for i in range(9):
        for j in range(9):
            if tableau[i,j]!=0:
                S+=1
    if S>=61:
        p='easy'
    elif S<61 and S>41 :
        p='medium'
    elif S<=41 and S>21 :
        p='hard'
    else:
        p='ultrahard'
    return p
