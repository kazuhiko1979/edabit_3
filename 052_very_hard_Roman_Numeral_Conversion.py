"""Roman Numeral Conversion
Create a function that will take either a string containing a roman numeral, or an integer.

Given a string, return the integer value of that roman numeral.
Given an integer, return the equivalent roman numeral.
Symbols to Values
I ➞ 1

V ➞ 5

X ➞ 10

L ➞ 50

C ➞ 100

D ➞ 500

M ➞ 1000
Examples
roman_numerals("V") ➞ 5

roman_numerals("IV") ➞ 4

roman_numerals("CII") ➞ 102

roman_numerals(45) ➞ "XLV"

roman_numerals(1666) ➞ "MDCLXVI"
Notes
Numerical and Roman Numeral inputs will be positive numbers between 1 and 9999.
"""

def roman_numerals(s):
    
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    if type(s) is str:
        for char in reversed(s):
            current_value = roman_dict[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        
        return total
    elif type(s) is int:
        value_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
        
        roman_str = ""
        for value, symbol in value_map:
            while s >= value:
                roman_str += symbol
                s -= value
        
        return roman_str

print(roman_numerals('I')) # 1)
print(roman_numerals('V')) # 5)
print(roman_numerals('X')) # 10)
print(roman_numerals('L')) # 50)
print(roman_numerals('C')) # 100)
print(roman_numerals('D')) # 500)
print(roman_numerals('M')) # 1000)
print(roman_numerals('IV')) # 4)
print(roman_numerals('VI')) # 6)
print(roman_numerals('XIV')) # 14)
print(roman_numerals('LIX')) # 59)
print(roman_numerals('XCIX')) # 99)
print(roman_numerals('CII')) # 102)
print(roman_numerals('XLV')) # 45)
print(roman_numerals('XXX')) # 30)
print(roman_numerals('XXXVI')) # 36)
print(roman_numerals('DCCXIV')) # 714)
print(roman_numerals('MMXVIII')) # 2018)
print(roman_numerals('MDCLXVI')) # 1666)
print(roman_numerals('MCCCXXIV')) # 1324)
print(roman_numerals(1324)) # 'MCCCXXIV')