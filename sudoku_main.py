import os
import numpy as np
from colorama import Fore, Style
from backtracking import Sudoku_Solver

# Prend le fichier et le retourne en array 9x9
def sudoku_format(file_name):
    # file_path récupère le fichier
    file_path = file_name
    # Lecture du fichier
    with open(file_path, 'r') as file:
        content = file.read()
    # Formattage du contenu : les espaces sont effacés, les _ sont remplacés par des 0, et les retours à la ligne sont effacés
    content = content.replace(' ', '').replace('_', "0").replace('\n', '')
    # Une array est créée grâce à numPy et le contenu de la variable content est ajouté à l'array en type int
    content_array = np.array(list(content)).astype(int)
    # L'array est reshape en 9x9
    reshaped_array = content_array.reshape((9, 9))
    # Retourne l'array
    return reshaped_array

# Prend les coordonnées de tous les éléments > 0 avant résolution
def get_coordinates(grille):
    # Vaiable qui va stocker les coordonnées
    coordinates = []
    # Boucle sur toute la grille
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            # Append dans coordinates si l'élément est supérieur à 0
            if grille[i][j] > 0:
                coordinates.append((i, j))

    return coordinates

# Affichage du sudoku dans un format lisible
def print_grille(grille, coordinates):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            element = str(grille[i][j]) # element = current element that is being printed
            if (i, j) in coordinates: # Si les coordonnées de cet élément sont en relaton avec
                element = f"{Fore.GREEN}{element}{Style.RESET_ALL}"

            # Dessine un trait vertical toutes les 3 colonnes
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(element, end=" ")

        print()

        # Dessine une ligne horizontale toutes les 3 lignes (3 % 3 = 0 et i != 0)
        if i % 3 == 2 and i != 8:
            print("- - - - - - - - - - -")


# Choix du sudoku à résoudre par l'utilisateur
def prompt():
    print("Sudoku Solver, bienvenue !")
    # Tant que l'utilisateur veut résoudre des Sudoku
    while True:
        # Choix du fichier
        file_name = input("Veuillez choisir un sudoku à résoudre (nom du fichier): ")
        # Vérifie si le fichier existe
        if os.path.exists(file_name):
            # try/catch au cas où le format du fichier n'est pas bon
            try:
                sudoku = sudoku_format(file_name) #Appel de la fonction qui prend le fichier txt et le convertit en array
                coordinates = get_coordinates(sudoku)
                Sudoku_Solver.backtracking(sudoku)  # Appel de la méthode solve de la classe Sudoku_Solver
                print(print_grille(sudoku, coordinates))
            # Catch de l'erreur si le format du fichier n'est pas bon
            except ValueError as e:
                print("Mauvais format")
            choix_user = (input("Voulez-vous résoudre un autre Sudoku ? (y/n) "))
            if choix_user.lower() != 'y':
                print("À bientôt !")
                break
        else:
            choix_user = (input("Ce fichier n'existe pas ! Voulez-vous utiliser un autre fichier ? (y/n) "))
            if choix_user.lower() != 'y':
                print("À bientôt !")
                break

# Appel de la fonction prompt pour interagir avec la console
prompt()
