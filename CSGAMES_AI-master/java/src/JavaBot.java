import utils.Character;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;


// Example bot
// Check this file to understand how to make a basic bot.

public class JavaBot extends Bot{

    public String get_name(){
        return "Java";
    }

    public HashMap<String, String> turn(String game_state, HashMap<String, Object> character_state, ArrayList<HashMap<String, Object>> other_bots){
        super.turn(game_state, character_state, other_bots);

        ArrayList<Integer> goal = new ArrayList<>(Arrays.asList(1, 1));

        if (player.getLocation().get(0) == 1 && player.getLocation().get(1) == 1){
            System.out.println("To destination");
        }

        String direction = pathfinder.getNextDirection(game_state, player.getLocation(), goal);
        if (direction != null){
            return command.move(direction);
        }
        else{
            return command.idle();
        }
    }
}