import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
                int nx = x + diagonal[j][0];
                int ny = y + diagonal[j][1];

                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (matrix[nx][ny] != 0) {
                        cnt++;
                    }
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
                    boolean temp = true;

                    for (int k = 0; k < clearSize; k++) {
                        if (cloud.get(k)[0] == i && cloud.get(k)[1] == j)
                            temp = false;
                    }

                    if (temp) {
                        matrix[i][j] -= 2;
                        cloud.add(new int[] {i, j});
                    }
                }
            }
        }

        // 구름 소멸
        cloud.subList(0, clearSize).clear();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        matrix = new int[n][n];
        cloud.add(new int[] {n - 2, 0});
        cloud.add(new int[] {n - 2, 1});
        cloud.add(new int[] {n - 1, 0});
        cloud.add(new int[] {n - 1, 1});

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < m; i++) {
//            System.out.println(Arrays.deepToString(matrix));
            st = new StringTokenizer(br.readLine());

            // 구름 이동
            moveCloud(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            for (int j = 0; j < cloud.size(); j++) {
//                System.out.println(Arrays.toString(cloud.get(j)));
            }
            // 구름 칸의 물 1 증가
            for (int j = 0; j < cloud.size(); j++) {
                int x = cloud.get(j)[0];
                int y = cloud.get(j)[1];

                matrix[x][y]++;
            }
//            System.out.println(Arrays.deepToString(matrix));

            // 물이 증가한 칸(구름 칸) 버그 실행
            // 대각선에 물이 있는 바구니 만큼 기준 영역 물 증가
            executionBug();
//            System.out.println(Arrays.deepToString(matrix));

            // 물의 양이 2이상인 칸, -2 및 구름 생성(구름이 사라진 칸 제외)
            makeCloud();
//            System.out.println(Arrays.deepToString(matrix));
        }

        br.close();

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer += matrix[i][j];
            }
        }

        System.out.println(answer);
    }
}
