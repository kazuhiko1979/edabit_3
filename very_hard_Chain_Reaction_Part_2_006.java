/**
Chain Reaction (Part #2)
This is a sequel to Chain Reaction (Part #1), with the same setup, but a different flavor.

As in the previous part, you will be given a rectangular array representing a "map" with three types of spaces:

"+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
"x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
Empty spaces "0".
The goal is simple: given a map, return the minimum number of bombs that need to be set off for all bombs to be destroyed by the chain reaction.

Let's look at some examples:

[
  ["+", "+", "+", "0", "+", "+", "+"],
  ["+", "+", "+", "0", "0", "+", "+"]
]
For the map above, the answer is 2; to explode all bombs you just need to set off one "+" bomb in the right cluster and one in the left cluster.

[
  ["x", "0", "x"],
  ["x", "x", "x"]
]
For the map above, the answer is 3; clearly setting off the three bottom "x" bombs is enough, and no less than three bombs suffice.

[
  ["x", "x", "x", "0", "x"],
  ["x", "x", "x", "x", "x"],
  ["x", "x", "x", "0", "x"]
]
For the map above, the answer is 3; setting off the three rightmost bombs in the middle row will do the trick.

Examples
min_bombs_needed([
  ["+", "+", "+", "0", "+", "+", "+"],
  ["+", "+", "+", "0", "0", "+", "+"]
]) ➞ 2

min_bombs_needed([
  ["x", "0", "x"],
  ["x", "x", "x"]
]) ➞ 3

min_bombs_needed([
  ["x", "x", "x", "0", "x"],
  ["x", "x", "x", "x", "x"],
  ["x", "x", "x", "0", "x"]
]) ➞ 3
Notes
Note that both "+" and "x" bombs have an "explosion range" of 1.
To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be part 3!
Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.
**/

import java.util.*;

public class very_hard_Chain_Reaction_Part_2_006 {

    // 深さ優先探索を行うDFSメソッド
    private static void dfs(char[][] grid, boolean[][] visited, int x, int y, char bombType) {
        // スタックを使って深さ探索
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{x, y});

        // "+"爆弾と"x"爆弾の隣接セルの方向を設定
        int[][] directions;
        if (bombType == '+') {
            directions = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, 1}}; // 上下左右
        } else { // bombType == "x"
            directions = new int[][]{{1, 1}, {-1, -1}, {1, -1}, {-1, 1}}; // 対角線
        }

        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int cx = current[0], cy = current[1];
            for (int[] direction : directions) {
                int nx = cx + direction[0], ny = cy + direction[1];
                if (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length &&
                        !visited[nx][ny] && grid[nx][ny] == bombType) {
                    visited[nx][ny] = true;
                    stack.push(new int[]{nx, ny});
                }
            }
        }
    }

    public  static int minBombsNeeded(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];

        // 爆弾の種類を判定する
        char bombType = grid[0][0] == '+' || grid[1][0] == '+' ? '+' : 'x';
        int clusterCount = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == bombType && !visited[i][j]){
                    visited[i][j] = true;
                    dfs(grid, visited, i, j, bombType);
                    clusterCount += 1;
                }
            }
        }

        return clusterCount;
    }


    public static void main(String[] args) {
        char[][] grid1 = {
                {'+', '+', '+', '0', '+', '+', '+'},
                {'+', '+', '+', '0', '0', '+', '+'}
        };
        System.out.println(minBombsNeeded(grid1)); // ➞ 2

        char[][] grid2 = {
                {'x', '0', 'x'},
                {'x', 'x', 'x'}
        };
        System.out.println(minBombsNeeded(grid2)); // ➞ 3

        char[][] grid3 = {
                {'x', 'x', 'x', '0', 'x'},
                {'x', 'x', 'x', 'x', 'x'},
                {'x', 'x', 'x', '0', 'x'}
        };
        System.out.println(minBombsNeeded(grid3)); // ➞ 3

        char[][] grid4 = {
                {'+', '+', '0', '+', '+'},
                {'+', '0', '+', '0', '+'},
                {'0', '+', '+', '+', '0'},
                {'+', '0', '+', '0', '+'},
                {'+', '+', '0', '+', '+'}
        };
        System.out.println(minBombsNeeded(grid4)); // ➞ 1
    }
}