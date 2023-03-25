
class Node:
    
    def __init__(self, x, y, isWall):
        self.x = x
        self.y = y
        self.isWall = isWall
        self.parent = None
        self.g = 0
        self.h = 0
        self.isGoal = False
        self.isStart = False
        self.isPath = False
        self.isAgent = False
        self.f = 0
    
    def calcH(self, goal):
        self.h = (abs(self.x - goal.x) + abs(self.y - goal.y)) * 10
    
    def calcG(self): 
        if self.x == self.parent.x or self.y == self.parent.y:
            self.g = self.parent.g + 10
        else:
            self.g = self.parent.g + 14
        
    def calcF(self):
        self.f = self.g + self.h

        
        
    
    
    
