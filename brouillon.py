#lecture du fichier de l'état initial dans plateau racine
taille = 10
file = open("fichier.txt", "r")
lines = file.readlines()
file.close()
print(lines)

root_grid = [[0]*taille for _ in range(taille)]
for i in range(len(lines)) :
    coords = lines[i].split()
    root_grid[int(coords[0])][int(coords[1])] = 1
    

first_grid = [[0,0]*taille for _ in range(taille)]

#boucle d'initialisation à partir de la grille racine
for x in range(taille) :
    for y in range(taille) :
        if root_grid[x][y] == 1 :
            first_grid[x][y] += 1 #indique que la cellule était vivante au tour d'avant
            first_grid[x-1][y-1] += 2
            first_grid[x][y-1] += 2
            first_grid[x+1][y-1] += 2
            first_grid[x-1][y] += 2
            first_grid[x+1][y] += 2
            first_grid[x-1][y+1] += 2
            first_grid[x][y+1] += 2
            first_grid[x+1][y+1] += 2

#voisin compte le nombre de cellules vivantes autour d'une cellule dans la grille racine


#boucle principale, pair cellule morte, impair cellule vivante

def main_evaluate(grid, stock) :
    stock = [[0,0]*taille for _ in range(taille)]
    for x in range(taille) :
        for y in range(taille) :
            if grid[x][y] == (5 or 6 or 7) :
                stock[x][y] += 1 #indique que la cellule était vivante au tour d'avant
                stock[x-1][y-1] += 2
                stock[x][y-1] += 2
                stock[x+1][y-1] += 2
                stock[x-1][y] += 2
                stock[x+1][y] += 2
                stock[x-1][y+1] += 2
                stock[x][y+1] += 2
                stock[x+1][y+1] += 2

    return stock
