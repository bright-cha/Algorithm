import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Bj2178 {
    static int N, M;
    static boolean[][] visited;
    static Integer[][] matrix;
    static Integer[] node;

    public static int[][] delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    static int bfs() {
        ArrayDeque<Integer[]> q = new ArrayDeque<>();

        q.offer(new Integer[] {0, 0, 1});
        visited[0][0] = true;

        while (!q.isEmpty()) {
            node = q.poll();

            if (node[0] == N - 1 && node[1] == M - 1) {
                return node[2];
            }

            for (int i = 0; i < 4; i++) {
                int nx = node[0] + delta[i][0];
                int ny = node[1] + delta[i][1];

                if ((0 <= nx && nx < N) && (0 <= ny && ny < M) && matrix[nx][ny] != 0) {
                    if (!visited[nx][ny]) {
                        visited[nx][ny] = true;
                        q.offer(new Integer[] {nx, ny, node[2] + 1});
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        matrix = new Integer[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }

        System.out.println(bfs());
    }
}
