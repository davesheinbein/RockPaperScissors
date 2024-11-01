import random

def player(prev_play, opponent_history=[], name_history=[], my_history=[], play_order=[{"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}]):
    opponent_history.append(prev_play)
    
    # Default response
    guess = "R"
    iter = len(opponent_history)
    
    # Define counter moves
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Reset history every 1000 rounds
    if iter == 1001:
        opponent_history.clear()
        opponent_history.append(prev_play)
        name_history.clear()
        name_history.append('')
        my_history.clear()

    # Identify bot based on the first three moves
    if iter <= 4:
        if iter == 1:
            my_history.append("R")
            return "R"
        elif iter == 2:
            my_history.append("P")
            return "P"
        elif iter == 3:
            my_history.append("S")
            return "S"
        else:
            opponent_code = "".join(opponent_history[-3:])
            codetobot = {"RPP": "quincy", "PPP": "abbey", "PPS": "kris", "RRR": "mrugesh"}
            opponent = codetobot.get(opponent_code, "unknown")
            name_history.append(opponent)

    if name_history[-1] == 'quincy':
        # Strategy against quincy
        choices = ["R", "R", "P", "P", "S"]
        next_move = choices[iter % len(choices)]
        guess = ideal_response[next_move]

    elif name_history[-1] == 'abbey':
        # Enhanced pattern tracking for abbey
        if iter >= 3:
            last_three = "".join(my_history[-3:])
            if last_three in play_order[0]:
                play_order[0][last_three] += 1
            else:
                play_order[0][last_three] = 1

        potential_plays = [my_history[-1] + "R", my_history[-1] + "P", my_history[-1] + "S"]
        sub_order = {k: play_order[0].get(k, 0) for k in potential_plays}

        # Counter abbey’s predicted next move
        prediction = max(sub_order, key=sub_order.get)[-1:] if sub_order else random.choice(["R", "P", "S"])
        guess = ideal_response[prediction]

    elif name_history[-1] == 'kris':
        # Strategy against kris
        next_move = ideal_response[my_history[-1]]
        guess = ideal_response[next_move]

    elif name_history[-1] == 'mrugesh':
        # Enhanced strategy for mrugesh
        last_ten = opponent_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count) if last_ten else "S"
        
        if len(last_ten) >= 2:
            move_pair = last_ten[-2] + last_ten[-1]
            if move_pair in play_order[0]:
                play_order[0][move_pair] += 1
            else:
                play_order[0][move_pair] = 1
            predicted_move = max(play_order[0], key=play_order[0].get)[-1]
            guess = ideal_response[predicted_move]
        else:
            guess = ideal_response[most_frequent]

    my_history.append(guess)
    return guess
