import random as rand

class Queen():
    
    posx = 0
    posy = 0
    
    
    def __init__(self, x:int, y:int):
      self.posx = x
      self.posy = y
    


    def generate_random_pos(self): #Randomized their y position to a random row
        self.posy = rand.randint(self.posx, 7)
        
    def compare_queen(self, q) -> bool:
        bx: int = q.posx
        by: int = q.posy
        
        if (self.posx == bx): #Same row
            return True
        if (self.posy == by): #same collumn
            return True
        if (abs(self.posx-bx) == abs(self.posy-by)): #Diagonal
            return True
        return False
                    

    
   
    