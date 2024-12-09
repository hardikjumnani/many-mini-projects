from typing import Dict

from art import logo, vs
from game_data import data

import random

def rand_person() -> Dict:
    return random.choice(data)

def compare(p1: Dict, p2: Dict, user_input: str):
    p_more: Dict[str, str|int] = p1 if p1['follower_count'] >= p2['follower_count'] else p2

    return True if (user_input.lower() == 'higher' and p_more == p2) or (user_input.lower() == 'lower' and p_more == p1) else False

def play_game() -> None:
    p1 = rand_person()
    score = 0
    while True:
        p2 = rand_person()
        print(p1['name'], p1['follower_count'], vs, p2['name'])

        if not compare(p1, p2, user_input=input('Higher or Lower? ')):
            print('Incorrect Guess.', p2['name'], p2['follower_count'])
            print('Your score was', score)
            break
        else:
            print("Correct Guess\n\n")
            p1 = p2

        score += 1


if __name__ == '__main__':
    print(logo)
    
    play_game()