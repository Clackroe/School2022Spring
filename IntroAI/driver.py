
from queens import Queen as q
import numpy as np

h_value = 0  #heuristic value

#board setup
board_size = 8;
board = np.zeros((board_size, board_size), dtype=int) # initial board set to zeros

#queen setup
qlist:q = []


def main():

    initialize_queens()
    h_value = calculate_h()
    generate_queens()
    calculate_h()
    print_board()




#print the board in a correct format
def print_board():
    print(f"\n   Current h: {h_value}")
    print(" --Current State---------")
    for i in reversed(range(board_size)):
        print("| ", end="")
        for j in range(board_size):
            if (j==board_size-1):
                print(board[j][i], end=" |")
            else:
                print(f"{board[j][i]},", end=" ")
        print()
    print(" ------------------------")
    
   
def generate_queens():
    for qt in qlist:
        qt.generate_pos()
        board[qt.position[0], qt.position[1]] = 1
        
def initialize_queens():
    for i in range(board_size):
        qlist.append(q(i, 0))

def calculate_h() -> int:
    val = 0
    for i in range(len(qlist)):
        for j in range(len(qlist)):
            if (i == j):
                pass
            elif(qlist[i].compare_queens(qlist[j])):
                val+=1
    return val
                

        

if __name__ == '__main__':
    main()
    



