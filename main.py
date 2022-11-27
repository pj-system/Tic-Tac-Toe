Board = {
    7: ' ', 8: ' ', 9: ' ',
    4: ' ', 5: ' ', 6: ' ',
    1: ' ', 2: ' ', 3: ' ',
}


def Check_For_Win():

    # Horizontals
    if Board[1] == Board[2] == Board[3] != ' ' or Board[4] == Board[5] == Board[6] != ' ' or Board[7] == Board[8] == Board[9] != ' ':
        Winner = PLAYER_SHAPE[PLAYER]
        return True
    # Verticals
    elif Board[1] == Board[4] == Board[7] != ' ' or Board[2] == Board[5] == Board[8] != ' ' or Board[3] == Board[6] == Board[9] != ' ':
        Winner = PLAYER_SHAPE[PLAYER]
        return True
    # Cross
    elif Board[7] == Board[5] == Board[3] != ' ' or Board[1] == Board[5] == Board[9] != ' ':
        Winner = PLAYER_SHAPE[PLAYER]
        return True
    else:
        return False


def Update(Board):
    print(f"""{Board[7]} | {Board[8]} | {Board[9]}
{Board[4]} | {Board[5]} | {Board[6]}
{Board[1]} | {Board[2]} | {Board[3]}
""")


WIN_CRITERIA = False

PLAYER_SHAPE = ["X", "O"]
PLAYER = 1
CHECK_LEGAL_MOVE = False

while WIN_CRITERIA == False:
    This_Turn = int(input(f"{PLAYER_SHAPE[PLAYER]} player's turn: "))
    CHECK_LEGAL_MOVE = False

    while CHECK_LEGAL_MOVE == False:

        if Board[This_Turn] != " ":
            This_Turn = int(
                input(f"Illegal move - {PLAYER_SHAPE[PLAYER]} player's turn again: "))
        else:
            Board[This_Turn] = PLAYER_SHAPE[PLAYER]
            CHECK_LEGAL_MOVE = True

    WIN_CRITERIA = Check_For_Win()

    Update(Board)

    if WIN_CRITERIA == True:
        WINNER = PLAYER_SHAPE[PLAYER]

    if PLAYER_SHAPE[PLAYER] == "X":
        PLAYER = 1
    else:
        PLAYER = 0

print('Winner: ' + WINNER + '!!!')
