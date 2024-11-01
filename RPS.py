import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # If it's the first play, choose Rock
    if not prev_play:
        return "R"

    # Count frequencies of last few moves
    move_count = {'R': 0, 'P': 0, 'S': 0}

    # Count the last 5 moves
    for move in opponent_history[-5:]:
        if move:
            move_count[move] += 1

    # Determine the most frequent move
    most_frequent_move = max(move_count, key=move_count.get)

    # Counter the most frequent move
    counter_move = {
        'R': 'P',  # Paper beats Rock
        'P': 'S',  # Scissors beat Paper
        'S': 'R'   # Rock beats Scissors
    }

    # Return the counter move for the most frequent play
    return counter_move[most_frequent_move]
