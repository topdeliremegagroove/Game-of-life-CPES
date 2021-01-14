from tkinter import *
from functools import partial
# Utilisation de la fontion partial pour mettre des argument dans les "command" des boutons et "tag_bind".


# Mise en place de la fenêtre de jeu :
root = Tk()
root.title("Le Jeu de la Vie")
root.iconbitmap("logo.ico")




def change_color(coords, _) :        # changement de couleur des cellules
    i, j = coords
    if c.itemcget(grid_display[i][j], "fill") == "white" :
        c.itemconfig(grid_display[i][j], fill="black")
    else :
        c.itemconfig(grid_display[i][j], fill="white")



def initialisation() :           # Implémentation du Canvas contenant les cellules, et des différents boutons et textes de contrôle :

    global c, grid_display

    # Si le jeu dépasse de votre écran, diminuer la taille du Canvas (en pixel) ci-dessous :
    height = width = 900
    c = Canvas(root, height = height, width = width, bd=0, bg = "grey")
    c.grid(row=0, column=0, rowspan = 30)

    cell_side = height/size

    # Liste contenant les cellules :
    grid_display = []


    for i in range(size) :
        grid_display.append([])
        for j in range(size) :

            # Création des cellules dans le Canvas :
            grid_display[i].append(c.create_rectangle(cell_side*j, cell_side*i, cell_side*(j+1), cell_side*(i+1), width = 2, fill="white", tags=f"{i}_{j}"))

            # Détection de clique sur une cellule :
            c.tag_bind(f"{i}_{j}","<Button-1>", partial(change_color, (i, j)) )


    # Boutons permanents :
    global welcome_label, speed_scale, step, step_label, reset_button, reset_state

    # Texte de présentation :
    welcome_label = Label(text="Welcome in the Game of Life!")
    welcome_label.grid(row=3, column=2, columnspan=7)

    # Curseur de vitesse :
    speed_scale = Scale(root, orient="horizontal", from_ = 0, to = 16, resolution=0.1, tickinterval=2, label="Speed (steps/sec)", length = 330)
    speed_scale.set(2)
    speed_scale.grid(row=11, column=2, rowspan=4, columnspan=7)

    # Affichage de l'étape actuelle :
    step = 0
    step_label = Label(root, text=f"Step {step}")
    step_label.grid(row=15, column=2, columnspan=7)

    # Le bouton reset permet de revenir à la grille vierge à tout moment (la variable reset_state indique que le jeu est en cours d'initialisation) :
    reset_state = True
    reset_button = Button(root, command=reset, text="  Reset  ")
    reset_button.grid(row=20, column=5)



    # Boutons spécifiques à l'initialisation (stockés dans un dictionnaire pour pouvoir être détruits plus facilement) :
    global dico
    dico = {}

    # Entrée du nom du fichier d'initialistion :
    dico["file_entry"] = Entry(root, width = 30)
    dico["file_entry"].grid(row=5, column=2, columnspan=7)

    # Bouton de départ :
    dico["launch_button"] = Button(root, command=grid_generation, text="  Go !  ")
    dico["launch_button"].grid(row=6, column=2, columnspan=7)


    # Bouton pour sauvegarder l'affichage actuel :
    dico["save_button"] = Button(root, command=save, text="Save the grid")
    dico["save_button"].grid(row=27, column=2, columnspan=7)
    # Et une boîte d'entrée pour le nom du fichier (si l'entrée est vide, sauvegarde au nom 'Sauvegarde_tmp') :
    dico["save_entry"] = Entry(root, width=30)
    dico["save_entry"].grid(row=26, column=2, columnspan=7)


    # Label de modification de la taille de la grille :
    dico["size_label"] = Label(root, text = f"  Change size ({size}) :  ")
    dico["size_label"].grid(row=18, column=2, columnspan=7)

    # Entrée pour modifier manuellement la taille :
    dico["size_entry"] = Entry(root, width=7)
    dico["size_entry"].grid(row=19, column=5)

    # Boutons d'incrémentation/décrémentation de la taille de la grille (de 1, 2 ou 4 cellules) :
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

    # Désactivation des boutons de décrémentation pour avoir un minimum de 5 cellules :
    if size < 9 :
        dico["size_decrement4"].configure(state=DISABLED)
        if size < 7 :
            dico["size_decrement2"].configure(state=DISABLED)
            if size < 6 :
                dico["size_decrement1"].configure(state=DISABLED)



