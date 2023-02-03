
from queens import Queen as q
import numpy as np

class driver():
    h_value = 0  #heuristic value

    #board setup
    board_size = 8;
    board = np.zeros((board_size, board_size), dtype=int) # initial board set to zeros

    #queen setup
    qlist:q = []

    #print the board in a correct format
    def print_board(self):
        print(f"\n   Current h: {self.h_value/2}")
        print(" --Current State---------")
        for i in reversed(range(self.board_size)):
            print("| ", end="")
            for j in range(self.board_size):
                if (j==self.board_size-1):
                    print(self.board[j][i], end=" |")
                else:
                    print(f"{self.board[j][i]},", end=" ")
            print()
        print(" ------------------------")
        
    
    def generate_queens(self):
        for qt in self.qlist:
            qt.generate_pos()
            self.board[qt.position[0], qt.position[1]] = 1
            
    def initialize_queens(self):
        for i in range(self.board_size):
            self.qlist.append(q(i, 0))

    def calculate_h(self):
        for i in range(len(self.qlist)):
            for j in range(len(self.qlist)):
                if (i == j):
                    pass
                elif(self.compare_queens(self.qlist[i], self.qlist[j])):
                    self.h_value+=1
                    break;
                    
    def compare_queens(self, a: q, b: q) -> bool:
        ax: int = a.position[0]
        ay: int = a.position[1]
        bx: int = b.position[0]
        by: int = b.position[1]
        
        #Same row
        if (ax == bx):
            return True
        #same collumn
        if (ay == by):
            return True
        #Diagonal
        if (abs(ax-bx) == abs(ay-by)):
            return True
        return False
                    

            

if __name__ == '__main__':
    drive = driver()
    drive.initialize_queens()
    drive.generate_queens()
    drive.calculate_h()
    drive.calculate_h()
    drive.print_board()
        



