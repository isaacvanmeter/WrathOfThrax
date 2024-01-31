package game;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class WrathOfThrax {
    public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	System.out.println("enter IP address");
    String serverAddress = in.nextLine(); // Update with your server IP address
    int serverPort = 13001; // Update with your server port

        try {
            Socket socket = new Socket(serverAddress, serverPort);
            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            DataOutputStream outToServer = new DataOutputStream(socket.getOutputStream());

            
            String welcomeMessage = inFromServer.readLine();
            System.out.println("Server: " + welcomeMessage);

            
            String initialMessage = inFromServer.readLine();
            System.out.println("Server: " + initialMessage);



            while (true) {
                String stats = inFromServer.readLine();
                System.out.println("Server: " + stats);
                
                System.out.print("Enter your action (a*/h*): ");
                String userInput = inFromUser.readLine();

                
                outToServer.writeBytes(userInput);

                
                String serverResponse = inFromServer.readLine();
                System.out.println("Server: " + serverResponse);

                
                if (serverResponse.contains("defeated") || serverResponse.contains("remaining")) {
                    break;
                }
            }
            in.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}