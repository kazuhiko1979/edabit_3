import java.util.Scanner;

public class tokyo_online {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double base = scan.nextDouble();    // 底辺
        double height = scan.nextDouble();  // 高さ

        double area = base * height / 2.0;

        System.out.println(area);
    }
}