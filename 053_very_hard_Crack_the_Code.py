"""
Crack the Code
This is a reverse-coding challenge. Create a function that outputs the correct list from the input. Use the following examples to crack the code.

Examples
decode("hello") ➞ [5, 2, 9, 9, 3]

decode("wonderful") ➞ [11, 3, 2, 1, 2, 6, 3, 9, 9]

decode("something challenging") ➞ [7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]
"""
def decode(txt):
	
	lst = []
	for letter in txt:
		num_ord = ord(letter)
		sum = 0
		for num in str(num_ord):
			sum += int(num)
		lst.append(sum)	
	return lst


# テスト
print(decode("hello"))       # [5, 2, 9, 9, 3]
print(decode("wonderful"))  # [11, 3, 2, 1, 2, 6, 3, 9, 9]
print(decode("all my friends"))  # [16, 9, 9, 5, 10, 4, 5, 3, 6, 6, 2, 2, 1, 7]
print(decode("River"))       # [10, 6, 10, 2, 6]

