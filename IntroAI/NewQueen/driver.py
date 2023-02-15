

import time
from queens import Queen
from board import Board


curr_state = Board([])

goal_score = 0

num_restarts = 0
num_neighbors = 0
num_states = 0



curr_state.start_random()



loop = True
while (loop):
    
    time.sleep(3)
    neighbors = []
    curr_state.place_queens()
    curr_state.calculate_score()
    if(curr_state.score == goal_score):
        loop = False
        break
    else:
        for q in range(len(curr_state.qlist)):
            
            for r in range (len(curr_state.qlist)):
                temp = curr_state.produce_neighbor(q, r)
                if (temp.score < curr_state.score):
                    neighbors.append(temp)     
        
        if (len(neighbors) <=0):
            curr_state.print_board()
            print(f"No Better Neighbors Found..")
            print("RESTARTING")
            num_restarts +=1
            curr_state = Board([])
            curr_state.start_random()
        else:
            best_neighbor = Board([])
            for n in neighbors:
                if (len(best_neighbor.qlist) == 0):
                    best_neighbor = n
                else:
                    if (n.score < best_neighbor.score):
                        best_neighbor = n
                    
            
            curr_state.print_board()
            print(f"Number of Better Neighbors: {len(neighbors)}")
            print(f"Setting New State...")
            num_states +=1
            curr_state = best_neighbor
            curr_state.start()
        
        
    
    

curr_state.print_board()
print(f"Solution Found!")
print(f"States Changed: {num_neighbors}")
print(f"Num Restarts: {num_states}")



    