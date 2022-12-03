from game_board import Game_Board
from players import RandomPlayer, MiniMaxPlayer
from time import sleep

# Set up board and players
end_criteria = False
gb = Game_Board()
players = {
    1: RandomPlayer,
    2: MiniMaxPlayer
    # More to come soon™
}
select_player_input = (
    "Select the player you wish to play against:\n"
    + "1 - Random Player\n"
    + "2 - Minimax Player\n"
    + "Choice: "
)
while True:
    try:
        opp_player = players[int(input(select_player_input))](player="O")
    except KeyError:
        print('Invalid option, choose between 1 and 2\n')
        sleep(0.5)
        continue
    except ValueError:
        print('Invalid option, choose a number that is either 1 or 2\n')
        sleep(0.5)
        continue
    else:
        break
current_player = "X" if opp_player.player == "O" else "O"
print()

# main loop
while end_criteria == False:
    if current_player == "X":
        while True:
            try:
                move_to_play = int(input(f"{current_player} Player's turn: "))
                gb.check_legal(move_to_play)
            except ValueError:
                print("Enter a number between 1 and 9.\n")
                continue
            except AssertionError:
                print("Illegal move - try again.\n")
                continue
            else:
                break
        gb.draw_move(move_to_play, current_player)

    else:
        move_to_play = opp_player.play_move(board=gb, player=current_player, maximising_player=True)
        gb.draw_move(coordinate=move_to_play[1], player=current_player)

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
