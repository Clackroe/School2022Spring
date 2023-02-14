
from ast import List
from queens import Queen as q
import numpy as np

class driver():
    current_h_value = 0  #heuristic value
    goal_state = 0
    
    best_queen = 0

    #board setup
    board_size = 8;
    board = np.zeros((board_size, board_size), dtype=int) # initial board set to zeros

    #queen setup
    qlist = []

    
    def set_h(self, value):
        self.current_h_value = value
    
    #print the board in a correct format
    def print_board(self):
        print(f"\n   Current h: {self.current_h_value}")
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
        
    def initialize_queens(self): #Creates an initial array of queens, each assigned a collumn
        for i in range(self.board_size):
            self.qlist.append(q(i, 0))
            
    def generate_queens(self): #Takes the position stored by each queen and updates it
        for qt in self.qlist:
            qt.generate_pos()
            self.board[qt.position[0], qt.position[1]] = 1 #Get Queens Stored Location and create queen
            

    def calculate_h(self) -> int: #Calculates the Heuristic Value of the Board/State
        value = 0
        for i in range(len(self.qlist)):
            for j in range(len(self.qlist)):
                if (i == j):
                    pass
                elif(self.compare_queens(self.qlist[i], self.qlist[j])):
                    value+=1
                    break
        return value
                    
    def compare_queens(self, a: q, b: q) -> bool:
        ax: int = a.position[0]
        ay: int = a.position[1]
        bx: int = b.position[0]
        by: int = b.position[1]
        
        
        if (ax == bx): #Same row
            return True
        if (ay == by): #same collumn
            return True
        if (abs(ax-bx) == abs(ay-by)): #Diagonal
            return True
        return False
         
    def print_algorithm(self, neighbors):
        self.print_board()
        print(f"Better Neighbors {neighbors}")

    def calc_better_pos(self) -> int:
        better_neighbors = 0
        btq = 0
        for qt in self.qlist:
            best_pos = [qt.position[0], qt.position[1]]
            og_pos = [qt.position[0], qt.position[1]]
            best_h = self.current_h_value
            
            for r in range(self.board_size):
                qt.position = [qt.position[0], r]
                curr_h = self.calculate_h()
                if (curr_h < best_h):
                    best_h = curr_h
                    best_pos[0] = qt.position[0]
                    best_pos[1] = r
            if (qt.best_h < self.qlist[btq].best_h):
                btq = self.qlist.index(qt)
            qt.position = og_pos
            qt.best_postition = best_pos
            qt.best_h = best_h
            if (qt.best_h < self.current_h_value):
                better_neighbors +=1
        self.best_queen = btq
        return better_neighbors
                
    

    def hill_climb(self):

        if (self.current_h_value == self.goal_state):
            self.print_board()
            print("Found The Solution!!!")
            print(f"State changes: ")
            print(f"Restarts: ")
        else:
            neighbors = self.calc_better_pos()
            self.print_algorithm(neighbors)
            if (neighbors == 0):
                print("RESTARTING")
                self.initialize_queens()
                self.start()
            else:
                print("SETTING NEW CURRENT STATE")
                
                #self.qlist[self.best_queen].position = self.qlist[self.best_queen].best_position
                self.best_queen = 0
                self.start()
                
    def start(self):
        self.generate_queens()
        self.current_h_value = self.calculate_h()
        self.hill_climb()
                
                
            
                
            
                
                    
            

if __name__ == '__main__':
    drive = driver()
   
    drive.initialize_queens()
    drive.start()
    
    



