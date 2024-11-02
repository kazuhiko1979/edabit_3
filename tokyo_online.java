public class tokyo_online {
    public static void main(String[] args) {
        final int MEM = 70;
        final int SUB = 3;

        // 2次元配列
        int[][] scores = new int[MEM][SUB];

        // スコア
        for (int i = 0; i < MEM; i++) {
            scores[i][0] = (i * 87 + 71) % 101;
            scores[i][2] = (i * 59 + 55) % 101;
            scores[i][1] = (i * 79 + 23) % 101;
        }

        // 科目ごとの合計
        int[] subTotals = new int[SUB];

        // 合計の計算
        for (int[] student : scores) {
            for (int i = 0; i < SUB; i++) {
                subTotals[i] += student[i];
            }
        }

        // 平均
        for (int i = 0; i < SUB; i++) {
            System.out.printf("科目%d:%.2f%n", i + 1, (double)subTotals[i] / MEM);
        }
    }
}