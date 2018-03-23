import py4j.GatewayServer;

import java.util.ArrayList;
public class JavaBotEntryPoint {

    private ArrayList<Bot> bots;

    public JavaBotEntryPoint() {
        bots = new ArrayList<>();

        // Add your bots here
        bots.add(new MyBot());
    }

    public ArrayList<Bot> getBots() {
        return bots;
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new JavaBotEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}