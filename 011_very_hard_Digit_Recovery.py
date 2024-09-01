"""
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
"""
d = {"ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}


def digits_recovery(s):
    result = []
    for i in range(len(s)):
        for j,k in d.items():
            if sorted(j) == sorted(s[i:i+len(j)]):
                result.append(k)
    return ''.join(map(str, result)) or "No digits found"


# テスト
print(digits_recovery("NEO"))  # Expected: 1
print(digits_recovery("ONETWO"))  # Expected: 12
print(digits_recovery("ZYX"))  # Expected: No digits found
print(digits_recovery("NEOTWONEINEIGHTOWSVEEN"))  # Expected: 12219827
print(digits_recovery("TWWTONE"))  # Expected: 21
print(digits_recovery("ONENO"))  # Expected: 11