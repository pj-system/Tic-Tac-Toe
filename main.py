import random


class Game_Board:

    def __init__(self):
        self.board_dict = {
            7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' ',
        }

    def Update(self):

        print(
            f'{self.board_dict[7]} | {self.board_dict[8]} | {self.board_dict[9]}\n'
            + f'{self.board_dict[4]} | {self.board_dict[5]} | {self.board_dict[6]}\n'
            + f'{self.board_dict[1]} | {self.board_dict[2]} | {self.board_dict[3]}'
        )

    def Check_For_Win(self):

        # Horizontals
        if self.board_dict[1] == self.board_dict[2] == self.board_dict[3] != ' ' or self.board_dict[4] == self.board_dict[5] == self.board_dict[6] != ' ' or self.board_dict[7] == self.board_dict[8] == self.board_dict[9] != ' ':
            return True
        # Verticals
        elif self.board_dict[1] == self.board_dict[4] == self.board_dict[7] != ' ' or self.board_dict[2] == self.board_dict[5] == self.board_dict[8] != ' ' or self.board_dict[3] == self.board_dict[6] == self.board_dict[9] != ' ':
            return True
        # Cross
        elif self.board_dict[7] == self.board_dict[5] == self.board_dict[3] != ' ' or self.board_dict[1] == self.board_dict[5] == self.board_dict[9] != ' ':
            return True
        else:
            return False

    def Draw_Move(self, coordinate, player):
        self.board_dict[coordinate] = player

    def Check_Complate(self):
        for key in self.board_dict:
            if self.board_dict[key] == ' ':
                return False
        return True

    def Check_Legal(self, position):
        if self.board_dict[position] != ' ':
            return False
        else:
            return True


class Player:
    def __init__(self, current_board):
        self.board = current_board

    def Check_Legal(self, position):
        if self.board[position] != ' ':
            return False
        else:
            return True


class Ai_Player_Random(Player):

    def Make_Move(self):
        move = random.randint(1, 9)
        return move


class Human_Player:

    def Pick_Move(self):
        pass


gb = Game_Board()
End_Criteria = False
SHAPES = ["X", "O"]
Current_Player = 0


def minimax(board, depth, maximisingPLayer):
    pass


# main loop
while End_Criteria == False:
    This_Turn = int(
        input(f"{SHAPES[Current_Player]} Current_Player's turn: "))
    Legal = False

    while Legal == False:

        if gb.Check_Legal(This_Turn) == False:
            This_Turn = int(
                input(f"Illegal move - {SHAPES[Current_Player]} Current_Player's turn again: "))
        else:
            gb.Draw_Move(This_Turn, SHAPES[Current_Player])
            Legal = True

    End_Criteria = gb.Check_For_Win()
    gb.Update()

    # check if game ends else change players
    if End_Criteria == True:
        print('Winner: ' + SHAPES[Current_Player] + '!!!')
    elif gb.Check_Complate() == True:
        End_Criteria = True
        print('Draw')
    elif SHAPES[Current_Player] == "X":
        Current_Player = 1
    else:
        Current_Player = 0
