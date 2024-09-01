/**
 Digits Recovery
 Mubashir shuffled a given string of letters by mistake. Some letters in the input string are representing a digit (from zero to nine). Help him to recover all the digits.

 Only consecutive letters can be used. "OTNE" cannot be recovered to 1.
 Every letter has to start with an increasing index. "ONENO" results to 11, because E can be used two times.
 You can ignore all letters in the string if they don't end-up in a digit.
 If no digits can be found, return "No digits found"
 Take care about the order! "ENOWT" will be recovered to 12 and not to 21.
 The input string consists only UpperCase letters.
 Examples
 digits_recovery("NEO") ➞ "1"

 digits_recovery("ONETWO") ➞ "12"

 digits_recovery("ZYX") ➞ "No digits found"

 digits_recovery("NEOTWONEINEIGHTOWSVEEN") ➞ "12219827"
 */

import java.util.*;

public class very_hard_Digit_Recovery_011 {
    private static final Map<String, Integer> d = new HashMap<String, Integer>() {{
        put("ZERO", 0); put("ONE", 1); put("TWO", 2); put("THREE", 3); put("FOUR", 4);
        put("FIVE", 5); put("SIX", 6); put("SEVEN", 7); put("EIGHT", 8); put("NINE", 9);
    }};

    public static String digitsRecovery(String s) {
        List<Integer> r = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            for (Map.Entry<String, Integer> entry : d.entrySet()) {
                String j = entry.getKey();
                Integer k = entry.getValue();
                if (i + j.length() <= s.length() &&
                        sortString(j).equals(sortString(s.substring(i, i + j.length())))) {
                    r.add(k);
                }
            }
        }
        if (r.isEmpty()) {
            return "No digits found";
        } else {
            StringBuilder sb = new StringBuilder();
            for (Integer num : r) {
                sb.append(num);
            }
            return sb.toString();
        }
    }

    private static String sortString(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }

    public static void main(String[] args) {
        System.out.println(digitsRecovery("NEO"));  // Expected: 1
        System.out.println(digitsRecovery("ONETWO"));  // Expected: 12
        System.out.println(digitsRecovery("ZYX"));  // Expected: No digits found
        System.out.println(digitsRecovery("NEOTWONEINEIGHTOWSVEEN"));  // Expected: 12219827
        System.out.println(digitsRecovery("TWWTONE"));  // Expected: 21
        System.out.println(digitsRecovery("ONENO"));  // Expected: 111
    }
}

