from typing import Callable

class bg_colors:
    HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\u001b[33m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[96m'

class Mastermind:
    @staticmethod
    def input_valid_win_num() -> int:
        from getpass import getpass
        num: int = -1
        while True:
            if num >= 10: return num
            
            try: 
                num: int = int(getpass(prompt='Enter a multi-digit (>=10) number (hidden): '))
            except ValueError: 
                num = -1
                continue
    
    @staticmethod
    def input_valid_guess() -> int:
        """
        Fn takes a valid guess number
        >>> input_valid_guess()
        """
        num: int = -1
        while True:            
            try: 
                num: int = int(input('Enter a guess: '))
                assert num >= 0, 'Number should be greater than 0'
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

            for i in range(len(str_guess)):
                try: str_win[i]
                except:
                    break

                if str_guess[i] == str_win[i]:
                    print(f'{bg_colors.GREEN}{str_guess[i]}{bg_colors.ENDC}', end='')
                elif str_guess[i] in str_win:
                    print(f'{bg_colors.YELLOW}{str_guess[i]}{bg_colors.ENDC}', end='')
                else:
                    print(f'•', end='')
                
            print('\n')

            return -1
        
        return match_guess

    @staticmethod
    def half_game(A: str, B: str) -> None:

        print(f'Player {A},')
        win_num: int = Mastermind.input_valid_win_num()
        match_guess: Callable = Mastermind.match_guess_and_win(win_num)

        print('\n')
        
        print(f'Player {B},')
        print(f'The number has {len(str(win_num))} digits.')

        tries: int = 0
        while True:
            guess_num: int = Mastermind.input_valid_guess()

            tries += 1

            if match_guess(guess_num) == 1:
                print(f'Hooray! You guessed the number in {tries} tries Player {B}.')
                break

        return tries

    @staticmethod
    def play_game(A: str, B: str) -> None:
        print(f'{A}, it\'s your turn!')
        tries_1: int = Mastermind.half_game(A, B)

        print(f'Now {A} will guess the number.')
        tries_2: int = Mastermind.half_game(B, A)

        if tries_1 == tries_2: print(f'Alas! It\'s a tie')
        else:
            winner: str|None = None
            if tries_1 > tries_2: winner = A
            elif tries_1 < tries_2: winner = B

            print(f'{bg_colors.GREEN}Superb! {winner} wins the game.{bg_colors.ENDC}')

        print('\n')



if __name__ == '__main__':

    playing: bool = True
    while playing:
        Mastermind.play_game('Ram', 'Shyam')
        print('\nAnother game? 1 or 0')
        if int(input()) == 0: playing = False

    print('Thanks for playing!')