import random as rand

class Queen():
    
    position = [0, 0]
    
    def __init__(self, x:int, y:int):
       self.position = [x, y]
    


    def generate_pos(self):
        self.position[1] = rand.randint(0, 7)
                    

    
   
    