from node import Node
import numpy as np


boardSize = 15
    
board = [[Node(row, col, False) for col in range(boardSize)] for row in range(boardSize)]

def main():
    
    
    
   
    displayBoard(board)
    
    
    startingNode = getStartingNodeFromUser()
    startingNode.setDisplay("S")
    
    goalNode = getGoalNodeFromUser()
    goalNode.setDisplay("G")
    
    displayBoard(board)
    
    
    
    
   
   
    #this is an implementation of the A* algorithm
    openList = []
    closedList = []
    
    


def initializeBoard(board):
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            board[row, col] = Node(row, col, False)

def getStartingNodeFromUser():
    print("Please enter the starting node")
    startRow = int(input("Enter the row: "))
    startCol = int(input("Enter the column: "))
    board[startRow, startCol] = "S"
    return Node(startRow, startCol, False)

def getGoalNodeFromUser():
    print("Please enter the goal node")
    goalRow = int(input("Enter the row: "))
    goalCol = int(input("Enter the column: "))
    board[goalRow, goalCol] = "G"
    return Node(goalRow, goalCol, False)

def displayBoard(board):
    for i in reversed(range(boardSize)):
            print("| ", end="")
            for j in range(boardSize):
                if(j == boardSize-1):
                    print(f"{board[i][j]}", end=" |")
                else:
                    print(f"{board[i][j]},", end=" ")
            print("")    
   
    
    
    
        
    
    

if __name__ == '__main__':
    main()
    