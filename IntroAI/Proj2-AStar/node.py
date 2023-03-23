
class Node:
    
    row, col, f, g, h, parent, isWall = 0, 0, 0, 0, 0, None, False
    
    display = "0"
    
    def __init__(self, row, col, isWall):
        self.row = row
        self.col = col
        self.isWall = isWall
        self.parent = None
        
    def setF(self):
        f = self.g + self.h
    def setG(self, value):
        self.g = value
    def setH(self, value):
        self.h = value
    def setParent(self, n):
        self.parent = n
    
    def getF(self):
        return self.f
    
    def getG(self):
        return self.g
    def getH(self):
        return self.h
    def getParent(self):
        return self.parent
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    
    def equals(self, inNode):
        return self.row == inNode.getRow() and self.col == inNode.getCol()
    
    def setDisplay(self, value):
        self.display = value
    
    
    def __str__(self):
        if (self.isWall):
            self.display = "1"
        return str(self.display)


        
        
    
    
    
