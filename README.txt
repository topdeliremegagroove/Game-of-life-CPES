# Game-of-life-CPES
Projet en L2 CPES, programmer le jeu de la vie du mathématicien John Conway. Damien Fromilhague, Hugo Le Roux et Corentin Lucas


Bienvenue dans le Jeu de la Vie ! 

Notre programme est une implémentation python du Jeu de la Vie de Conway, dont les règles complètes, peuvent être retrouvées sur Wikipédia (https://fr.wikipedia.org/wiki/Jeu_de_la_vie).
En plus de notre fichier .py, vous pourrez retrouver une image  servant de logo (logo.ico) à la fenêtre de visualisation ; ainsi que trois fichier .txt (Presentation.txt, Presentation2.txt, et Canon.txt).
Pour un bon fonctionnement du programme, assurez-vous que ces fichiers se trouvent dans votre working directory. 

À l'exécution, notre programme affiche une grille de cellules blanches (mortes). Il suffit de cliquer dessus pour les rendre vivantes, et de lancer le jeu en appuyant sur le bouton "Go !".
Vous pouvez également entrer le nom d'un des fichiers de présentation (sans le .txt) dans la première boîte de dialogue pour les lancer.
Dans le cas d'utilisation du fichier Canon.txt, merci de changer la taille de la grille à au moins 42 cellules de côté (se référer ci-dessous pour la gestion de la taille). Pour les autres fichiers, la taille par défaut de 30 cellules de côté est suffisante.

Il est possible, avant et pendant le jeu, de régler la vitesse d'exécution en glissant le curseur "Speed" (notez qu'une grille trop grande majorera la vitesse possible).
Le bouton "Pause" permet de stopper momentanément le jeu. 
Lors de la pause, il est possible d'avancer étape par étape avec le bouton "Next Step", ou bien de reprendre l'avancée automatique avec le bouton "Resume".

Nous avons décidé d'ajouter des contrôles supplémentaires afin de rentre le jeu plus agréable :
- Il est possible de changer la taille de la grille avec les boutons allant de -4 à +4 ; ou bien en entrant un entier dans la boîte de dialogue située entre ces boutons, puis en apuyant sur "Reset". Pour des raisons d'utilité, une taille minimale de 5 cellule de côté est automatiquement affichée ;
- Le bouton "Reset" permet de réinitialiser la grille à l'état vierge à tout moment ;
- Une sauvegarde des coordonnées de l'état initial de la grille est automatiquement effectuée dans le working directory sous le nom "Sauvegarde_tmp.txt", et ce à chaque fois que le programme est lancé à partir d'un motif manuel.
Il est possible de personnaliser le nom du fichier en entrant le nom désiré dans la boîte de dialogue en bas (sans le .txt). 

Quelques indications sur les fichiers de présantation :
- Presentation.txt : Il y a là 5 structure. Trois sont stables (le Bloc (centre en haut), le Bateau (en haut à droite), et une structure stable à 27 cellules (droite)) ; et deux structures sont périodiques (le clignotant (2-périodique) et l'horloge (4-périodique)) ;
- Presentation2.txt : Il s'agit une structure de base de 5 cellules, mais qui est très instable. Du fait des bordures de notre programme, la structure atteint stabilité au bout d'une 320aine d'étapes, mais sans restriction de bords, la stabilité n'est atteinte qu'au bout de 1103 étapes.
- Canon.txt : Voici le plus petit générateur de planneur. Un planeur est une structure en translation diagonale toutes les 4 étapes, allant vers l'infini.


En espérant que la Vie vous réserve de bonnes surprises, 

Damien Fromilhague, Hugo Le Roux, Corentin Lucas.
