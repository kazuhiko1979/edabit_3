"""
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
"""


def postfix(expression):
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    stack = []

    try:
        for token in expression.split():
            if token in operators:
                # If token is an operator, pop two operands and perform the operation
                b, a = stack.pop(), stack.pop()
                result = operators[token](a, b)
                stack.append(result)
            else:
                # If token is an operand, convert to float and push to stack
                stack.append(float(token))

        # The final result should be the only item left in the stack
        if len(stack) != 1:
            raise ValueError("Invalid expression")

        return stack[0]

    except (IndexError, ValueError, ZeroDivisionError) as e:
        return f"Error: {str(e)}"


# Test cases
print(postfix("8 1 +"))
print(postfix("9 3 /"))
print(postfix("13 6 7 8 4 / 9 * - + +"))
print(postfix("8 2 5 * +"))
print(postfix("10 7 1 1 + - / 6 * 3 5 4 + - +"))


# def postfix(expression):
#     expression = expression.split(" ")
#
#     while len(expression) > 0:
#         if len(expression) == 1:
#             return expression[0]
#         for value in expression:
#             if value in ["/", "*", "+", "-"]:
#                 calc_a = expression[expression.index(value)-2]
#                 calc_b = expression[expression.index(value)-1]
#                 result = str(eval(calc_a + value + calc_b))
#                 expression.insert(expression.index(calc_a), result)
#                 expression.remove(calc_a)
#                 expression.remove(calc_b)
#                 expression.remove(value)
#                 break


# print(postfix("8 1 +"))
# print(postfix("9 3 /"))
# print(postfix("13 6 7 8 4 / 9 * - + +"))
# print(postfix("8 2 5 * +"))
# print(postfix("10 7 1 1 + - / 6 * 3 5 4 + - +"))