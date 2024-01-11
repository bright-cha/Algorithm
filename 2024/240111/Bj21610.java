import java.util.Scanner;

public class Bj21610 {
    static int n;
    static int m;
    static int[][] matrix;
    static int[][] delta = {{}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}};

    static void moveCloud(int dir, int dis) {
        int[][] newMatrix = new int[0][0];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < m; i++) {
            int direction = sc.nextInt();
            int distance = sc.nextInt();

            // 구름 이동
            moveCloud(direction, distance);
            // 구름 칸의 물 1 증가
            // 구름 소멸
            // 물이 증가한 칸 버그 실행
                // 대각선에 물이 있는 바구니 만큼 기준 영역 물 증가
            // 물의 양이 2이상인 칸, -2 및 구름 생성(구름이 사라진 칸 제외)

        }
    }
}
