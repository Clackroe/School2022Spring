#include <iostream>
#include <string>
#include <list>

#include "node.cpp"

using namespace std;

const int boardSize = 15;
const double wallPercent = 0.1;

// Test Variables
int numWalls = 0;
int numNodes = 0;

// Cost of moving Globals
int verticalCost = 10;
int horizontalCost = 10;
int diagonalCost = 14;

list<Node> openList;
list<Node> closedList;

Node board[boardSize][boardSize];

Node startingNode;
Node goalNode;

Node currNode;



// Function Prototypes
void generateGrid(Node grid[boardSize][boardSize]);
void printGrid(Node grid[boardSize][boardSize]);
void getstartingNode(Node grid[boardSize][boardSize]);
void getGoalNode(Node grid[boardSize][boardSize]);
Node getLowestNode();
list<Node> getAdjacentNodes(Node* node);






int main()
{
    // Random Seed
    srand((unsigned)time(NULL));

    // Generate Grid
    generateGrid(board);

   printGrid(board);
    cout << "Walls: " << numWalls << endl;
    cout << "Nodes: " << numNodes << endl;
    cout << "Percent: " << (double)numWalls / numNodes << endl;

    // Get Starting Node
    getstartingNode(board);
    openList.push_back(startingNode);

    // Get Goal Node
    getGoalNode(board);

     // Print Grid
    printGrid(board);
    cout << "Walls: " << numWalls << endl;
    cout << "Nodes: " << numNodes << endl;
    cout << "Percent: " << (double)numWalls / numNodes << endl;


    bool contSearch = true;
    while (contSearch)
    {
        currNode = getLowestNode();
        closedList.push_back(currNode);

        // Check if the current node is the goal
        if (currNode.isEqual(&(goalNode)))
        {
            contSearch = false;
            cout << "Goal Found" << endl;
            // TODO
            break;
        }

        // Get Adjacent Nodes
        list<Node> adjNodes = getAdjacentNodes(currNode);

        // Check if the adjacent nodes are in the closed list
        for (Node an : adjNodes)
        {
            for (Node cn : closedList)
            {
                if (an.isEqual(&cn))
                {
                    // TODO: Remove from Adjacent Nodes IF better path not found
                }
                else{
                    //TODO: Generate G, H, F values
                }
            }
        }
       

    }
}

void generateGrid(Node grid[boardSize][boardSize])
{
    // Generate Grid of Nodes
    for (int i = 0; i < boardSize; i++)
    {
        for (int j = 0; j < boardSize; j++)
        {
            grid[i][j] = Node(i, j, false);
            numNodes++;
        }
    }

    // Generate Walls
    for (int i = 0; i < boardSize; i++)
    {
        for (int j = 0; j < boardSize; j++)
        {
            if (rand() % 100 < wallPercent * 100)
            {
                grid[i][j].setWall(true);
                numWalls++;
            }
        }
    }
}

void printGrid(Node grid[boardSize][boardSize])
{
    for (int i = boardSize-1; 0 <= i; i--)
    {
        for (int j = 0; j < boardSize; j++)
        {
            if (grid[i][j].getWall())
            {
                cout << "X ";
            }
            else if (grid[i][j].isEqual(&startingNode))
            {
                cout << "S ";
            }
            else if (grid[i][j].isEqual(&goalNode))
            {
                cout << "G ";
            }
            
            else
            {
                cout << "O ";
            }
        }
        cout << endl;
    }
}

void getstartingNode(Node grid[boardSize][boardSize])
{
    int row = 0;
    int col = 0;
    bool valid = false;
    while (!valid)
    {
        cout << "Enter Starting Row: ";
        cin >> row;
        cout << "Enter Starting Column: ";
        cin >> col;
        if (row < 0 || row > boardSize || col < 0 || col > boardSize)
        {
            cout << "Invalid Input" << endl;
        }
        else if (grid[row][col].getWall())
        {
            cout << "Invalid Input" << endl;
        }
        else
        {
            valid = true;
        }
    }
    startingNode = grid[row][col];
}

