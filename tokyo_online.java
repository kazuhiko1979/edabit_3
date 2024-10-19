import java.util.Scanner;

public class tokyo_online {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double heightCm  = scan.nextDouble();
        double weightKg  = scan.nextDouble();

        double heightM = heightCm / 100.0;

        // 標準体重
        double standardWeight = heightM * heightM * 22;

        // 標準体重と、入力体重の差
        double weightDifference = weightKg - standardWeight;

        System.out.printf("%.1f\n", standardWeight);

        if (weightDifference < -10){
            System.out.println("Underweight");
        } else if (weightDifference <= 10) {
            System.out.println("Normal");
        } else {
            System.out.println("Overweight");
        }
    }
}
