import numpy

class QueensAI:
           
    
    def setup_board(self, size):
        
        board = numpy.zeros((size, size))
   
    def print_board(self, board):
        for rows in board:
            for value in rows:
                value=0
                print(value, end="")
                print(", ", end="")
            print()

r = QueensAI(8)
r.setup_board()
   
        