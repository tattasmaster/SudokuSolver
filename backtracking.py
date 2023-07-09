class Sudoku_Solver:

    # Trouve et retourne une case qui est égale à 0 (vide)
    def trouver_case_vide(grille):
        # Boucle for sur l'array
        for i in range(len(grille)):
            for j in range(len(grille[0])):  # grille[0] représente la longueur de chaque ligne
                # Retourne une case égale à 0 (vide)
                if grille[i][j] == 0:
                    return (i, j)  # ligne, colonne

        # Retourne None si il n'y a aucune case égale à 0
        return None

    # Vérifie si le nombre que l'on essaye est valide (grille représente la grille, num le nombre qu'on a inséré, et pos la position)
    def valide(grille, num, pos):
        # Vérifie la ligne
        for i in range(len(grille[0])):
            # Vérifie sur chaque élément de la ligne si il y a un nombre égal à num, à moins que ce soit la position où l'on a inséré num
            if grille[pos[0]][i] == num and pos[1] != i:
                return False

        # Vérifie la colonne
        for i in range(len(grille)):
            # Vérifie sur chaque élément de la colonne si il y a un nombre égal à num, à moins que ce soit la position où l'on a inséré num
            if grille[i][pos[1]] == num and pos[0] != i:
                return False

        # Permet à l'algorithme de savoir dans quelle division de la grille num se trouve
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        # Boucle sur les neufs éléments de la division, permet aussi de se positionner sur la bonne division
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                # Vérifie sur chaque élément de la division si il y a un nombre égal à num
                if grille[i][j] == num and (i, j) != pos:
                    return False

        return True

    # Algorithme de backtracking
    def backtracking(grille):
        # Appel de la fonction find_empty qui retourne une case vide
        find = Sudoku_Solver.trouver_case_vide(grille)
        # Si la case n'est pas vide, on passe
        if not find:
            return True
        else:
            row, col = find

        # Essai des valeurs de 1 à 9 inclus sur la case
        for i in range(1, 10):
            # Appel de la fonction valid, et si la fonction retourne vrai alors on peut insérer i (le chiffre que l'on teste)
            if Sudoku_Solver.valide(grille, i, (row, col)):
                # Ajout de i sur la case
                grille[row][col] = i

                # Appel de la fonction à chaque insertion
                if Sudoku_Solver.backtracking(grille):
                    return True

                # Récursivité
                grille[row][col] = 0

        # Si on boucle sur tous les nombres mais qu'aucun d'entre eux n'est valide, alors -> grille[row][col] = 0
        return False