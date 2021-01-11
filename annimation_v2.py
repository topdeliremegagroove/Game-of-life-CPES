from tkinter import *
from functools import partial
from time import sleep

root = Tk()
root.title("Le Jeu de la Vie")

# A faire : changer la taille de la grille ;
#           détecter la taille du fichier lu (ou en faire une par défaut, et dans ce cas, centrer les coordonnées) ;
#           --> faire avancer étape par étape
#           bouton de réinitialisation

taille = 30
pixel = 1000

c = Canvas(root, height = pixel, width = pixel, bg="grey")
c.grid(row=0, column=0, rowspan = 20)
side = pixel/taille

grid_display = []

def change_col(coord, _) :        # changement de couleur des boutons
    i,j = coord
    if c.itemcget(grid_display[i][j], "fill") == "white" :
        c.itemconfig(grid_display[i][j], fill="black")
    else :
        c.itemconfig(grid_display[i][j], fill="white")


def boutons() :             # implémentation des boutons pour initialiser la grille et les contrôles

    for i in range(taille) :
        grid_display.append([])
        for j in range(taille) :
            grid_display[i].append(c.create_rectangle(side*j, side*i, side*(j+1), side*(i+1), width=2, fill="white", tags=f"{i}_{j}"))
            c.tag_bind(f"{i}_{j}","<Button-1>", partial(change_col, (i,j)))

    global entry_file, launch_button, speed_scale, step, step_label, save_button, save_entry

    # Entrée du fichier d'initialistion
    entry_file = Entry(root, width = 30)
    entry_file.grid(row=4, column=50)

    # Bouton de départ
    launch_button = Button(root, command=grid_generation, text="  Go !  ")
    launch_button.grid(row=5, column=50)

    # Curseur de la vitesse
    speed_scale = Scale(root, orient="horizontal", from_ = 0, to = 16, resolution=0.1, tickinterval=2, label="Speed (steps/sec)", length = 330)
    speed_scale.set(2)
    speed_scale.grid(row=7, column=50, rowspan=3)

    # Affichage de l'étape actuelle
    step = 0
    step_label = Label(root, text=f"Step {step}")
    step_label.grid(row=11, column=50)

    # Bouton pour sauvegarder l'affichage actuel
    save_button = Button(root, command=sauvegarde, text="Save the grid")
    save_button.grid(row=15, column=50)
    # Et une boîte d'entrée pour le nom du fichier
    save_entry = Entry(root, width=30)
    save_entry.grid(row=14, column=50)



def sauvegarde() :
    file_name = save_entry.get()
    if file_name == "" :
        file_name = "Sauvegarde_tmp"

    f = open(f"{file_name}.txt", "w")
    for i in range(len(grid_display)) :
        for j in range(len(grid_display)) :
            if c.itemcget(grid_display[i][j], "fill") == "black" :
                f.write(f"{i} {j}\n")
    f.close



def grid_generation() :                 # création de la première grille 0_1

    for i in range(len(grid_display)) :         # désactivation des cases
        for j in range(len(grid_display)) :
            c.dtag(grid_display[i][j], f"{i}_{j}")

    if entry_file.get() != "" :
        file = open(f"{entry_file.get()}.txt", "r")
        lines = file.readlines()
        file.close()

        grid = [[0]*taille for _ in range(taille)]
        for i in range(len(lines)) :
            coords = lines[i].split()
            grid[int(coords[0])][int(coords[1])] = 1

    else :
        grid = []
        for i in range(len(grid_display)) :
            grid.append([])
            for j in range(len(grid_display)) :
                if c.itemcget(grid_display[i][j], "fill") == "white" :
                    grid[i].append(0)
                else :
                    grid[i].append(1)

        # Sauvegarde automatique de la position de départ
        sauvegarde()

    first_grid = [[0]*taille for _ in range(taille)]
    for x in range(1, taille-1) :
        for y in range(1, taille-1) :
            if grid[x][y] == 1 :
                first_grid[x][y] += 1 #indique que la cellule était vivante au tour d'avant
                first_grid[x-1][y-1] += 2
                first_grid[x][y-1] += 2
                first_grid[x+1][y-1] += 2
                first_grid[x-1][y] += 2
                first_grid[x+1][y] += 2
                first_grid[x-1][y+1] += 2
                first_grid[x][y+1] += 2
                first_grid[x+1][y+1] += 2

#boucle d'initialisation à partir de la grille racine
    entry_file.destroy()
    launch_button.destroy()
    save_button.destroy()
    save_entry.destroy()


    global pause_button
    # Bouton de pause
    pause_button = Button(root, text="Pause", command=partial(pause, grid))
    pause_button.grid(row=0, column = 50)

    update(first_grid)

    # generation_plateau(first_grid)


def generation_plateau(grid) :    # destruction des boutons et remplacement par des Labels à partir de la grille 0_1    (du coup non)
    pass
    # entry_file.destroy()
    # launch_button.destroy()
    # save_button.destroy()
    # save_entry.destroy()

#             # IMPORTANT J'ai gardé les boutons en les désactivant et on gagne beaucoup en rapidité
#
#     # for i in range(30) :
#     #     for j in range(30) :
#     #         grid_display[i][j].destroy()
#
#
#     for i in range(len(grid)) :
#         for j in range(len(grid)) :
#
#             if grid[i][j] % 2 == 0 :
#                 color = "white"
#             else :
#                 color = "black"
#
#             # grid_display[i][j] = c.create_rectangle(side*j, side*i, side*(j+1), side*(i+1), width=2, fill=color)



    # global pause_button
    # # Bouton de pause
    # pause_button = Button(root, text="Pause", command=partial(pause, grid))
    # pause_button.grid(row=0, column = 50)
    #
    # update(grid)



def update(grid) :          # fonction d'actualisation des Labels à partir d'une grille donné.
    global step
    step += 1
    step_label.configure(text=f"Step {step}")

    for i in range(len(grid)) :
        for j in range(len(grid)) :

            if grid[i][j] % 2 == 0 :
                color = "white"
            else :
                color = "black"

            c.itemconfig(grid_display[i][j], fill = color)

    new_grid = main_evaluate(grid)     # fonction qui calcule la grille suivante

    if grid == new_grid :       # arrêt du programme quand il n'y a plus d'évolution
        return

    speed = speed_scale.get()
    if speed != 0 :
        root.after(int(1000/speed), update, new_grid)
    else :
        pause(new_grid)




def main_evaluate(grid) :
    stock = [[0]*len(grid) for _ in range(len(grid))]
    for x in range(1, len(grid)-1) :
        for y in range(1, len(grid)-1) :
            if grid[x][y] in [5, 6, 7] :
                stock[x][y] += 1 #indique que la cellule était vivante au tour suivant
                stock[x-1][y-1] += 2
                stock[x][y-1] += 2
                stock[x+1][y-1] += 2
                stock[x-1][y] += 2
                stock[x+1][y] += 2
                stock[x-1][y+1] += 2
                stock[x][y+1] += 2
                stock[x+1][y+1] += 2

    return stock


def pause(grid) :                   # qq pb à régler : reenr à l'ancienne vitesse quand on reprend ; quand on fait apuse, ne pas faire l'update qui va se faire à la fin de l'after (pour des temps longs ntmt) ; voir si on peut mettre plusieurs arguments dans partial (peut être en utilisant des tuples)
    speed_scale.set(0)
    pause_button.configure(text="Resume", command=partial(resume, grid))

def resume(grid) :
    speed_scale.set(2)
    pause_button.configure(text="Pause", command=partial(pause, grid))
    update(grid)







buttons()





root.mainloop()