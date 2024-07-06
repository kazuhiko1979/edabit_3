/**
Infection of the Ones
Write a function that replaces every row and column that contains at least one 1 into a row/column that is filled entirely with 1s.

        Solve this without returning a copy of the input list.

Examples
ones_infection([
                       [0, 0, 1],
                       [0, 0, 0],
                       [0, 0, 0]
                       ]) ➞ [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
        ]

ones_infection([
                       [1, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 0]
                       ]) ➞ [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0]
        ]

ones_infection([
                       [0, 1, 0, 1],
                       [0, 0, 0, 0],
                       [0, 1, 0, 0]
                       ]) ➞ [
        [1, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1]
        ]
Notes
You must mutate the original matrix.
Input matrices will have at least row and one column.
Bonus: Solve this without using any higher-order function
 **/
import java.util.*;

public class very_hard_Infection_of_the_Ones_001 {
    public static int[][] onesInfection(int[][] arr) {
        int rows = arr.length;
        int cols = arr[0].length;

        // 1が存在する行と列を記録
        Set<Integer> infectedRows = new HashSet<>();
        Set<Integer> infectedCols = new HashSet<>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (arr[i][j] == 1) {
                    infectedRows.add(i);
                    infectedCols.add(j);
                }
            }
        }
        // 感染した行と列を1で埋める
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (infectedRows.contains(i) || infectedCols.contains(j)) {
                    arr[i][j] = 1;
                }
            }
        }

        return arr;
    }
    // 配列を表示するヘルパーメソッド
    public static void printArray(int[][] arr){
        for (int[] row : arr){
            System.out.println(Arrays.toString(row));
        }
    }
    public static void main(String[] args) {
        // テストケース
        int[][][] testCases = {
                {
                        {0, 0, 1},
                        {0, 0, 0},
                        {0, 0, 0}
                },
                {
                        {1, 0, 1, 0},
                        {0, 1, 0, 0},
                        {0, 0, 0, 0}
                },
                {
                        {0, 1, 0, 1},
                        {0, 0, 0, 0},
                        {0, 1, 0, 0}
                }
        };

        // テスト実行
        for (int[][] testCase : testCases) {
            System.out.println("Input:");
            printArray(testCase);
            int[][] result = onesInfection(testCase);
            System.out.println("Output:");
            printArray(result);
            System.out.println();
        }
    }
}

