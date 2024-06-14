# generate a random 2 if an empty position (.) exists, else end game
# double numbers if same and collide in a move
from typing import List
from random import randint

legal_moves = ['w', 'a', 's', 'd']
def legal_move_input(dialog):
    while True:
        move: str = input(dialog)
        if move.lower() in legal_moves: return move.lower()
        else: print('You entered invalid move, the legal moves are', legal_moves)

# Define ANSI escape sequences for text colors
class TextColors:
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    RESET = '\033[0m'  # Reset to default color

class Board_2048:
    def __init__(self, n=4):
        self._n: int = n
        self._board: List[List] = [['.' for _ in range(self._n)] for _ in range(self._n)]
        self._final_score: int = 0
        self._latest_2: List[int, int] = []

        r_i = randint(0, self._n - 1)
        r_j = randint(0, self._n - 1)
        self._latest_2 = [r_i, r_j]
        self._board[r_i][r_j] = '2'
    
    def place_random_2(self):
        count: int = 0
        max_count: int = self._n ** 2
        while True:
            r_i = randint(0, self._n - 1)
            r_j = randint(0, self._n - 1)
            if self._board[r_i][r_j] == '.':
                self._latest_2 = [r_i, r_j]
                self._board[r_i][r_j] = '2'
                break
            elif count >= max_count:
                max_num = 0
                for i in range(self._n):
                    for j in range(self._n):
                        if self._board[i][j] == '.':
                            self._board[i][j] = '2'
                            break
                        else:
                            if int(self._board[i][j]) > max_num:
                                max_num = int(self._board[i][j])
                else:
                    self._final_score = max_num
                    return 'game_over'

            else:
                count += 1
                continue
    
    def print_board(self):
        for i in range(self._n):
            for j in range(self._n):
                if i == self._latest_2[0] and j == self._latest_2[1]: print(f'{TextColors.GREEN}{self._board[i][j]}{TextColors.RESET}', end=' ')
                else: print(self._board[i][j], end=' ')
            print()
        print()
    
    def move_elems(self, temp_arr: List, positive: bool) -> List:
        if temp_arr == ['.', '.', '.', '.']: return temp_arr

        try: 
            while True:
                temp_arr.remove('.')
        except ValueError:
            pass

        if positive:
            skip_next = False
            for i in range(len(temp_arr)-1, 0, -1):
                if skip_next == True: 
                    skip_next = False
                    continue
                try:
                    if temp_arr[i] == temp_arr[i-1] and temp_arr[i] != '.':
                        temp_arr[i-1] = str(int(temp_arr[i-1]) * 2)
                        temp_arr.pop(i)
                        skip_next = True
                except IndexError: pass

        else:
            skip_next = False
            for i in range(len(temp_arr)-1):
                if skip_next == True: 
                    skip_next = False
                    continue
                try:
                    if temp_arr[i] == temp_arr[i+1] and temp_arr[i] != '.':
                        temp_arr[i] = str(int(temp_arr[i]) * 2)
                        temp_arr.pop(i+1)
                        skip_next = True
                except IndexError: pass


        while len(temp_arr) < self._n:
            if positive: temp_arr.append('.')
            else: temp_arr.insert(0, '.')
        
        return temp_arr

    def up(self) -> str|None:
        for j in range(self._n):
            temp_arr = []
            for i in range(self._n):
                temp_arr.append(self._board[i][j])

            temp_arr = self.move_elems(temp_arr, positive=True)

            for i in range(self._n):
                self._board[i][j] = temp_arr[i]
        
        return self.place_random_2()

    def down(self): 
        for j in range(self._n):
            temp_arr = []
            for i in range(self._n):
                temp_arr.append(self._board[i][j])

            temp_arr = self.move_elems(temp_arr, positive=False)

            for i in range(self._n):
                self._board[i][j] = temp_arr[i]
        
        return self.place_random_2()

    def left(self): 
        for i in range(self._n):
            temp_arr = []
            for j in range(self._n):
                temp_arr.append(self._board[i][j])

            temp_arr = self.move_elems(temp_arr, positive=True)

            for j in range(self._n):
                self._board[i][j] = temp_arr[j]
        
        return self.place_random_2()

    def right(self): 
        for i in range(self._n):
            temp_arr = []
            for j in range(self._n):
                temp_arr.append(self._board[i][j])

            temp_arr = self.move_elems(temp_arr, positive=False)

            for j in range(self._n):
                self._board[i][j] = temp_arr[j]
        
        return self.place_random_2()


if __name__ == '__main__':
    print('RULES')
    print('Use w, a, s, d to perform up, left, down, right moves respectively')
    print('The game is over once you have no more places to place a new "2"')
    print('Your high score will be the largest tile in the game.')
    print('Best Of Luck')
    print('vvvvvvvvvvvvvvvvvvv')

    board = Board_2048()
    board.print_board()

    not_lost: bool = True
    final_score: int = 0
    while not_lost:
        new_move: str = legal_move_input('Perform your move. ')
        if new_move == 'w': 
            if board.up() == 'game_over':
                not_lost = False
        if new_move == 'a': 
            if board.left() == 'game_over':
                not_lost = False
        if new_move == 's': 
            if board.down() == 'game_over':
                not_lost = False
        if new_move == 'd': 
            if board.right() == 'game_over':
                not_lost = False
        
        board.print_board()
    
    print('Game Over')
    print('Your final score is', board._final_score)