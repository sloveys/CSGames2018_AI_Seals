package utils;

import java.util.ArrayList;
import java.util.List;

// Inspired from http://www.peachpit.com/articles/article.aspx?p=101142&seqNum=2

/**
 The AStarNode class, along with the AStarSearch class,
 implements a generic A* search algorithm. The AStarNode
 class should be subclassed to provide searching capability.
 */
public class AStarNode implements Comparable {

    AStarNode pathParent;
    float costFromStart;
    float estimatedCostToGoal;
    private int x;
    private int y;
    private char symbol;
    private ArrayList<AStarNode> neighbors;

    public AStarNode(int p_x, int p_y, char p_symbol){
        x = p_x;
        y = p_y;
        symbol = p_symbol;
        neighbors = new ArrayList<>();
    }

    public void add_neighbor(AStarNode p_node){
        neighbors.add(p_node);
    }

    public float getCost() {
        return costFromStart + estimatedCostToGoal;
    }

    public int getX() {
        return x;
    }

    public int getY(){
        return y;
    }

    public int compareTo(Object other) {
        float thisValue = this.getCost();
        float otherValue = ((AStarNode)other).getCost();

        float v = thisValue - otherValue;
        return (v>0)?1:(v<0)?-1:0; // sign function
    }


    /**
     Gets the cost between this node and the specified
     adjacent (AKA "neighbor" or "child") node.
     */
    public float getCost(AStarNode node){
        return 1;
    }


    /**
     Gets the estimated cost between this node and the
     specified node. The estimated cost should never exceed
     the true cost. The better the estimate, the more
     effecient the search.
     */
    public float getEstimatedCost(AStarNode node){
        return Math.abs(node.getY() - y) + Math.abs(node.getX() - x);
    }


    /**
     Gets the children (AKA "neighbors" or "adjacent nodes")
     of this node.
     */
    public List getNeighbors(){
        return neighbors;
    }

    public char getSymbol() {
        return symbol;
    }
}