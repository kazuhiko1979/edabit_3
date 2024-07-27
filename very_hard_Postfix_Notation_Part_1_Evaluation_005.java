/**
 Postfix Notation (Part 1: Evaluation)
 Mathematical expressions are usually written with infix notation, where the operator is in-between the two operands. Postfix notation, on the other hand, is where the operator follows the operands. As we use operator precedence to determine the order of calculation (e.g. multiplication/division is evaluated before addition/subtraction), we can change the position of the operands and eliminate the need for parentheses:

 2 + 5   # Infix
 2 5 +   # Postfix

 5 + (1 + 2) * 4 - 3   # Infix
 5 1 2 + 4 * + 3 -     # Postfix
 Postfix expressions are evaluated by reading left-to-right. Any time an operator is reached, a calculation is performed on the previous two operands. The process repeats until there are no more calculations to perform:

 2 3 4 * + 9 -   # evaluate 3x4
 2 12 + 9 -   # evaluate 2+12
 14 9 -   # evaluate 14-9
 5   # final answer
 Given a postfix expression as a string, return the evaluated expression. A single space separates each operator/operand.

 Examples
 postfix("12 3 /") ➞ 4

 postfix("5 3 4 * +") ➞ 17

 postfix("5 3 + 4 *") ➞ 32
 Notes
 Postfix is also known as "Reverse Polish Notation". See the resources tab for more information.
 """
 """
 Postfix Notation (Part 1: Evaluation)

 This function evaluates a postfix expression given as a string.
 Each operator/operand is separated by a single space.
 **/
import java.util.Stack;
import java.util.HashMap;
import java.util.function.BinaryOperator;

public class very_hard_Postfix_Notation_Part_1_Evaluation_005 {

    private static final HashMap<String, BinaryOperator<Double>> operators = new HashMap<>();

    static {
        operators.put("+", (a, b) -> a + b);
        operators.put("-", (a, b) -> a - b);
        operators.put("*", (a, b) -> a * b);
        operators.put("/", (a, b) -> a / b);
    }

    public static double postfix(String expression) {
        Stack<Double> stack = new Stack<>();

        try {
            for (String token : expression.split(" ")) {
                if (operators.containsKey(token)) {
                    // If token is an operator, pop two operands and perform the operation
                    double b = stack.pop();
                    double a = stack.pop();
                    double result = operators.get(token).apply(a, b);
                    stack.push(result);
                } else {
                    // If token is an operand, convert to double and push to stack
                    stack.push(Double.parseDouble(token));
                }
            }

            // The final result should be the only item left in the stack
            if (stack.size() != 1) {
                throw new IllegalArgumentException("Invalid expression");
            }

            return stack.pop();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            return Double.NaN;  // Not a Number to indicate an error
        }
    }

    public static void main(String[] args) {
        System.out.println(postfix("8 1 +"));
        System.out.println(postfix("9 3 /"));
        System.out.println(postfix("13 6 7 8 4 / 9 * - + +"));
        System.out.println(postfix("8 2 5 * +"));
        System.out.println(postfix("10 7 1 1 + - / 6 * 3 5 4 + - +"));
    }
}