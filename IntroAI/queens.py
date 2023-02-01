class Queen:
    
    position = [int]
    
def compareQueens(self, other : Queen) -> bool:
    x = other.position[0]
    y= other.position[1]
    
    
    if (y == self.position[1] or x == self.position[0]):
        return True
    
    elif (y-self.position[1] == x-self.position[0] or self.position[1]-y == self.position[0]-x):
        return True
    else:
        return False
        
                    

    
   
    