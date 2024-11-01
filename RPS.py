import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # If it's the first play, choose Rock
    if not prev_play:
        return "R"

    # Count frequencies of the last 10 moves
    move_count = {'R': 0, 'P': 0, 'S': 0}
    for move in opponent_history[-10:]:
        if move:
            move_count[move] += 1

    # Determine the most frequent move in the last 10
    most_frequent_move = max(move_count, key=move_count.get)

    # Counter move mapping
    counter_move = {
        'R': 'P',  # Paper beats Rock
        'P': 'S',  # Scissors beats Paper
        'S': 'R'   # Rock beats Scissors
    }

    # Analyze longer patterns (e.g., last 5 moves)
    if len(opponent_history) > 5:
        pattern_count = {'R': 0, 'P': 0, 'S': 0}
        for move in opponent_history[-5:]:
            if move:
                pattern_count[move] += 1

        # If any move was played more than twice in the last 5 moves, counter it
        for move in pattern_count:
            if pattern_count[move] >= 2:
                return counter_move[move]

    # Introduce a slightly more significant randomness to reduce predictability
    if random.random() < 0.2:  # 20% chance to play randomly
        return random.choice(['R', 'P', 'S'])
    else:
        return counter_move[most_frequent_move]
