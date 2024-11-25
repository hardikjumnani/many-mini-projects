'''

Cows and Bulls is a pen and paper code-breaking game usually played between 2 players. In this, a player tries to guess a secret code number chosen by the second player. The rules are as follows:

- A player will create a secret code, usually a 4-digit number.  This number should have no repeated digits.
- Another player makes a guess (4 digit number) to crack the secret number. Upon making a guess, 2 hints will be provided- Cows and Bulls.
- Bulls indicate the number of correct digits in the correct position and cows indicates the number of correct digits in the wrong position. For example, if the secret code is 1234 and the guessed number is 1246 then we have 2 BULLS (for the exact matches of digits 1 and 2) and 1 COW (for the match of digit 4 in the wrong position)
- The player keeps on guessing until the secret code is cracked. The player who guesses in the minimum number of tries wins.
'''
from typing import Callable

class CowsAndBulls:
    @staticmethod
    def input_valid_win_num() -> int:
        from getpass import getpass
        num: int = -1
        while True:
            if len(str(num)) == 4:
                if len(set(str(num))) == 4: return num
                else: print('The number doesn\'t have distinct digits')
            else: print('The number wasn\'t 4 digits long.')
            
            try: 
                num: int = int(getpass(prompt='Enter a 4-digit number with distinct digits (hidden): '))
            except ValueError: 
                num = -1
                continue
    
    @staticmethod
    def input_valid_guess() -> int:
        num: int = -1
        while True:
            try: 
                num: int = int(input('Enter a guess: '))
                assert num >= 0, 'Number should be greater than 0.'
                assert len(str(num)) == 4, 'Number should be of 4-digits.'
                assert len(set(str(num))) == 4, 'Number should have distinct digits.'
            except ValueError:
                num = -1
                print('Number not found.')
                continue
            except Exception as e:
                num = -1
                print(e)
                continue
                
            return num
    
    @staticmethod
    def match_guess_and_win(win: int) -> Callable:
        def match_guess(guess: int) -> int:
            if win == guess: return 1

            str_win, str_guess = str(win), str(guess)

            cows, bulls = 0, 0
            for i in range(len(str_guess)):
                if str_guess[i] == str_win[i]:
                    bulls += 1
                elif str_guess[i] in str_win:
                    cows += 1
                
            print(f'{bulls} bulls, {cows} cows')

            return -1
        
        return match_guess

    @staticmethod
    def play_game(A: str, B: str) -> None:

        print(f'Player {A},')
        win_num: int = CowsAndBulls.input_valid_win_num()
        match_guess: Callable = CowsAndBulls.match_guess_and_win(win_num)

        print('\n')
        
        print(f'Player {B},')
        print(f'Guess the 4-digits')

        tries: int = 0
        while True:
            guess_num: int = CowsAndBulls.input_valid_guess()

            tries += 1

            if match_guess(guess_num) == 1:
                print(f'Hooray Player {B}! You guessed the number in {tries} tries.')
                break

        return tries
    
if __name__ == '__main__':

    playing: bool = True
    while playing:
        CowsAndBulls.play_game('Ram', 'Shyam')
        print('\nAnother game? 1 or 0')
        if int(input()) == 0: playing = False

    print('Thanks for playing!')