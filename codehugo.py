from tkinter import *
from functools import partial

dico = {}
root = Tk()


def generation_plateau(grid) :   

    for i in range(len(grid)) :
        for j in range(len(grid)) :
            #dico[f"b{chr(i)}{chr(j)}"].destroy()

            if grid[i][j]%2 == 0 :
                color = "white"
            else :
                color = "black"

            dico[f"b{chr(i)}{chr(j)}"] = Label(root, padx=15, pady=5, bg=color, relief=RAISED)
            dico[f"b{chr(i)}{chr(j)}"].grid(row=i, column=j)

generation_plateau([[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])

root.mainloop()
