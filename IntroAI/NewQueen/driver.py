

import time
from queens import Queen
from board import Board


curr_state = Board([])

goal_score = 0

num_states = 0
num_neighbors = 0



curr_state.start_random()


while (True):
    for q in range(curr_state.length):
        
        for r in range(curr_state.length):
            temp = curr_state.produce_neighbor(q, r)
            temp.calculate_score()
            temp.print_board()
    break
            
        
    
        
                


curr_state.print_board()
print(f"Solution Found!")
print(f"States Changed: {num_neighbors}")
print(f"Num Restarts: {num_states}")




    