from tkinter import *
from functools import partial

root = Tk()
root.title("Le Jeu de la Vie")
root.iconbitmap("logo.ico")

'''' A faire : détecter la taille du fichier lu (ou en faire une par défaut, et dans ce cas, centrer les coordonnées) ;
'''



def change_color(coords, _) :        # changement de couleur des boutons
    i, j = coords
    if c.itemcget(grid_display[i][j], "fill") == "white" :
        c.itemconfig(grid_display[i][j], fill="black")
    else :
        c.itemconfig(grid_display[i][j], fill="white")


def initialisation() :             # implémentation des boutons pour initialiser la grille et les contrôles

    global c, grid_display

    height = width = 900
    c = Canvas(root, height = height, width = width, bd=0, bg = "grey")
    c.grid(row=0, column=0, rowspan = 30)

    cell_side = height/size

    grid_display = []


    for i in range(size) :
        grid_display.append([])
        for j in range(size) :

            grid_display[i].append(c.create_rectangle(cell_side*j, cell_side*i, cell_side*(j+1), cell_side*(i+1), width = 2, fill="white", tags=f"{i}_{j}"))

            c.tag_bind(f"{i}_{j}","<Button-1>", partial(change_color, (i, j) ))



    global welcome_label, speed_scale, step, step_label, reset_button

    # Boutons permanents :

    # Texte de présentation :
    welcome_label = Label(text="Bienvenue dans le Jeu de la Vie !")
    welcome_label.grid(row=3, column=2, columnspan=7)

    # Curseur de la vitesse :
    speed_scale = Scale(root, orient="horizontal", from_ = 0, to = 16, resolution=0.1, tickinterval=2, label="Speed (steps/sec)", length = 330)
    speed_scale.set(2)
    speed_scale.grid(row=11, column=2, rowspan=4, columnspan=7)

    # Affichage de l'étape actuelle :
    step = 0
    step_label = Label(root, text=f"Step {step}")
    step_label.grid(row=15, column=2, columnspan=7)

    # le bouton reset permet de revenir à la grille vierge à tout moment :
    reset_button = Button(root, command=reset, text="  Reset  ")
    reset_button.grid(row=20, column=5)


    # Boutons d'initialisation (stockés dans un dictionnaire pour pouvoir être détruits plus facilement) :

    global dico
    dico = {}

    # Entrée du fichier d'initialistion :
    dico["file_entry"] = Entry(root, width = 30)
    dico["file_entry"].grid(row=5, column=2, columnspan=7)

    # Bouton de départ :
    dico["launch_button"] = Button(root, command=grid_generation, text="  Go !  ")
    dico["launch_button"].grid(row=6, column=2, columnspan=7)


    # Bouton pour sauvegarder l'affichage actuel :
    dico["save_button"] = Button(root, command=sauvegarde, text="Save the grid")
    dico["save_button"].grid(row=27, column=2, columnspan=7)
    # Et une boîte d'entrée pour le nom du fichier (si l'entrée est vide, sauvegarde au nom 'Sauvegarde_tmp') :
    dico["save_entry"] = Entry(root, width=30)
    dico["save_entry"].grid(row=26, column=2, columnspan=7)


    # Label pour modifier la taille du quadrillage
    dico["size_label"] = Label(root, text = f"  Changer la taille ({size}) :  ")
    dico["size_label"].grid(row=18, column=2, columnspan=7)

    # Entrée pour modifier manuellement la taille :
    dico["size_entry"] = Entry(root, width=7)
    dico["size_entry"].grid(row=19, column=5)

    dico["size_increment1"] = Button(root, text="+1", command=partial(reset, 1))
    dico["size_increment1"].grid(row=19, column=6)

    dico["size_increment2"] = Button(root, text="+2", command=partial(reset, 2))
    dico["size_increment2"].grid(row=19, column=7)

    dico["size_increment4"] = Button(root, text="+4", command=partial(reset, 4))
    dico["size_increment4"].grid(row=19, column=8)


    dico["size_decrement1"] = Button(root, text="-1", command=partial(reset, -1))
    dico["size_decrement1"].grid(row=19, column=4)

    dico["size_decrement2"] = Button(root, text="-2", command=partial(reset, -2))
    dico["size_decrement2"].grid(row=19, column=3)

    dico["size_decrement4"] = Button(root, text="-4", command=partial(reset, -3))
    dico["size_decrement4"].grid(row=19, column=2)

    if size < 9 :
        dico["size_decrement4"].configure(state=DISABLED)
        if size < 7 :
            dico["size_decrement2"].configure(state=DISABLED)
            if size < 6 :
                dico["size_decrement1"].configure(state=DISABLED)



