from typing import Any
from random import randint

def int_input(dialog: str = '') -> Any:
    while True:
        try:
            inp = input(dialog)
            if inp == '': raise Exception('You entered a blank input. Try again.')

            inp = int(inp)
            return inp
    
        except ValueError:
            print('Your number was not an integer. Try again.')
        except Exception as e:
            print(e)

def main():
    a = int_input('Enter first value of range. ')
    b = int_input('Enter last value of range. ')

    if a > b:
        print('Your first value was greater than the last value, swapping it.')
        a, b = b, a

    guess_count: int = 0
    guess: int = -100000
    win_number: int = randint(a, b)

    while guess != win_number:
        guess = int_input('Take a guess. ')
        guess_count += 1
    
    print('You guessed the number in', guess_count, 'tries!')

if __name__ == '__main__':
    main()