/**
 Count 5s and Win
 Arun is obsessed with primes, especially five.
 He considers a number to be luckiest if it has the highest number of five in it.
 If two numbers have the same frequency of five, Arun considers the larger of them to be luckiest,
 and if there is no five in any number,
 the first given number is considered luckiest. Help him choose the luckiest number.

 Examples
 get_luckiest([5, 12, 55, 11]) ➞ 55

 get_luckiest([5, 12, -55,  11]) ➞ -55

 get_luckiest([515, 1255, -55,  1]) ➞ 1255

 get_luckiest([44, 12, 7, 40]) ➞ 44
 Notes
 Return None if given an empty list.
 **/

import java.util.*;

public class very_hard_Count_5s_and_Win_004 {
    public static Integer getLuckiest(List<Integer> listOfNumbers){
        if (listOfNumbers.isEmpty()) {
            return null;
        }

        List<Integer> numbersWithFive = new ArrayList<>();
        for (Integer num: listOfNumbers){
            if (String.valueOf(num).contains("5")){
                numbersWithFive.add(num);
            }
        }
        if (!numbersWithFive.isEmpty()) {
            return Collections.max(numbersWithFive, (a, b) -> {
                int countA = countFives(a);
                int countB = countFives(b);
                if (countA != countB) {
                    return Integer.compare(countA, countB);
                }
                return Integer.compare(a, b);
            });
        }

        return listOfNumbers.get(0);
    }

    private static int countFives(int num) {
        return (int) String.valueOf(Math.abs(num)).chars().filter(ch -> ch == '5').count();
    }


    public static void main(String[] args) {
        List<List<Integer>> testCases = Arrays.asList(
                Arrays.asList(5, 12, 55, 11),
                Arrays.asList(5, 12, -55, 11),
                Arrays.asList(515, 1255, -55, 1),
                Arrays.asList(44, 12, 7, 40),
                Arrays.asList(-1, -43, -67, 3),
                new ArrayList<>()
        );

        for (List<Integer> testCase : testCases) {
            System.out.println(getLuckiest(testCase));
        }
    }
}
