import random
import time
from node import Node

board_size = 15
wall_prob = 0.1



def main():
        
    world = generateGrid()
    
    #Testing for fail case
    # for x in range(board_size):
    #     world[x][5].isWall = True
    
    startCoord, goalCoord = userSelectStartGoal(world)
    world[startCoord[0]][startCoord[1]].isStart = True
    startNode = world[startCoord[0]][startCoord[1]]
    startNode.isWall = False
    world[goalCoord[0]][goalCoord[1]].isGoal = True
    goalNode = world[goalCoord[0]][goalCoord[1]]
    goalNode.isWall = False
    
    
   
    path = aStarAlgorithm(world, startNode, goalNode)
    
    printGrid(world)
    
    if(path == None):
        print("No path was found")
    else:
        #print the path
        print("Path:", end=" ")
        for p in path:
            print("(" + str(p.x) + ", " + str(p.y) + ")", end=" ")
        print("\nPath Length: " + str(len(path)) + " nodes")
        
    print("Wall to Node Ratio: " + str(calculatWallToNodeRatio(world)))
    
    
    #ask whether to animate the path
    while True:
        answer = input("\033[1;31m" + "Do you want to see it animated? (y/n) "+ "\033[0m").lower()
        if answer == "y":
            animateTraversal(world, path)
            break
        elif answer == "n":
            print("Okay, bye!")
            break
        else:
            print("Please enter either 'yes' or 'no'")
    
    
    
    
    
    



def animateTraversal(grid, path):
    for x in range(len(path)):
        print(chr(27) + "[2J")
        grid[path[x].x][path[x].y].isAgent = True
        printGrid(grid)
        time.sleep(0.5)
        grid[path[x].x][path[x].y].isAgent = False
    

def calculateLowestF(openList):
    lowestF = openList[0].f
    lowestNode = openList[0]
    for node in openList:
        if (node.f < lowestF):
            lowestF = node.f
            lowestNode = node
    return openList.index(lowestNode)

def generatePath(node):
    path = []
    while (node.parent != None):
        path.append(node)
        node.isPath = True
        node = node.parent
    path.append(node)
    node.isPath = True
    return path[::-1]

def generateGrid():
    grid = [[Node(x, y, False) for y in range(board_size)] for x in range(board_size)]
    #assign walls
    for x in range(board_size):
        for y in range(board_size):
            if random.random() < wall_prob:
                grid[x][y].isWall = True
           
    return grid

def getNeighbors(grid, node): 
    x, y = node.x, node.y
    neighbors = []
    
    for xOffset in range(-1, 2):
        for yOffset in range(-1, 2):
            if xOffset == 0 and yOffset == 0:
                continue
            newX = x + xOffset
            newY = y + yOffset
            if 0 <= newX < board_size and 0 <= newY < board_size and not grid[newX][newY].isWall:
                neighbors.append(grid[newX][newY])
    return neighbors    
    
    


def userSelectStartGoal(grid):
    print("Select start and goal positions")
    start = None
    goal = None
    while start is None or goal is None:
        printGrid(grid)
        print("Enter start position (x,y): ")
        start = input()
        print("Enter goal position (x,y): ")
        goal = input()
        try:
            start = start.split(",")
            goal = goal.split(",")
            start = (int(start[0]), int(start[1]))
            goal = (int(goal[0]), int(goal[1]))
            if grid[start[0]][start[1]].isWall or grid[goal[0]][goal[1]].isWall:
                print("Invalid start or goal position")
                start = None
                goal = None
            else:
                grid[start[0]][start[1]].isStart = True
                grid[goal[0]][goal[1]].isGoal = True
        except:
            print("Invalid start or goal position")
            start = None
            goal = None
    return start, goal


def calculatWallToNodeRatio(grid):
    wallCount = 0
    for x in range(board_size):
        for y in range(board_size):
            if grid[x][y].isWall:
                wallCount += 1
    return wallCount / (board_size * board_size)

def printGrid(grid):
    for x in reversed(range(board_size)):
        for y in range(board_size):
            if grid[x][y].isAgent:
                print("\033[1;33m" + "A" + "\033[0m", end=" ")
            elif grid[x][y].isWall:
                print("\033[1;31m" + "X" + "\033[0m" , end=" ")
            elif grid[x][y].isStart:
                print("\033[1;36m" + "S" + "\033[0m", end=" ")
            elif grid[x][y].isGoal:
                print("\033[1;35m" + "G" + "\033[0m", end=" ")
            elif grid[x][y].isPath:
                print("\033[1;32m" + "P" + "\033[0m", end=" ")
            else:
                print("0" + "\033[0m", end=" ")
        print()
        

def aStarAlgorithm(world, startNode, goalNode):
    openList = []
    closedList = []
    
    
    
    #add start node to open list
    openList.append(startNode)
    
    
    #while open list is not empty
    
    while (len(openList) > 0):
        
        printGrid(world)
        print("Open List: " + str(len(openList)))
        print("Closed List: " + str(len(closedList)))
    
        #get node with lowest f value from open list   
        #remove node from open list
        #add node to closed list
        currentNode = openList.pop(calculateLowestF(openList))
        closedList.append(currentNode)
        
        #if node is goal, return path
        if (currentNode == goalNode):
            print("\n\033[1;32m" +"Goal Reached!!"+ "\033[0m")
            # print("Current Node: " + str(currentNode.x) + ", " + str(currentNode.y))
            # print("Goal Node: " + str(goalNode.x) + ", " + str(goalNode.y))
            return generatePath(currentNode)
        
        #get neighbors of node
        neighbors = getNeighbors(world, currentNode)
        
        #for each neighbor
        for n in neighbors:
            #if neighbor is in closed list, continue
            if (n in closedList):
                continue
            else:
                #generate g, h, and f value for neighbor
                n.parent = currentNode
                n.calcG()
                n.calcH(goalNode)
                n.calcF()
                
                #if neighbor is in open list
                if (n in openList):
                    #if neighbor's g value is lower than current g value
                    if (n.g < currentNode.g):
                        #add neighbor to open list
                        openList.append(n)
                else:
                    #add neighbor to open list
                    openList.append(n)

        
if __name__ == "__main__":
    main()