import java.io.*;
import java.util.StringTokenizer;

public class Bj10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int H = Integer.parseInt(st.nextToken());
            st.nextToken();
            int N = Integer.parseInt(st.nextToken());

            int floor = N % H == 0 ? H : N % H; // 층 수 계산
            int room = (N - 1) / H + 1; // 호수 계산

            // 출력 형식에 맞게 문자열로 변환하여 출력
            bw.write(floor + String.format("%02d", room));
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }
}
