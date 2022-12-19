import math
import random
from game_board import GameBoard
from abc import ABC, abstractmethod
import numpy as np


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

    def play_move(self, board: GameBoard, player: str, maximising_player: bool = True, *args, **kwargs) -> list:
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
                _, Eva = self.play_move(
                    board=board, player=other_player, maximising_player=False)
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
                _, Eva = self.play_move(
                    board=board, player=other_player, maximising_player=True)
                if Eva < minEva:
                    best_move = move
                minEva = min(Eva, minEva)
                board.board_dict[move] = " "
            return [best_move, minEva]


class TabQLPLayer(Player):
    """Player that makes their move based on tabular Q Learning."""

    def __init__(self, player: str) -> None:
        super().__init__(player)
        self.q_dict = {}
        self.move_history = []
        self.epsilon = 0.9  # % of time a Q value actions is taken, otherwise a random action
        self.gamma = 0.95  # discount factor
        self.alpha = 0.9  # learning rate
        self.init_q = 0.5

    def __repr__(self) -> str:
        """When calling print() or repr() on an instance of this class, it returns the below"""
        return 'Tabular Q Learning Player'

    def play_move(self, board: GameBoard, *args, **kwargs) -> str:
        """
        Plays a move
        """
        options = board.possible_moves()
        options_dict = {}
        options_Q_dict = {}
        for move in options:
            board.board_dict[move] = self.player
            options_dict[int(move)] = self.hash_state(board)
            options_Q_dict[int(move)] = self.get_q(options_dict[int(move)])
            board.board_dict[move] = ' '

        if random.random() > self.epsilon:
            next_move = random.choice(options)
            self.move_history.insert(
                0, [max(options_Q_dict.values()), options_dict[next_move]])
            return next_move

        else:
            next_move = options[0]
            for key, value in options_dict.items():
                if self.get_q(value) > self.get_q(options_dict[next_move]):
                    next_move = key
            self.move_history.insert(
                0, [max(options_Q_dict.values()), options_dict[next_move]])
            return int(next_move)

    def update_q(self):
        pass

    def get_q(self, hash: str) -> float:
        """
        Returns the Q Value for a given move if known, else initialises Q for that move and returns inital Q
        """
        if hash in self.q_dict:
            q_val = self.q_dict[hash]
            return q_val
        else:
            self.q_dict[hash] = self.init_q
            return self.init_q

    def hash_state(self, board: GameBoard) -> str:
        """Returns a hash value of the current board state
        followed by 9 digit string where 0 = " ", 1 = player, 2 = other player
        """
        hashvalue = ''
        for key, value in board.board_dict.items():
            if value == self.player:
                hashvalue = ''.join([hashvalue, '1'])
            elif value != self.player and value != ' ':
                hashvalue = ''.join([hashvalue, '2'])
            elif value == ' ':
                hashvalue = ''.join([hashvalue, '0'])
        return hashvalue

    def learning(self, other_player: Player, training_epsiodes: int, gb=GameBoard()) -> None:
        """
        Trains the AI
        """
        ticcount = 0
        for _ in range(training_epsiodes):
            current_player = 'X'
            end_criteria = False
            while end_criteria == False:
                if current_player == self.player:
                    move_to_play = self.play_move(board=gb, player=self.player)
                    if isinstance(move_to_play, (list, tuple)):
                        move_to_play = move_to_play[0]
                    gb.draw_move(position=move_to_play, player=current_player)
                    current_player = other_player.player

                else:
                    move_to_play = other_player.play_move(
                        board=gb, player=other_player.player)
                    if isinstance(move_to_play, (list, tuple)):
                        move_to_play = move_to_play[0]
                    gb.draw_move(position=move_to_play, player=current_player)
                    current_player = self.player

                if gb.check_for_win() == True or gb.check_complete() == True:
                    end_criteria = True

            if end_criteria == True:

                if gb.check_winner(self.player) == True:
                    end_q = 1.0

                elif gb.check_winner(other_player.player) == True:
                    end_q = 0.0

                else:
                    end_q = 0.5

                count = 0
                for turn in self.move_history:
                    if count == 0:
                        self.q_dict[turn[1]] = end_q
                        count += 1
                    else:
                        nextmaxQ = self.move_history[(count-1)][0]
                        self.q_dict[turn[1]] = self.q_dict[turn[1]] + \
                            self.alpha*(self.gamma*nextmaxQ -
                                        self.q_dict[turn[1]])
                        count += 1

            self.move_history = []
            gb = GameBoard()

            # print(ticcount)

            ticcount = ticcount + 1

        self.epsilon = 1


# player2 = TabQLPLayer(player="O")
# coach = RandomPlayer(player="X")
# player2.learning(coach, 100)
