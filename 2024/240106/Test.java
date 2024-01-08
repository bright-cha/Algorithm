public class Test {
    public static void main(String[] args) {
        int[][] rectangle = {{1,1,7,4},{3,2,5,5},{4,3,6,9},{2,6,8,8}};
        int characterX = 1;
        int characterY = 3;
        int itemX = 7;
        int itemY = 8;

        int[][] matrix = new int[51][51];

        // 사각형 그리기
        for (int i = 0; i < rectangle.length; i++) {
            int y1 = rectangle[i][0];
            int x1 = rectangle[i][1];
            int y2 = rectangle[i][2];
            int x2 = rectangle[i][3];

            for (int x = x1; x <= x2; x++) {
                matrix[x][y1] =
            }

        }
    }
}
