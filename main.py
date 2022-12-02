import random
import math


class Game_Board:

    def __init__(self):
        self.board_dict = {

            7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' ',
        }

        self.win_options = [
            [7, 8, 9], [4, 5, 6], [1, 2, 3],
            [7, 4, 1], [8, 5, 2], [9, 6, 3],
            [1, 5, 9], [7, 5, 3]
        ]

    # draws the board state
    def Update(self):

        print(
            f'{self.board_dict[7]} | {self.board_dict[8]} | {self.board_dict[9]}\n'
            + f'{self.board_dict[4]} | {self.board_dict[5]} | {self.board_dict[6]}\n'
            + f'{self.board_dict[1]} | {self.board_dict[2]} | {self.board_dict[3]}'
        )

    # check for any win
    def Check_For_Win(self):

        win = False

        for options in self.win_options:
            first = self.board_dict[options[0]]
            for option in options:
                win = True if first == self.board_dict[option] != ' ' else False
                if win == False:
                    break
            if win == True:
                return True
        return False

    # check if specific player won
    def Check_Winner(self, letter):

        win = False

        for options in self.win_options:
            first = letter
            for option in options:
                win = True if first == self.board_dict[option] != ' ' else False
                if win == False:
                    break
            if win == True:
                return True
        return False

    def Draw_Move(self, coordinate, player):
        self.board_dict[coordinate] = player

    def Check_Complete(self):
        for key in self.board_dict:
            if self.board_dict[key] == ' ':
                return False
        return True

    def Check_Legal(self, position):
        if self.board_dict[position] != ' ':
            return False
        else:
            return True

    # returns number of free spaces on the board
    def Free_Spaces(self):
        free = " "
        count = 0
        for key, value in self.board_dict.items():
            if value == free:
                count += 1
        return count

    # returns a list of possible moves
    def Possible_Move(self):
        free = " "
        pos_moves = []
        for key, value in self.board_dict.items():
            if value == free:
                pos_moves.append(key)
        return pos_moves


gb = Game_Board()
End_Criteria = False
Current_Player = "O"


def minimax(board, player, maximisingPlayer):
    other_player = "X" if player == "O" else "O"

    if board.Check_Winner(other_player) == True:
        return [(1*board.Free_Spaces() + 1), None] if maximisingPlayer == False else [(-1*board.Free_Spaces() - 1), None]

    elif board.Check_Complete() == True:
        return [0, None]

    if maximisingPlayer == True:  # maximising player
        maxEva = -(math.inf)
        list_of_moves = board.Possible_Move()

        for move in list_of_moves:
            board.board_dict[move] = player
            Eva = minimax(board, other_player, False)
            if Eva[0] > maxEva:
                best_move = move
            maxEva = max(Eva[0], maxEva)
            board.board_dict[move] = " "
        return [maxEva, best_move]
    else:  # minimising player
        minEva = (math.inf)
        list_of_moves = board.Possible_Move()

        for move in list_of_moves:
            board.board_dict[move] = player
            Eva = minimax(board, other_player, True)
            if Eva[0] < minEva:
                best_move = move
            minEva = min(Eva[0], minEva)
            board.board_dict[move] = " "
        return [minEva, best_move]


def random_move():
    move = random.randint(1, 9)
    return move


# main loop
while End_Criteria == False:
    Legal = False
    if Current_Player == "X":
        This_Turn = int(
            input(f"{Current_Player} Player's turn: "))

        while Legal == False:

            if gb.Check_Legal(This_Turn) == False:
                This_Turn = int(
                    input(f"Illegal move - {Current_Player} Player1's turn again: "))
            else:
                gb.Draw_Move(This_Turn, Current_Player)
                Legal = True
    else:
        This_Turn = minimax(gb, Current_Player, True)
        gb.Draw_Move(This_Turn[1], Current_Player)

    End_Criteria = gb.Check_For_Win()
    gb.Update()
    print(' ')

    # check if game ends else change players
    if End_Criteria == True:
        print('Winner: ' + Current_Player + '!!!')
    elif gb.Check_Complete() == True:
        End_Criteria = True
        print('Draw')
    elif Current_Player == "X":
        Current_Player = "O"
    else:
        Current_Player = "X"
