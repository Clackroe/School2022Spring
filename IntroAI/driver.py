
from queens import Queen as q

import numpy as np

h_value = 0 #heuristic value

#board setup
board_size = 8;
board = np.zeros((board_size, board_size), dtype=int) # initial board set to zeros

#queen setup
qlist:q = []


def main():
    initialize_queens()
    
    generate_queens()
    
    
    
    print_board()




#print the board in a correct format
def print_board():
    for i in reversed(range(board_size)):
        for j in range(board_size):
            if (j==board_size-1):
                print(board[j][i], end="")
            else:
                print(f"{board[j][i]},", end=" ")
        print()
   
def generate_queens():
    for qt in qlist:
        qt.generate_pos()
        board[qt.position[0], qt.position[1]] = 1
        


def initialize_queens():
    for i in range(board_size):
        qlist.append(q(i, 0))


if __name__ == '__main__':
    main()
    



