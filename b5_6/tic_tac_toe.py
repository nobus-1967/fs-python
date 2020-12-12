"""Tic Tac Toe game, (c) Nobus, 2020."""

# Create a dictionary for matching
# players' moves and field coordinates.
MOVES = {'a3': 0,
         'b3': 1,
         'c3': 2,
         'a2': 3,
         'b2': 4,
         'c2': 5,
         'a1': 6,
         'b1': 7,
         'c1': 8
         }

# Create patterns of winning moves.
WIN = ({0, 1, 2},
       {3, 4, 5},
       {6, 7, 8},
       {0, 3, 6},
       {1, 4, 7},
       {2, 5, 8},
       {0, 4, 8},
       {2, 4, 6})


def main():
    """Start the main function of the game."""
    # Create the empty field.
    field = ['.'] * 9

    # Show game info.
    print('\n\tWelcome to TIC-TAC-TOE game!')

    # Show rules.
    show_rules()

    # Show that the game begins.
    print('Let\'s play a new game!')

    # Show the starting position.
    show_field(field)

    # Call play_game function.
    play_game(field)

    # Show final message.
    print('\nThank you for playing the game!')


def show_rules():
    """Show brief rules of Tic Tac Toe game."""
    rules = """
\"Tic-tac-toe" (or "Noughts and Crosses") is the game for
two players(X and O), who take turns moving on the 3×3 field.
The player who succeeds in placing three of their marks
in a horizontal, vertical, or diagonal row is the winner.
A game can also end in a draw if there's no longer any empty cells.
"""
    print(rules)


def play_game(field):
    """Control the process of a game."""
    move = play_move('X', field)
    if move:
        return move
    move = play_move('O', field)
    if move:
        return move
    play_game(field)


def play_move(player, field):
    """Control the move."""
    # Check for empty cell
    is_empty_cell = check_empty_cells(field)
    if is_empty_cell:
        # Continue the game.
        # Input new move and refresh the position.
        input_new_move(player, field)
        show_field(field)

        # Check for the winner.
        winner = check_win(player, field)
        if winner:
            print(f'Player ({player}) wins the game!')
            return True
        return False
    else:
        # End the game.
        print('That\'s a draw! The game is over.')
        return True


def show_field(field):
    """Show the current position."""
    print('\nCurrent position of the game:\n')
    print('\t ', 'A', 'B', 'C')
    print('\t3', field[0], field[1], field[2], '3')
    print('\t2', field[3], field[4], field[5], '2')
    print('\t1', field[6], field[7], field[8], '1')
    print('\t ', 'A', 'B', 'C\n')


def check_empty_cells(field):
    """Check for empty cells."""
    flag = False
    for index in range(0, 9):
        if field[index] == '.':
            flag = True
    return flag


def input_new_move(player, field):
    """Request the player's move, check it and change the field."""
    try:
        new_move = input(f'Player ({player}): please, enter your move: ')
        new_move = new_move.lower()
        if len(new_move) < 2 or len(new_move) > 2:
            print('You should enter valid coordinates \n\
\t(for example: a1, b2 etc)!')
            return input_new_move(player, field)
        index = MOVES[new_move]
        is_empty_cell = check_cell(index, player, field)
        if is_empty_cell:
            field[index] = player
        else:
            return input_new_move(player, field)
    except KeyError:
        print('You\'ve entered wrong coordinates! Please, try again.')
        return input_new_move(player, field)


def check_cell(index, player, field):
    """Check if the cell is empty."""
    if field[index] != '.':
        print('That cell is not empty! Please, choose another cell.')
        return False
    return True


def check_win(player, field):
    """Check if the player wins."""
    flag = False
    player_moves = check_player_moves(player, field)
    for pattern in WIN:
        if pattern.intersection(player_moves) == pattern:
            flag = True
    return flag


def check_player_moves(player, field):
    """Collect all player moves to check them."""
    player_moves = set()
    for i in range(0, 9):
        if field[i] == player:
            player_moves.add(i)

    return player_moves


# Call the main function.
if __name__ == '__main__':
    main()
