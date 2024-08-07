"""
Count 5s and Win
Arun is obsessed with primes, especially five. He considers a number to be luckiest if it has the highest number of five in it. If two numbers have the same frequency of five, Arun considers the larger of them to be luckiest, and if there is no five in any number, the first given number is considered luckiest. Help him choose the luckiest number.

Examples
get_luckiest([5, 12, 55, 11]) ➞ 55

get_luckiest([5, 12, -55,  11]) ➞ -55

get_luckiest([515, 1255, -55,  1]) ➞ 1255

get_luckiest([44, 12, 7, 40]) ➞ 44
Notes
Return None if given an empty list.
"""

def get_luckiest(list_of_numbers):
    if not list_of_numbers:
        return None

    def five_count(num):
        return str(num).count('5')

    numbers_with_five = [num for num in list_of_numbers if '5' in str(num)]
    if numbers_with_five:
        return max(numbers_with_five, key=lambda x: (five_count(x), x))
    return list_of_numbers[0]

    # if any('5' in str(num) for num in list_of_numbers):
    #     value_5counts = {num: str(num).count('5') for num in list_of_numbers}
    #     max_value = max(value_5counts.values())
    #     max_value_5counts = {k: v for k, v in value_5counts.items() if v == max_value}
    #     return max(max_value_5counts)
    # return list_of_numbers[0]


print(get_luckiest([5, 12, 55, 11]))
print(get_luckiest([5, 12, -55,  11]))
print(get_luckiest([515, 1255, -55,  1]))
print(get_luckiest([44, 12, 7, 40]))
print(get_luckiest([-1, -43, -67, 3]))