def save() :                                               # Sauvegarde de la grille actuelle :
    # Déterminisation du nom du fichier à sauvegarder :
    file_name = dico["save_entry"].get()
    if file_name == "" :
        file_name = "Sauvegarde_tmp"

    # Écriture du fichier de coordonnées :
    f = open(f"{file_name}.txt", "w")
    for i in range(len(grid_display)) :
        for j in range(len(grid_display)) :
            if c.itemcget(grid_display[i][j], "fill") == "black" :
                f.write(f"{i} {j}\n")
    f.close



def grid_generation() :   # Création de la première grille 0_1, puis traduction en 0-15 ; création du bouton pause :

    # Désactivation des tags des cellules :
    for i in range(len(grid_display)) :
        for j in range(len(grid_display)) :
            c.dtag(grid_display[i][j], f"{i}_{j}")


    # Génération de la grille de départ à partir d'un fichier donné :
    if dico["file_entry"].get() != "" :
        file = open(f"{dico['file_entry'].get()}.txt", "r")
        lines = file.readlines()
        file.close()

        grid = [[0]*size for _ in range(size)]
        for i in range(len(lines)) :
            coords = lines[i].split()
            grid[int(coords[0])][int(coords[1])] = 1

    # Ou manuellement dans le cas échéant
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
        save()

    # Traduction en grille 0-15 (une cellule impaire indique une cellule vivante) :
    first_grid = [[0]*len(grid) for _ in range(len(grid))]
    for i in range(1, len(grid)-1) :
        for j in range(1, len(grid) - 1) :
            if grid[i][j] == 1 :
                first_grid[i][j] += 1       # Indique que la cellule était vivante au tour d'avant (imparité)
                first_grid[i-1][j-1] += 2
                first_grid[i][j-1] += 2
                first_grid[i+1][j-1] += 2
                first_grid[i-1][j] += 2
                first_grid[i+1][j] += 2
                first_grid[i-1][j+1] += 2
                first_grid[i][j+1] += 2
                first_grid[i+1][j+1] += 2

    # Suppression des widget d'initialisation :
    for widget in dico.values() :
        widget.destroy()

    # Création du bouton pause :
    global pause_button, step

    # Bouton de pause : le curseur de vitesse est mis à 0, ce qui déclanche la fonction pause() dans update().
    pause_button = Button(root, text="  Pause  ", command=lambda : speed_scale.set(0))
    pause_button.grid(row=6, column=2, rowspan=2, columnspan=7)

    # Fin de l'initialisation indiquée par la variable reset_state :
    global reset_state
    reset_state = False

    step =- 1

    # On met en œuvre la première grille :
    update(first_grid)




def update(grid) :          # Fonction d'actualisation des cellules à partir d'une grille donnée :
    # Si le jeu est en cours de (ré)initialisation, la fonction update s'arrête (pour contrer le after() ci-après) :
    if reset_state :
        return

    for i in range(len(grid)) :
        for j in range(len(grid)) :

            # Détermination de la nouvelle couleur des cellules (impaire = vivante) :
            if grid[i][j] % 2 == 0 :
                color = "white"
            else :
                color = "black"

            # Actualisation de la couleur des cellules :
            c.itemconfig(grid_display[i][j], fill = color)

    # Incrémentation de l'étape :
    global step
    step += 1
    step_label.configure(text=f"Step {step}")

    # Évaluation de la grille suivante :
    new_grid = main_evaluate(grid)

    # Arrêt du programme s'il n'y a plus d'évolution :
    if grid == new_grid :
        pause_button.configure(state=DISABLED)
        return

    # Si la vitesse est à 0, appel de la fonction pause(), sinon, appel récursif de update(), après un certain temps à l'aide de la méthode tkinter .after() :
    speed = speed_scale.get()
    if speed != 0 :
        root.after(int(1000/speed), update, new_grid) #pendant un certain temps j'attends, puis j'appelle la fonction update
    else :
        pause(new_grid)