void getGoalNode(Node grid[boardSize][boardSize])
{
    int row = 0;
    int col = 0;
    bool valid = false;
    while (!valid)
    {
        cout << "Enter Goal Row: ";
        cin >> row;
        cout << "Enter Goal Column: ";
        cin >> col;
        if (row < 0 || row > boardSize || col < 0 || col > boardSize)
        {
            cout << "Invalid Input" << endl;
        }
        else if (grid[row][col].getWall())
        {
            cout << "Invalid Input" << endl;
        }
        else
        {
            valid = true;
        }
    }
    goalNode = grid[row][col];
}

Node getLowestNode()
{
    Node lowestF;
    openList.sort();
    lowestF = openList.front();
    openList.pop_front();
    return lowestF;
}

list<Node> getAdjacentNodes(Node node)
{
    list<Node> adjNodes;
    int row = node.getRow();
    int col = node.getCol();

    // Check if the node is on the edge of the board
    if (row == 0)
    {
        // Check if the node is in the corner of the board
        if (col == 0)
        {
            // Check if the node is in the corner of the board
            adjNodes.push_back(board[row][col + 1]);
            adjNodes.push_back(board[row + 1][col]);
            adjNodes.push_back(board[row + 1][col + 1]);
        }
        else if (col == boardSize - 1)
        {
            adjNodes.push_back(board[row][col - 1]);
            adjNodes.push_back(board[row + 1][col]);
            adjNodes.push_back(board[row + 1][col - 1]);
        }
        else
        {
            adjNodes.push_back(board[row][col - 1]);
            adjNodes.push_back(board[row][col + 1]);
            adjNodes.push_back(board[row + 1][col]);
            adjNodes.push_back(board[row + 1][col - 1]);
            adjNodes.push_back(board[row + 1][col + 1]);
        }
    }
    else if (row == boardSize - 1)
    {
        // Check if the node is in the corner of the board
        if (col == 0)
        {
            adjNodes.push_back(board[row - 1][col]);
            adjNodes.push_back(board[row - 1][col + 1]);
            adjNodes.push_back(board[row][col + 1]);
        }
        else if (col == boardSize - 1)
        {
            adjNodes.push_back(board[row - 1][col]);
            adjNodes.push_back(board[row - 1][col - 1]);
            adjNodes.push_back(board[row][col - 1]);
        }
        else
        {
            adjNodes.push_back(board[row][col - 1]);
            adjNodes.push_back(board[row][col + 1]);
            adjNodes.push_back(board[row - 1][col]);
            adjNodes.push_back(board[row - 1][col - 1]);
            adjNodes.push_back(board[row - 1][col + 1]);
        }
    }
    else if (col == 0)
    {
        adjNodes.push_back(board[row - 1][col]);
        adjNodes.push_back(board[row - 1][col + 1]);
        adjNodes.push_back(board[row][col + 1]);
        adjNodes.push_back(board[row + 1][col]);
        adjNodes.push_back(board[row + 1][col + 1]);

        return adjNodes;
    }
    else if (col == boardSize - 1)
    {
        adjNodes.push_back(board[row - 1][col]);
        adjNodes.push_back(board[row - 1][col - 1]);
        adjNodes.push_back(board[row][col - 1]);
        adjNodes.push_back(board[row + 1][col]);
        adjNodes.push_back(board[row + 1][col - 1]);
    }
    else
    {
        adjNodes.push_back(board[row - 1][col]);
        adjNodes.push_back(board[row - 1][col - 1]);
        adjNodes.push_back(board[row - 1][col + 1]);
        adjNodes.push_back(board[row][col - 1]);
        adjNodes.push_back(board[row][col + 1]);
        adjNodes.push_back(board[row + 1][col]);
        adjNodes.push_back(board[row + 1][col - 1]);
        adjNodes.push_back(board[row + 1][col + 1]);
    }
    return adjNodes;
    

}

bool isInClosedList(Node node)
{
    
    for (Node n : closedList)
    {
        if(node.isEqual(&n))
        {
            return true;
        }
    }

    return false;
}