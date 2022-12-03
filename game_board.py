"""Contains the Game_Board class which holds the board state and possible actions that can be performed."""

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
    def draw_board(self):
        print(
            f'{self.board_dict[7]} | {self.board_dict[8]} | {self.board_dict[9]}\n'
            + f'{self.board_dict[4]} | {self.board_dict[5]} | {self.board_dict[6]}\n'
            + f'{self.board_dict[1]} | {self.board_dict[2]} | {self.board_dict[3]}\n'
        )

    # check for any win
    def check_for_win(self):

        win = False

        for options in self.win_options:
            first = self.board_dict[options[0]]
            for option in options:
                win = True if first == self.board_dict[option] != ' ' else False
                if win == False:
                    break
            if win:
                return win
        return win

    # check if specific player won
    def check_winner(self, letter):

        win = False

        for options in self.win_options:
            first = letter
            for option in options:
                win = True if first == self.board_dict[option] != ' ' else False
                if win == False:
                    break
            if win:
                return win
        return win

    def draw_move(self, coordinate, player):
        self.board_dict[coordinate] = player

    def check_complete(self):
        for key in self.board_dict:
            if self.board_dict[key] == ' ':
                return False
        return True

    def check_legal(self, position):
        if self.board_dict[position] != ' ':
            raise AssertionError("Illegal Move!")
        else:
            return True

    # returns number of free spaces on the board
    def num_free_spaces(self):
        free = " "
        count = 0
        for value in self.board_dict.values():
            if value == free:
                count += 1
        return count

    # returns a list of possible moves
    def possible_moves(self):
        free = " "
        pos_moves = []
        for key, value in self.board_dict.items():
            if value == free:
                pos_moves.append(key)
        return pos_moves