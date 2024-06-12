from typing import Tuple, List
from random import choice

nouns: Tuple = ('cat', 'tree', 'book', 'chair', 'apple', 'bird', 'shoe', 'fish', 'cup', 'flower')

def main():
    win_word: str = choice(nouns)
    win_word_meta: List = [0] * len(win_word)
        # 0 - not revealed
        # 1 - revealed

    guess_count: int = 1
    guess_word: str = input('Take a guess. ').lower()
    while guess_word != win_word:
        for i in range(len(win_word)):
            try:
                if guess_word[i] == win_word[i]:

                    win_word_meta[i] = 1
            except:
                # guess_word smaller than win_word
                pass
        
        for i in range(len(win_word_meta)):
            if win_word_meta[i] == 1:
                print(win_word[i], end='')
            else:
                print('_', end='')
        print()

        guess_word: str = input('Take a guess. ').lower()

        guess_count += 1
    
    print(f'You guess the word \'{win_word}\' in {guess_count} tries')


if __name__ == '__main__':
    main()