import java.util.*;

public class Bj21610 {
    static int n;
    static int m;
    static int[][] matrix;
    static int[][] delta = {{}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}};
    static int[][] diagonal = {{-1, -1}, {1, 1}, {1, -1}, {-1, 1}};
    static ArrayList<int[]> cloud = new ArrayList<>();

    static void moveCloud(int dir, int dis) {
        for (int i = 0; i < cloud.size(); i++) {
            int nx = (cloud.get(i)[0] + delta[dir][0] * dis) % n;
            nx = nx < 0 ? n + nx : nx;
            int ny = (cloud.get(i)[1] + delta[dir][1] * dis) % n;
            ny = ny < 0 ? n + ny : ny;
            cloud.set(i, new int[] {nx, ny});
        }
    }

    static void executionBug() {
        for (int i = 0; i < cloud.size(); i++) {
            int x = cloud.get(i)[0];
            int y = cloud.get(i)[1];

            int cnt = 0;
            for (int j = 0; j < 4; j++) {
                int nx = (x + diagonal[j][0]) % n;
                nx = nx < 0 ? n + nx : nx;
                int ny = (y + diagonal[j][1]) % n;
                ny = ny < 0 ? n + ny : ny;

                if (matrix[nx][ny] != 0) {
                    cnt++;
                }
            }

            matrix[x][y] += cnt;
        }
    }

    static void makeCloud() {
        int clearSize = cloud.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] >= 2) {
                    int[] temp = new int[] {i, j};
                    if (!cloud.contains(temp)) {
                        matrix[i][j] -= 2;
                        cloud.add(temp);
                    }
                }
            }
        }

        // 구름 소멸
        cloud.subList(0, clearSize).clear();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        matrix = new int[n][n];
        cloud.add(new int[] {n - 2, 0});
        cloud.add(new int[] {n - 2, 1});
        cloud.add(new int[] {n - 1, 0});
        cloud.add(new int[] {n - 1, 1});

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < 1; i++) {
            System.out.println(Arrays.deepToString(matrix));
            // 구름 이동
            moveCloud(sc.nextInt(), sc.nextInt());
            for (int j = 0; j < cloud.size(); j++) {
                System.out.println(Arrays.toString(cloud.get(j)));
            }
            // 구름 칸의 물 1 증가
            for (int j = 0; j < cloud.size(); j++) {
                int x = cloud.get(j)[0];
                int y = cloud.get(j)[1];

                matrix[x][y]++;
            }
            System.out.println(Arrays.deepToString(matrix));

            // 물이 증가한 칸(구름 칸) 버그 실행
            // 대각선에 물이 있는 바구니 만큼 기준 영역 물 증가
            executionBug();
            System.out.println(Arrays.deepToString(matrix));

            // 물의 양이 2이상인 칸, -2 및 구름 생성(구름이 사라진 칸 제외)
            makeCloud();
            System.out.println(Arrays.deepToString(matrix));
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer += matrix[i][j];
            }
        }

        System.out.println(answer);
    }
}
