/**
 Translate from Human to Programmer
 Replace the numbers in a string with their binary form.

 Examples
 replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."

 replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."

 replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"
 Notes
 There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
 Anything separates two numbers, even spaces ("2 2" --> "10 10").
 */
import java.util.function.Function;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class very_hard_Translate_from_Human_to_Programmer_010 {
    public static String replaceNums(String s) {
        Pattern pattern = Pattern.compile("\\d+");

        Function<String, String> toBinary = (match) -> {
            int number = Integer.parseInt(match);
            return Integer.toBinaryString(number);
        };

        StringBuffer result = new StringBuffer();
        Matcher matcher = pattern.matcher(s);

        while (matcher.find()) {
            matcher.appendReplacement(result, toBinary.apply(matcher.group()));
        }
        matcher.appendTail(result);

        return result.toString();
    }

    public static void main(String[] args) {
        String[] testCases = {
            "I have 2 sheep.",
            "I have 2 sheep, and 21 chickens.",
            "100 is my lucky number.",
            "My father was born in 1974.10.25.",
            "This sentence is10 35filled with ran20dom numbers on7 purpo31se.",
            "10hell76o4 boi"
        };
        for (String testCase: testCases) {
            System.out.println("Input:" + testCase);
            System.out.println("Output" + replaceNums(testCase));
            System.out.println();
        }
    }
}

