from typing import Tuple, List
from random import choice

hangman_figure = [
    '''
        ______________
             \|/
              |
              |''',
    '''
            ooooo
          oo     oo
        oo         oo
        oo         oo
        oo         oo
          oo     oo
            ooooo''',
    '''
              |
              |
              |''',
    '''
             /|\\
            / | \\
           /  |  \\
          /   |   \\
              |''',
    '''
             / \\
            /   \\
           /     \\
          /       \\'''
]

fruits: Tuple = (
    "apple", "banana", "orange", "strawberry", "grape",
    "mango", "blueberry", "pineapple", "watermelon", "cherry",
    "peach", "pear", "kiwi", "plum", "raspberry"
)

def draw_hangman(till_idx: int, lost=False) -> None:
    if lost: till_idx -= 1
    for i in range(min(till_idx + 1, len(hangman_figure))):
        if i == 0 and not lost:
            continue
        print(hangman_figure[i])

def char_input(dialog: str) -> str:
    while True:
        inp = input(dialog)
        if len(inp) == 1:
            return inp
        else:
            print('The input was not a character, enter only one alphabet.')

def main():
    win_word: str = choice(fruits)
    win_word_meta: List = [0] * len(win_word)
        # 0 - not revealed
        # 1 - revealed

    hangman_count: int = 0
    guess_letter: str = '_'
    while guess_letter != win_word:
        guess_letter = char_input('Give your guess character. ').lower()

        guessed_in_turn = False
        for i in range(len(win_word)):
            try:
                if guess_letter == win_word[i]:
                    if win_word_meta[i] != 1:
                        win_word_meta[i] = 1
                        guessed_in_turn = True
            except:
                # guess_letter smaller than win_word
                pass
        
        word_guessed = True
        for i in range(len(win_word_meta)):
            if win_word_meta[i] == 1:
                print(win_word[i], end='')
            else:
                word_guessed = False
                print('_', end='')
        print()

        if word_guessed: break

        if not guessed_in_turn:
            hangman_count += 1
            is_lost = hangman_count==len(hangman_figure)
            draw_hangman(hangman_count, lost = is_lost)

            if is_lost: 
                print('You couldn\'t guess the word')
                print('The word was', win_word)
                quit()

    print('Bravo! You guessed the word!')


if __name__ == '__main__':
    main()