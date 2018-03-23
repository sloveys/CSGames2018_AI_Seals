package utils;

import java.util.ArrayList;
import java.util.List;

public class Pathfinder {

    private ArrayList<ArrayList<AStarNode>> graph;



    public String getNextDirection(String map, ArrayList<Integer> start, ArrayList<Integer> goal){
        AStarSearch search = new AStarSearch();
        AStarNode start_node = this.graph.get(start.get(0)).get(start.get(1));
        AStarNode goal_node = this.graph.get(goal.get(0)).get(goal.get(1));
        List path = search.findPath(start_node, goal_node);
        return convertNodeToDirection(start, path);
    }

    private String convertNodeToDirection(ArrayList<Integer> start, List<AStarNode> path){
        if (path == null || path.size() == 0){
            return null;
        }

        if (start.get(1) == path.get(0).getX() + 1){
            return "W";
        }

        if (start.get(1) == path.get(0).getX() - 1){
            return "E";
        }

        if (start.get(0) == path.get(0).getY() + 1){
            return "N";
        }

        if (start.get(0) == path.get(0).getY() - 1){
            return "S";
        }
        return null;
    }


    public void createGraph(String map, ArrayList<Character> other_players){
        graph = new ArrayList<>();
        graph.add(new ArrayList<>());
        int y = 0;
        int x = 0;
        for (int i = 0; i < map.length(); i++){
            char c = map.charAt(i);
            for (int j = 0; j < other_players.size(); j++){
                ArrayList<Integer> player_location = other_players.get(j).getLocation();
                ArrayList<Integer> base_location = other_players.get(j).getBase();
                if (player_location.get(0) == y && player_location.get(1) == x){
                    c = 'C';
                }
                else if (base_location.get(0) == y && base_location.get(1) == x){
                    c = 'B';
                }
            }


            AStarNode node = new AStarNode(x, y, c);

            if (c == '\n'){
                graph.add(new ArrayList<>());
                y += 1;
                x = 0;
            }

            else{
                graph.get(y).add(node);
                x += 1;
            }
        }
        graph.remove(graph.size() - 1);
        graph = addNeighbors(graph);
    }

    private ArrayList<ArrayList<AStarNode>> addNeighbors(ArrayList<ArrayList<AStarNode>> graph){
        for (int y = 0; y < graph.size(); y++){
            for (int x = 0; x < graph.get(y).size(); x++){
                AStarNode node = graph.get(y).get(x);
                if ((y - 1) >= 0){
                    AStarNode top_neighbor = graph.get(y-1).get(x);
                    if (top_neighbor.getSymbol() == '0' || top_neighbor.getSymbol() == 'S'){
                        node.add_neighbor(top_neighbor);
                    }
                }
                if ((y + 1) < graph.size()){
                    AStarNode bottom_neighbor = graph.get(y+1).get(x);
                    if (bottom_neighbor.getSymbol() == '0' || bottom_neighbor.getSymbol() == 'S'){
                        node.add_neighbor(bottom_neighbor);
                    }
                }
                if ((x - 1) >= 0){
                    AStarNode left_neighbor = graph.get(y).get(x-1);
                    if (left_neighbor.getSymbol() == '0' || left_neighbor.getSymbol() == 'S'){
                        node.add_neighbor(left_neighbor);
                    }
                }
                if ((x + 1) < graph.size()){
                    AStarNode right_neighbor = graph.get(y).get(x+1);
                    if (right_neighbor.getSymbol() == '0' || right_neighbor.getSymbol() == 'S'){
                        node.add_neighbor(right_neighbor);
                    }
                }
            }
        }


        return graph;
    }
}
