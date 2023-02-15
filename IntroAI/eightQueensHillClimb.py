
from ast import List
import random
import numpy as np


class driver():

    board_size = 8
    
    goal_score = 0
    
    num_restarts = 0
    num_states = 0
    
    

    def main(self):

        curr_state = []
        curr_state = self.randomise_board()
        
        

          
        while(True):
            
            if (self.calcuate_score(curr_state) == self.goal_score):
                break
            else:
                
                neighbors = []
                
                for q in range(len(curr_state)):
                    
                    for row in range(len(curr_state)):
                        temp = list(curr_state)
                        temp[q] = row
                        temp_score = self.calcuate_score(temp)
                        if (temp_score < self.calcuate_score(curr_state)):
                            neighbors.append([q, row, temp_score])
                if (len(neighbors) > 0):
                    best_state = [0, 0, 1000]
                    for s in range(len(neighbors)):
                        if (neighbors[s][2] < best_state[2]):
                            best_state = neighbors[s]
                    
                    
                    print(f"-Current State - Score: {self.calcuate_score(curr_state)}-")
                    self.print_board(curr_state)
                    print(f"Number of Better Neighbors: {len(neighbors)}")
                    print("Setting New Board\n")
                    self.num_states +=1
                    curr_state[best_state[0]] = best_state[1]
                else:
                    print(f"-Current State - Score: {self.calcuate_score(curr_state)}-")
                    self.print_board(curr_state)
                    print(f"No Better Neighbors Found: {len(neighbors)} neighbors")
                    print("Restarting\n")
                    self.num_restarts +=1
                    curr_state = []
                    curr_state = self.randomise_board()
        
        print("_________Solution_________")
        self.print_board(curr_state)
        print("Solution Found!!")
        print(f"Number of States Changed: {self.num_states}")
        print(f"Number of Restarts: {self.num_restarts}")




    def calcuate_score(self, input):
        score = 0
        for q in range(len(input)):
            for q2 in range(q+1, len(input)):

                if input[q] == input[q2]:
                    score += 1

                if input[q] == input[q2] - (q - q2) or input[q] == input[q2] + (q - q2):
                    score += 1
        return score


    def randomise_board(self):
        input = []
        for i in range(self.board_size):
            input.append(random.randint(0, self.board_size-1))
        return input
    

    def print_board(self, input):
        board = np.zeros((self.board_size, self.board_size), dtype=int)
        for q in range(self.board_size):
            board[input[q]][q] = 1
        for i in reversed(range(self.board_size)):
            print("| ", end="")
            for j in range(self.board_size):
                if(j == self.board_size-1):
                    print(f"{board[i][j]}", end=" |")
                else:
                    print(f"{board[i][j]},", end=" ")
            print("")
            


if __name__ == '__main__':
    drive = driver()
    drive.main()
