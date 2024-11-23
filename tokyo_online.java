import java.util.Scanner;

public class tokyo_online {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextLine()) {
            String line = sc.nextLine();

            if (line.isEmpty()) {
                break;
            }

            int charCount = line.replace(" ", "").length();

            System.out.println(charCount);
        }
    }
}



