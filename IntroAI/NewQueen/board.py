
import string
from queens import Queen
from ast import List
import numpy as np

class Board():
    
    score:int = 0
    length = 8
    
    qlist = []
    
    board = [[]]
    
    
    def __init__(self, list): #Create with predefined list
        self.qlist = list
        self.board = np.zeros((self.length, self.length), dtype=int)
        
    
    
    
    def create_queens(self):
        for i in range(self.length):
            q = Queen(i, 0)
            self.qlist.append(q)
    
    def randomize_queens(self):
        for q in self.qlist:
            q.generate_random_pos()
            
    def place_queens(self):
       for q in self.qlist:
           self.board[q.posx][q.posy] = 1
           
    def calculate_score(self):
        value = 0
        for q1 in self.qlist:
            for q2 in self.qlist:
                if (q1 == q2):
                    pass
                elif(q1.compare_queen(q2)):
                    value+=1
                    break
        self.score = value
           
           
    def start_random(self):
        self.create_queens()
        self.randomize_queens()
        self.place_queens()
        self.calculate_score()
    
    def start(self):
        self.place_queens()
        self.calculate_score()
    
    def print_board(self):
        print(f"\n   Current h: {self.score}")
        print(" --Current State---------")
        for i in range(self.length):
            print("| ", end="")
            for j in range(self.length):
                if (j==self.length-1):
                    print(self.board[j][i], end=" |")
                else:
                    print(f"{self.board[j][i]},", end=" ")
            print()
        print(" ------------------------")
        
        
    def produce_neighbor(self, ind: int, row: int):
        
        list = []
        for q in self.qlist:
            list.append(q)
            
        list[ind].posy = row
    
        ret = Board(list)
        ret.place_queens()
        return ret
    
    
        