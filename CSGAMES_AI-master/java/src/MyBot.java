import utils.Pathfinder;

import java.util.ArrayList;
import java.util.HashMap;

public class MyBot extends Bot{

    public String get_name(){
        // Find a name for your bot
        return "Bot name";
    }

    public HashMap<String, String> turn(String game_state, HashMap<String, Object> character_state, ArrayList<HashMap<String, Object>> other_bots){
        // Your bot logic goes here.
        return command.idle();
    }
}