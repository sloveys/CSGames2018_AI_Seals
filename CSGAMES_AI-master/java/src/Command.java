import java.util.HashMap;

public class Command {

    private int player_id;

    public Command(int id){
        player_id = id;
    }

    public HashMap<String, String> idle(){
        HashMap<String, String> command = new HashMap<>();
        command.put("command", "idle");
        command.put("character_id", String.valueOf(player_id));
        return command;
    }

    public HashMap<String, String> attack(String direction){
        HashMap<String, String> command = new HashMap<>();
        command.put("command", "attack");
        command.put("character_id", String.valueOf(player_id));
        command.put("direction", direction);
        return command;
    }

    public HashMap<String, String> collect(){
        HashMap<String, String> command = new HashMap<>();
        command.put("command", "collect");
        command.put("character_id", String.valueOf(player_id));
        return command;
    }

    public HashMap<String, String> move(String direction){
        HashMap<String, String> command = new HashMap<>();
        command.put("command", "move");
        command.put("character_id", String.valueOf(player_id));
        command.put("direction", direction);
        return command;
    }

    public HashMap<String, String> rest(){
        HashMap<String, String> command = new HashMap<>();
        command.put("command", "rest");
        command.put("character_id", String.valueOf(player_id));
        return command;
    }

    public HashMap<String, String> store(){
        HashMap<String, String> command = new HashMap<>();
        command.put("command", "store");
        command.put("character_id", String.valueOf(player_id));
        return command;
    }

}
