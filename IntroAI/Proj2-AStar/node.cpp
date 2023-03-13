#include <iostream>
#include <string>


using namespace std;

class Node{
    private:
        //Values for the node
        int f; //Total cost
        int h; //Heuristic cost
        int g; //Movement cost 

        bool isWall; //Is the node a wall
        bool isPath;

        Node* parent = NULL; //Parent Node

        //Position of the node
        int col = 150;//Column
        int row = 150;//Row

    public:
        //Constructor
        Node(){
            f = 0;
            h = 0;
            g = 0;
            isWall = false;
            parent = NULL;
            }

        Node(int r, int c, bool wall){
            row = r;
            col = c;
            isWall = wall;
            parent = NULL;
        }

        //Getters
        int getF(){return f;}
        int getH(){return h;}
        int getG(){return g;}
        int getCol(){return col;}
        int getRow(){return row;}
        bool getWall(){return isWall;}
        bool getPath(){return isPath;}
        Node* getParent(){return parent;}

        //Setters
        void setF(){
            f = g + h;
        }
        void setH(int value){
            h = value;
        }
        void setG(int value){
            g = value;
        }
        void setParent(Node* p){
            parent = p;
        }
        void setWall(bool wall){
            isWall = wall;
        }
        void setPath(bool path){
            isPath = path;
        }
        void setCol(int c){
            col = c;
        }
        void setRow(int r){
            row = r;
        }

        bool isEqual(Node* n){
             return (n->getRow() == row && n->getCol() == col);
        }

        bool operator<(const Node& n) const{
            return f < n.f;
        }

        bool operator==(const Node& n) const{
            return (row == n.row && col == n.col);

        }


        //To String
        string toString(){
            string s = "Node: " + to_string(row) + " " + to_string(col) + " F: " + to_string(f) + " H: " + to_string(h) + " G: " + to_string(g);
            return s;
        }



    





};