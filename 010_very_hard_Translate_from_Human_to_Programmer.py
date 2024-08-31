"""
Translate from Human to Programmer
Replace the numbers in a string with their binary form.

Examples
replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."

replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."

replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"
Notes
There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
Anything separates two numbers, even spaces ("2 2" --> "10 10").
"""



# def replace_nums(string):
#
#     number = ""
#     result = ""
#
#     for char in string:
#         if char.isdigit():
#             number += char
#         elif number:
#             if not char.isdigit():
#                 number = int(number)
#                 binary = bin(number)[2:]
#                 result += binary
#                 number = ""
#                 result += char
#         elif char == ' ':
#             result += " "
#         else:
#             result += char
#     return result


print(replace_nums("I have 2 sheep.")) #,"I have 10 sheep.")
print(replace_nums("I have 2 sheep, and 21 chickens.")) #,"I have 10 sheep, and 10101 chickens.")
print(replace_nums("100 is my lucky number.")) # ,"1100100 is my lucky number.")
print(replace_nums("My father was born in 1974.10.25."))# ,"My father was born in 11110110110.1010.11001.")
print(replace_nums("This sentence is10 35filled with ran20dom numbers on7 purpo31se."))# ,"This sentence is1010 100011filled with ran10100dom numbers on111 purpo11111se.")
print(replace_nums("10hell76o4 boi")) # ,"1010hell1001100o100 boi")