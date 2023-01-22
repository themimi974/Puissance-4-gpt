import os

# Initialisation du tableau de jeu
grid = [[' ' for _ in range(7)] for _ in range(6)]

# Initialisation des variables de jeu
player = 1
p1_tokens = 21
p2_tokens = 21
p1_wins = 0
p2_wins = 0
game_over = False

def display_grid():
    print("  1   2   3   4   5   6   7")
    print("+---+---+---+---+---+---+---+")
    for i in range(5, -1, -1):
        row = "|"
        for j in range(7):
            row += " " + grid[i][j] + " |"
        print(row)
        print("+---+---+---+---+---+---+---+")

def add_token(col):
    global player
    global p1_tokens
    global p2_tokens
    global game_over

    # Vérifie si la colonne choisie est valide
    if col < 1 or col > 7:
        print("Veuillez choisir une colonne valide (1-7)")
        return

    # Parcours les lignes de la colonne pour trouver la première case vide
    for i in range(6):
        if grid[i][col-1] == ' ':
            if player == 1:
                grid[i][col-1] = 'X'
                p1_tokens -= 1
            else:
                grid[i][col-1] = 'O'
                p2_tokens -= 1
            break
        elif i == 5:
            print("Cette colonne est pleine, veuillez en choisir une autre.")
            return

    # Vérifie si un joueur a gagné
    if check_win():
        game_over = True
        return

    # Vérifie si il y a match nul
    if p1_tokens == 0 and p2_tokens == 0:
        game_over = True
        return

    # Change de joueur
    player = 3 - player


# Fonction pour vérifier si un joueur a gagné
def check_win():
    # Vérifie les lignes
    for i in range(6):
        for j in range(4):
            if grid[i][j] != ' ' and grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3]:
                return True

    # Vérifie les colonnes
    for i in range(3):
        for j in range(7):
            if grid[i][j] != ' ' and grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j]:
                return True

        # Vérifie les diagonales (haut-gauche -> bas-droite)
    for i in range(3):
        for j in range(4):
            if grid[i][j] != ' ' and grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3]:
                return True

    # Vérifie les diagonales (bas-gauche -> haut-droite)
    for i in range(3):
        for j in range(4):
            if grid[i+3][j] != ' ' and grid[i+3][j] == grid[i+2][j+1] == grid[i+1][j+2] == grid[i][j+3]:
                return True
    return False

# Boucle principale du jeu
while True:
    os.system("cls" if os.name == "nt" else "clear")
    display_grid()
    print("Joueur 1 (X) :", p1_tokens)
    print("Joueur 2 (O) :", p2_tokens)
    print("Parties gagnées: Joueur 1: ",p1_wins," Joueur 2: ",p2_wins)
    col = int(input("Joueur {} : Choisissez une colonne (1-7) : ".format(player)))
    add_token(col)

    if game_over:
        # Affiche le résultat final
        os.system("cls" if os.name == "nt" else "clear")
        display_grid()
        if check_win():
            print("Joueur {} a gagné !".format(player))
            if player == 1:
                p1_wins +=1
            else:
                p2_wins +=1
        else:
            print("Match nul !")
        game_over = False
        grid = [[' ' for _ in range(7)] for _ in range(6)]
        p1_tokens = 21
        p2_tokens = 21
        player = 1
        col = 0



# Affiche le résultat final
os.system("cls" if os.name == "nt" else "clear")
display_grid()
if check_win():
    print("Joueur {} a gagné !".format(player))
    if player == 1:
        p1_wins +=1
    else:
        p2_wins +=1
else:
    print("Match nul !")


