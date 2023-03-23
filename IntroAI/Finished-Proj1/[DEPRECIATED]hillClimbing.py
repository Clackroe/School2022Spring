


import random

import numpy as np

class driver():
    
    board_size = 8
    goal_score = 0
    
    num_states = 0

    def main(self):
        
        board = self.randomize_board()
     
        while(True):
            
            neighbors = {}
            if(self.calculate_score(board) == self.goal_score):
                break
            
            for q in range(len(board)):
                
                for row in range(len(board)):
                    if (board[q] != row):
                        temp = board.copy()   #TODO
                        temp[q] = row
                        neighbors[(q, row)] = self.calculate_score(temp)
            best_moves = []
            best_score = self.calculate_score(board)
            
            for q,score in neighbors.items():
                if (score < best_score):
                    best_score = score
                    
            for q, score in neighbors.items():
                if score == best_score and score:
                    best_moves.append(q)
            
            if len(best_moves) > 0:
                rand_num = random.randint(0, len(best_moves)-1)
                q = best_moves[rand_num][0]
                row = best_moves[rand_num][1]
                
                self.print_board(board)
                print(f"Number Of Better Neighbors: {len(best_moves)}")
                print("Setting New Board")
                self.num_states +=1
                
                board[q] = row
            else:
                print("Restarting!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        #SOLUTION FOUND
        self.print_board(board)
        print("SOLUTION FOUND!!")
        print(f"Number of States: {self.num_states}")


    def calculate_score(self, temp:list):
        score = 0
        
        for q in range(len(temp)):
            
            for row in range(q+1, len(temp)):
                
                if temp[q] == temp[row]:
                    score+=1
                    
                row_distance = row - q
                if (temp[q] == (temp[row] - row_distance) or temp[q] == (temp[row] + row_distance)):
                    score+=1
        return score
    
    def print_board(self, input):
        display = np.zeros((self.board_size, self.board_size), dtype=int)
        for q in range(self.board_size):
           display[q][input[q]] = 1
        
        print(f"\n   Current h: {self.calculate_score(input)}")
        print(" --Current State---------")
        for i in range(self.board_size):
            print("| ", end="")
            for j in range(self.board_size):
                if (j==self.board_size-1):
                    print(display[j][i], end=" |")
                else:
                    print(f"{display[j][i]},", end=" ")
            print()
        print(" ------------------------")
    
    def randomize_board(self):
        ret = []
        for i in range(self.board_size):
            ret.append(random.randint(0, self.board_size-1))
        return ret

if __name__ == '__main__':
    drive = driver()
    drive.main()


            