def sauvegarde() :
    file_name = dico["save_entry"].get()
    if file_name == "" :
        file_name = "Sauvegarde_tmp"

    f = open(f"{file_name}.txt", "w")
    for i in range(len(grid_display)) :
        for j in range(len(grid_display)) :
            if c.itemcget(grid_display[i][j], "fill") == "black" :
                f.write(f"{i} {j}\n")
    f.close



def grid_generation() :                 # création de la première grille 0_1, puis traduction en 0-15

    for i in range(len(grid_display)) :         # désactivation des cases en enlevant les tags
        for j in range(len(grid_display)) :
            c.dtag(grid_display[i][j], f"{i}_{j}")

    taille = size
    if dico["file_entry"].get() != "" :
        file = open(f"{dico['file_entry'].get()}.txt", "r")
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

    first_grid = [[0]*len(grid) for _ in range(len(grid))]
    for x in range(1, len(grid)-1) :
        for y in range(1, len(grid) - 1) :
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

    # Suppression des widget d'initialisation :
    for widget in dico.values() :
        widget.destroy()

    global pause_button, step
    # Bouton de pause
    pause_button = Button(root, text="  Pause  ", command=lambda : speed_scale.set(0)) # Le curseur mis à 0 arrête la boucle du update
    pause_button.grid(row=6, column=2, rowspan=2, columnspan=7)


    global reset_state
    reset_state = False

    step =- 1
    update(first_grid)




def update(grid) :          # fonction d'actualisation des Labels à partir d'une grille donné.
    if reset_state :
        return

    for i in range(len(grid)) :
        for j in range(len(grid)) :

            if grid[i][j] % 2 == 0 :
                color = "white"
            else :
                color = "black"

            c.itemconfig(grid_display[i][j], fill = color) #change l'objet du canva, change la couleur du rectangle dans grid display

    global step
    step += 1
    step_label.configure(text=f"Step {step}")
    new_grid = main_evaluate(grid)     # fonction qui calcule la grille suivante

    if grid == new_grid :       # arrêt du programme quand il n'y a plus d'évolution
        pause_button.configure(state=DISABLED)
        return

    speed = speed_scale.get()
    if speed != 0 :
        root.after(int(1000/speed), update, new_grid) #pendant un certain temps j'attends, puis j'appelle la fonction update
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


def pause(grid) :

    pause_button.configure(text="Resume", command=partial(resume, grid))

    global step_button
    step_button = Button(root, text="Next step", command=partial(update_step_by_step, grid))
    step_button.grid(row=9, column=2, rowspan=2, columnspan=7)


def resume(grid) :
    step_button.destroy()
    speed_scale.set(2)

    pause_button.configure(text="Pause", command=lambda : speed_scale.set(0)) #le bouton pause pointe vers la fonction pause
    update(grid)



def update_step_by_step(grid) :

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
        step_button.configure(state=DISABLED)
        pause_button.configure(state=DISABLED)
        return

    pause_button.configure(command=partial(resume, new_grid))

    step_button.configure(command=partial(update_step_by_step, new_grid))





def reset(x = 0) :

    global size, reset_state
    if reset_state == True :
        if dico["size_entry"].get() != "" :
            size = int(dico["size_entry"].get())
    if size < 5 :
        size = 5
    size += x

    reset_state = True

    for widget in root.winfo_children() :
        widget.destroy()

    initialisation()




size = 30
initialisation()





root.mainloop()
