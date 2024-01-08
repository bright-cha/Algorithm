import java.io.*;

public class Bj8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int chance = Integer.parseInt(br.readLine());
        for (int i = 0; i < chance; i++) {
            String str = br.readLine();

            int answer = 0;
            int point = 0;
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == 'O') {
                    answer += ++point;
                } else {
                    point = 0;
                }
            }

            bw.write(Integer.toString(answer));
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
