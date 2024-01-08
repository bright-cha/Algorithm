import java.util.Scanner;

public class Bj2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int d = a * b * c;

        int[] cnt = new int[10];
        while (d > 0) {
            int remain = d % 10;
            cnt[remain]++;
            d -= remain;
            d /= 10;
        }

        for (int j : cnt) {
            System.out.println(j);
        }
    }
}
