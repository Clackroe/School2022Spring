

# import time
# from queens import Queen
# from board import Board


# curr_state = Board([])

# goal_score = 0

# num_states = 0
# num_neighbors = 0



# curr_state.start_random()


# curr_state.produce_neighbor
            
        
    
        
                


# curr_state.print_board()
# print(f"Solution Found!")
# print(f"States Changed: {num_neighbors}")
# print(f"Num Restarts: {num_states}")
import time
from queens import Queen
from board import Board


def hill_climbing(state):
    global num_states, num_neighbors
    
    num_states = 0
    num_neighbors = 0
    
    # Initialize the current state
    current = state
    current.calculate_score()
    num_states += 1
    
    while True:
        # Generate all neighbors of the current state
        neighbors = []
        for i in range(Board.length):
            for j in range(Board.length):
                if current.qlist[i].posy != j:
                    neighbors.append(current.produce_neighbor(i, j))
        
        # Calculate the scores of all the neighbors
        for neighbor in neighbors:
            neighbor.calculate_score()
            num_neighbors += 1
        
        # Choose the best neighbor as the new current state
        best = min(neighbors, key=lambda x: x.score)
        
        if best.score >= current.score:
            # No better neighbor, return the current state as the solution
            return current
        else:
            # Update the current state with the best neighbor
            current = best
            num_states += 1

curr_state = Board([])

goal_score = 0

num_states = 0
num_neighbors = 0

curr_state.start_random()
curr_state.print_board()

hill_climbing(curr_state)
    

print(f"Solution Found!")
print(f"States Changed: {num_states}")
print(f"Num Neighbors Checked: {num_neighbors}")



    