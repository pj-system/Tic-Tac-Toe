from game_board import Game_Board
from players import UserPlayer, RandomPlayer, MiniMaxPlayer
from time import sleep

# Set up board and players
end_criteria = False
gb = Game_Board()
player1_dict = {
    1: UserPlayer(player="X"),
    2: RandomPlayer(player="X"),
    3: MiniMaxPlayer(player="X")
    # More to come soon™
}
player2_dict = {
    1: UserPlayer(player="O"),
    2: RandomPlayer(player="O"),
    3: MiniMaxPlayer(player="O")
    # More to come soon™
}
select_player_input = (
    "Select player <PLAYER_NUM>:\n"
    + ''.join([f"{idx} - {repr(player)}\n" for idx, player in player1_dict.items()])
    + "Choice: "
)
while True:
    try:
        player1 = player1_dict[int(input(select_player_input.replace('<PLAYER_NUM>', '1')))]
        print()
        player2 = player2_dict[int(input(select_player_input.replace('<PLAYER_NUM>', '2')))]
    except KeyError:
        print(f'Invalid option, choose between {min(list(player1_dict.keys()))} and {max(list(player1_dict.keys()))} inclusive.\n')
        sleep(0.5)
        continue
    except ValueError:
        print(f'Invalid option, choose a number that is between {min(list(player1_dict.keys()))} and {max(list(player1_dict.keys()))} inclusive.\n')
        sleep(0.5)
        continue
    except Exception:
        print("I didn't think you could screw up this badly, reading the instructions again.\n")
        sleep(0.5)
        continue
    else:
        break
    
# Player 1 with symbol X starts first
current_player = player1.player
print()

# main loop
while end_criteria == False:
    if current_player == "X":
        move_to_play = player1.play_move(board=gb, player=current_player, maximising_player=True)
        if isinstance(move_to_play, (list, tuple)):
            move_to_play = move_to_play[1]
        gb.draw_move(position=move_to_play, player=current_player)

    else:
        move_to_play = player2.play_move(board=gb, player=current_player, maximising_player=True)
        if isinstance(move_to_play, (list, tuple)):
            move_to_play = move_to_play[1]
        gb.draw_move(position=move_to_play, player=current_player)

    end_criteria = gb.check_for_win()
    gb.draw_board()
    sleep(0.5)

    # check if game ends else change players
    if end_criteria == True:
        print(f'Winner: {current_player} !!!')
    elif gb.check_complete() == True:
        end_criteria = True
        print('Draw')
    else:
        current_player = "X" if current_player == "O" else "O"
