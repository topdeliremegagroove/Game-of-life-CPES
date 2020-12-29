

class plateau():

    def __init__(self, fichier = None):
        #lecture du fichier de l'état initial dans plateau racine
        file = open("fichier.txt", "r")

        lines = file.readlines()
        file.close()
        plateau_racine = [[] for _ in range(len(lines))]
        for i in range(len(lines)) :
            for ch in lines[i][:-1] :
                plateau_racine[i].append(ch)

        





    
#fichier doit contenir la taille et l'état de chaque cel

    def lignes(self, nbre_de_lignes)






class case() :

    def __init__(self, etat, cord)

  
    def coordonnees(self, x, y)
        self.x = x
        self.y = y

    def etat(self, vivant = 0) :
        return vivant 
    #voir methode magique


#main

#première évaluation
etat_voisin = 0
for i in Lignes :
    for j in Colonnes :
        dans le plateau racine
        etat_voisin = [i-1][j-1] + [i-1][j] + [i-1][j+1] + [i][j-1] + [i][j+1] + [i+1][j-1] + [i+1][j] + [i+1][j+1]
        if (etat[i][j] == 0) and (etat_voisin == 3) :
            etat[i][j] = 1 pour le nouveau plateau
            rajouter +1 aux autres pour le tour d'après dans le plateau 1 au 8 fdp

        elif  (etat[i][j] == 1) and ((etat_voisin < 2) or (etat_voisin >= 4)) :
            etat[i][j] = 0
        e
        else : 

        case.etat = 0
        elif case.v

#evaluation suivante n>2

for i in Lignes :
    for j in Colonnes :
        if case.voisin = 






    

    







