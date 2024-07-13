/**
 Combine Arrays
 Create a function that takes three lists and returns one list where all passed arrays are combined into nested lists.

 These lists should be combined based on indexes: the first nested list should contain only the items on index 0, the second list on index 1, and so on.

 If any list contains fewer items than necessary, supplement the missing item with "*".

 Examples
 combine_lists([False, "False"], ["True", True, "bool"], ["None", "undefined"]) ➞ [[False, "True", "None"], ["False", True, "undefined"], ["*", "bool", "*"]]

 combine_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]) ➞ [[1, 4, 7], [2, 5,  8], [3, 6, 9]]

 combine_lists(["Jack", "Joe", "Jill"], ["Stuart", "Sammy", "Silvia"], ["Rick", "Raymond", "Riri"]) ➞ [["Jack", "Stuart", "Rick"], ["Joe", "Sammy",  "Raymond"], ["Jill", "Silvia", "Riri"]]
 **/
import java.util.*;

public class very_hard_Combine_Arrays_003 {
    public static List<List<Object>> combineLists(List<?>... lists) {
        // 最大の長さを取得
        int maxLen = 0;
        for (List<?> list : lists) {
            maxLen = Math.max(maxLen, list.size());
        }

        // リストを '*' で埋めて長さを揃える
        List<List<Object>> paddedLists = new ArrayList<>();
        for (List<?> list : lists) {
            List<Object> paddedList = new ArrayList<>(list);
            while (paddedList.size() < maxLen) {
                paddedList.add("*");
            }
            paddedLists.add(paddedList);
        }

        // 転置する
        List<List<Object>> result = new ArrayList<>();
        for (int i = 0; i < maxLen; i++) {
            List<Object> row = new ArrayList<>();
            for (List<Object> list : paddedLists) {
                row.add(list.get(i));
            }
            result.add(row);
        }

        return result;
    }

    public static void main(String[] args) {
    // テスト
        System.out.println(combineLists(
            Arrays.asList(false, "False"),
            Arrays.asList("True", true, "bool"),
                    Arrays.asList("None", "undefined")
                    ));

        System.out.println(combineLists(
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5, 6),
                    Arrays.asList(7, 8, 9)
                    ));

        System.out.println(combineLists(
            Arrays.asList("Jack", "Joe", "Jill"),
            Arrays.asList("Stuart", "Sammy", "Silvia"),
                    Arrays.asList("Rick", "Raymond", "Riri")
        ));
    }
}




