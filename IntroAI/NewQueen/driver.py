

import time
from queens import Queen
from board import Board


curr_state = Board([],[[]])

goal_score = 0

num_restarts = 0

num_states = 0



curr_state.start_random()




while(True):
    curr_state.calculate_score()
    if(curr_state.score <= goal_score):
        break
    num_neighbors = 0
    best_move = Board(curr_state.qlist.copy(), curr_state.board.copy())
    best_move.calculate_score()
    
   # time.sleep(3)
    for q in range(len(curr_state.qlist)):
        
        for r in range(q+1, curr_state.length):
            
            temp = curr_state.produce_neighbor(q, r)
            temp.calculate_score()
            
            
            if (temp.score < best_move.score):
                best_move = Board(temp.qlist.copy(), temp.board.copy())
                best_move.calculate_score()
                num_neighbors += 1
   
    if (num_neighbors == 0):
        curr_state.print_board()
        print("No Better States Found")
        print("Restarting")
        curr_state = Board([])
        curr_state.start_random()
    else:
        curr_state.print_board()
        print(f"Better Neighbors Found: {num_neighbors}")
        print("SETTING NEW BOARD")
        curr_state = Board(best_move.qlist.copy(), best_move.board.copy())
        curr_state.calculate_score
                
        
        
    
    

curr_state.print_board()
print(f"Solution Found!")
print(f"States Changed: {num_neighbors}")
print(f"Num Restarts: {num_states}")



    