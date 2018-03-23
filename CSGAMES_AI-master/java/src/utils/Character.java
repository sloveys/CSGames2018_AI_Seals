package utils;

import java.util.ArrayList;
import java.util.HashMap;

public class Character {


    private int id;
    private String name;
    private int health;
    private ArrayList<Integer> location;
    private ArrayList<Integer> base;

    private int spawn;
    private int points;
    private int carrying;

    private String status;

    public Character(int id, String name, int health, ArrayList<Integer> location, ArrayList<Integer> base, int spawn, int points, int carrying, String status) {
        this.id = id;
        this.name = name;
        this.health = health;
        this.location = location;
        this.base = base;
        this.spawn = spawn;
        this.points = points;
        this.carrying = carrying;
        this.status = status;
    }

    public static Character parse(HashMap<String, Object> character_state){
        int spawn = (int) character_state.get("spawn");
        String name = (String) character_state.get("name");
        int health = (int) character_state.get("health");
        ArrayList<Integer> location = (ArrayList<Integer>) character_state.get("location");
        int id = (int) character_state.get("id");
        int points = (int) character_state.get("points");
        int carrying = (int) character_state.get("carrying");
        ArrayList<Integer> base = (ArrayList<Integer>) character_state.get("base");
        String status = (String) character_state.get("status");
        return new Character(id, name, health, location, base, spawn, points, carrying, status);
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }

    public ArrayList<Integer> getLocation() {
        return location;
    }

    public ArrayList<Integer> getBase() {
        return base;
    }

    public int getSpawn() {
        return spawn;
    }

    public int getPoints() {
        return points;
    }

    public int getCarrying() {
        return carrying;
    }

    public String getStatus() {
        return status;
    }
}
