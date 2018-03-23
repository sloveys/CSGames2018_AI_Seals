import utils.Character;
import utils.Pathfinder;

import java.util.ArrayList;
import java.util.HashMap;

public class Bot {

    protected int player_id;
    protected Command command;
    protected Pathfinder pathfinder;
    protected Character player;
    protected ArrayList<Character> otherBots;

    public Bot(){
        player_id = -1;
        pathfinder = new Pathfinder();
        command = null;
    }

    public void set_player_id(int id){
        player_id = id;
        command = new Command(player_id);
    }

    public HashMap<String, String> turn(String game_state, HashMap<String, Object> character_state, ArrayList<HashMap<String, Object>> other_bots){
        this.player = Character.parse(character_state);
        this.otherBots = new ArrayList<>();
        for (int i = 0; i < other_bots.size(); i++){
            this.otherBots.add(Character.parse(other_bots.get(i)));
        }
        pathfinder.createGraph(game_state, this.otherBots);
        return command.idle();
    }
}
