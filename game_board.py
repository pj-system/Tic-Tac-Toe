"""Contains the GameBoard class which holds the board state and possible actions that can be performed."""

class GameBoard:

    def __init__(self) -> None:
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

    def draw_board(self) -> None:
        """Draws the board state in terminal."""
        print(
            f'{self.board_dict[7]} | {self.board_dict[8]} | {self.board_dict[9]}\n'
            + f'{self.board_dict[4]} | {self.board_dict[5]} | {self.board_dict[6]}\n'
            + f'{self.board_dict[1]} | {self.board_dict[2]} | {self.board_dict[3]}\n'
        )

    def check_for_win(self) -> bool:
        """Checks for any win by either players."""
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

    def check_winner(self, player: str) -> bool:
        """Check if a specific player has won."""
        win = False
        for options in self.win_options:
            first = player
            for option in options:
                win = True if first == self.board_dict[option] != ' ' else False
                if win == False:
                    break
            if win:
                return win
        return win

    def draw_move(self, position: int, player: str) -> None:
        """Draw a move on the board.
        
        Args:
            position (int): Integer representing the position of the board (1 to 9 inclusive)
            player (str): Symbol of the player that's drawing the move ('X' or 'O')
        """
        self.board_dict[position] = player

    def check_complete(self) -> bool:
        """Checks if the board has been complete (i.e., no free spaces left)."""
        for key in self.board_dict:
            if self.board_dict[key] == ' ':
                return False
        return True

    def check_legal(self, position: int):
        """Checks if a move is legal, an assertion error will be raised if it is not."""
        if self.board_dict[position] != ' ':
            raise AssertionError("Illegal Move!")
        else:
            return True

    def num_free_spaces(self) -> int:
        """Returns the number of free spaces on the board."""
        free = " "
        count = 0
        for value in self.board_dict.values():
            if value == free:
                count += 1
        return count

    # returns a list of possible moves
    def possible_moves(self) -> list:
        """Returns a list of all possible moves on the current board."""
        free = " "
        pos_moves = []
        for key, value in self.board_dict.items():
            if value == free:
                pos_moves.append(key)
        return pos_moves