def main_evaluate(grid) :       # Évaluation de la grille suivante :
    stock = [[0]*len(grid) for _ in range(len(grid))]
    for i in range(1, len(grid) - 1) :
        for j in range(1, len(grid) - 1) :

            # Une cellule sera vivante si elle possède 2 ou 3 voisines (2+2=4 ou 2+2+2=6) et qu'elle est vivante (+1) ; ou bien si elle est morte et possède trois voisines (2+2+2=6) :
            if grid[i][j] in [5, 6, 7] :
                stock[i][j] += 1         # Indique que la cellule était vivante au tour suivant
                stock[i-1][j-1] += 2
                stock[i][j-1] += 2
                stock[i+1][j-1] += 2
                stock[i-1][j] += 2
                stock[i+1][j] += 2
                stock[i-1][j+1] += 2
                stock[i][j+1] += 2
                stock[i+1][j+1] += 2

    return stock



def pause(grid) :
    # Le bouton pause devient Resume :
    pause_button.configure(text="Resume", command=partial(resume, grid))

    # Définition d'un bouton qui permet d'avancer étape par étape :
    global step_button
    step_button = Button(root, text="Next step", command=partial(update_step_by_step, grid))
    step_button.grid(row=9, column=2, rowspan=2, columnspan=7)


def resume(grid) :
    step_button.destroy()
    speed_scale.set(2)

    # Le bouton pause reprend ses fonctions originales :
    pause_button.configure(text="Pause", command=lambda : speed_scale.set(0))
    update(grid)



def update_step_by_step(grid) :     # Actualisation d'une unique étape :

    # Détermination de la couleur, et actualisation de la cellule :
    for i in range(len(grid)) :
        for j in range(len(grid)) :

            if grid[i][j] % 2 == 0 :
                color = "white"
            else :
                color = "black"

            c.itemconfig(grid_display[i][j], fill = color)

    # Incrémentation de l'étape
    global step
    step += 1
    step_label.configure(text=f"Step {step}")

    # Détermination de l'étape suivante :
    new_grid = main_evaluate(grid)

    # Arrêt du programme s'il n'y a plus d'évolution :
    if grid == new_grid :
        step_button.configure(state=DISABLED)
        pause_button.configure(state=DISABLED)
        return

    # Actualisation des boutons Pause et étape par étape pour reprendre avec la nouvelle grille :
    pause_button.configure(command=partial(resume, new_grid))
    step_button.configure(command=partial(update_step_by_step, new_grid))




def reset(x = 0) :      # Fonction de réinitialisation du jeu (x != 0 si activée par un bouton de changement de taille) :

    global size, reset_state

    # Récupération de la taille à laquelle réinitialiser (seulement si nous sommes en (ré)initialisation :
    if reset_state == True :
        if dico["size_entry"].get() != "" :
            size = int(dico["size_entry"].get())
    # Si la taille entrée est inférieure à 5, inititialise à ce minimum :
    if size < 5 :
        size = 5

    # Changement de la taille quand réinitialisation à partir d'un bouton de taille :
    size += x

    # Indique que la réinitialisation est en cours (pour éviter que le after() du update() ne relance un ancien jeu après création de la nouvelle grille vierge) :
    reset_state = True

    # Destruction de tous les objets de la fenêtre :
    for widget in root.winfo_children() :
        widget.destroy()

    # Réinitialisation (avec la nouvelle taille)
    initialisation()



# Taille par défaut et lancement du programme :
size = 30
initialisation()




root.mainloop()
