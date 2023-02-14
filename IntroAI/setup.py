
from ast import List
from queens import Queen as q
import numpy as np

class driver():
    current_h_value = 0  #heuristic value
    goal_state = 0
    
    # heuristic, index of queen, positionx, position y
    best_move = [int, int, int, int]

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
            
    def set_queens(self): 
        for qt in self.qlist:
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

    # def find_best_move(self):
    #     best_curr_move = [100, -1, -1, -1]
    #     for qt in range(len(self.qlist)):
            
    #         og_pos = self.qlist[qt].position
    #         best_h = self.current_h_value
            
    #         for r in range(self.board_size):
    #             self.qlist[qt].position[1] = r
    #             temp_h = self.calculate_h()
    #             if (temp_h < best_h):
    #                 best_h = temp_h
    #         if (best_h < best_curr_move[0]):
    #             best_curr_move = [best_h, qt, self.qlist[qt].position[0], self.qlist[qt].position[1]]
    #         self.qlist[qt].position = og_pos
        
    #     self.best_move = best_curr_move
        
                
                
                
                
        
    

    def hill_climb(self):
        while (self.current_h_value != 7):
            best_index = 0
            for qt in range(len(self.qlist)):
                
                
        
                og_pos = self.qlist[qt].position
                best_h = self.current_h_value
                best_pos = [0, 0]
                for r in range(self.board_size):
                    self.qlist[qt].position[1] = r
                    temp_h = self.calculate_h()
                    if (temp_h < best_h):
                        best_h = temp_h
                        best_pos =  self.qlist[qt].position
                self.qlist[qt].position = og_pos
                self.qlist[qt].best_h = best_h
                self.qlist[qt].best_pos = best_pos
                if (self.qlist[qt].best_h <= self.qlist[best_index].best_h):
                    best_index = qt
            
            self.qlist[best_index].position = self.qlist[best_index].best_pos
            board = np.zeros((self.board_size,self.board_size), dtype=int)
            self.set_queens()
            self.current_h_value = self.calculate_h()
            self.print_algorithm(-1)
        print("Found Solution") 
            
                    
        
            
              
                
    def start(self):
        self.generate_queens()
        self.current_h_value = self.calculate_h()
        self.hill_climb()
                
                
            
                
            
                
                    
            

if __name__ == '__main__':
    drive = driver()
   
    drive.initialize_queens()
    drive.start()
    pass
    
    
    
    



