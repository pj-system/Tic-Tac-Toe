import math
import random
from game_board import GameBoard
from abc import ABC, abstractmethod

class Player(ABC):
    """Base class that all player types inherit from."""
    def __init__(self, player: str) -> None:
        self.player = player
    
    @abstractmethod  # Dictates that all child classes must implement a __repr__ method
    def __repr__(self) -> str:
        """When calling print() or repr() on an instance of this class, it returns the below"""
        pass
    
    @abstractmethod  # Dictates that all child classes must implement a play_move method
    def play_move(self, board: GameBoard) -> str:
        pass


class UserPlayer(Player):
    """Player that the user controls."""
    def __init__(self, player: str) -> None:
        super().__init__(player)

    def __repr__(self) -> str:
        """When calling print() or repr() on an instance of this class, it returns the below"""
        return 'Yourself'

    def play_move(self, board: GameBoard, *args, **kwargs) -> str:
        while True:
            try:
                move_to_play = int(input(f"{self.player} Player's turn: "))
                board.check_legal(move_to_play)
            except ValueError:
                print("Enter a number between 1 and 9.\n")
                continue
            except KeyError:
                print("Enter a number between 1 and 9.\n")
                continue
            except AssertionError:
                print("Illegal move - try again.\n")
                continue
            else:
                break
        return move_to_play


class RandomPlayer(Player):
    """Player that randomly chooses moves based on available moves on the board."""
    def __init__(self, player: str) -> None:
        super().__init__(player)

    def __repr__(self) -> str:
        """When calling print() or repr() on an instance of this class, it returns the below"""
        return 'Random Player'

    def play_move(self, board: GameBoard, *args, **kwargs) -> str:
        list_of_moves = board.possible_moves()
        return random.choice(list_of_moves)


class MiniMaxPlayer(Player):
    """Player that makes their move based on the minimax algorithm."""
    def __init__(self, player: str) -> None:
        super().__init__(player)

    def __repr__(self) -> str:
        """When calling print() or repr() on an instance of this class, it returns the below"""
        return 'Minimax Player'

    def play_move(self, board: GameBoard, player: str, maximising_player: bool=True, *args, **kwargs) -> list:
        other_player = "X" if player == "O" else "O"

        if board.check_winner(other_player):
            return [None, (board.num_free_spaces() + 1)] if maximising_player == False else [None, (-board.num_free_spaces() - 1)]

        elif board.check_complete():
            return [None, 0]

        if maximising_player:  # maximising player
            maxEva = -math.inf
            list_of_moves = board.possible_moves()

            for move in list_of_moves:
                board.board_dict[move] = player
                _, Eva = self.play_move(board=board, player=other_player, maximising_player=False)
                if Eva > maxEva:
                    best_move = move
                maxEva = max(Eva, maxEva)
                board.board_dict[move] = " "
            return [best_move, maxEva]

        else:  # minimising player
            minEva = math.inf
            list_of_moves = board.possible_moves()

            for move in list_of_moves:
                board.board_dict[move] = player
                _, Eva = self.play_move(board=board, player=other_player, maximising_player=True)
                if Eva < minEva:
                    best_move = move
                minEva = min(Eva, minEva)
                board.board_dict[move] = " "
            return [best_move, minEva]
