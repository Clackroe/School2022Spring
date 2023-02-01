import random as rand

class Queen:
    
    position = [0, 0]
    
    def __init__(self, x:int, y:int):
       self.position = [x, y]
    
    def compare_queens(self, other) -> bool:
        x = other.position[0]
        y= other.position[1]
        
        
        if (y == self.position[1] or x == self.position[0]):
            return True
        
        elif (y-self.position[1] == x-self.position[0] or self.position[1]-y == self.position[0]-x):
            return True
        else:
            return False


    def generate_pos(self):
        self.position[1] = rand.randint(0, 7)
                    

    
   
    