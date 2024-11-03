"""
Count the Countdown Sequences
A countdown sequence is a descending sequence of k integers from k down to 1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list [x, y] where x is the number that represents how many of countdown sequences are in a given list and y is a list of those sequences in order which they appear in the list.

Examples
final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
# In this example we have 1 countdown sequence: 3, 2, 1

final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
# We have 2 countdown sequences:
# 5, 4, 3, 2, 1 and 3, 2, 1

final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
# We have 3 countdown sequences:
# 4, 3, 2, 1 ; 3, 2, 1 and 1

final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]

final_countdown([]) ➞  [0, []]
Notes
[1] is a valid countdown sequence.
All numbers will be greater than 0.
"""

def final_countdown(lst):

    count_down = []
    result = []

    for i, num in enumerate(reversed(lst)):
        if num == 1:
            count_down.append(num)
        elif num > 1 and len(count_down) >= 1:
            if (num - count_down[-1]) == 1:
                count_down.append(num)
            else:
                result.append(count_down[::-1])
                count_down = []

    if count_down != []:
        result.append(count_down[::-1])
        return [len(result), result]
    else:
        return [len(result), result]

print(final_countdown([5,4,3,2,1])) #, [1, [[5, 4, 3, 2, 1]]])
print(final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]))
print(final_countdown([2,5,4,3,2,1,2])) # , [1, [[5, 4, 3, 2, 1]]])
print(final_countdown([4,3,2,5,4,3])) # , [0, []]))
print(final_countdown([4,3,2,5,4,3,1])) # , [1, [[1]]]))
print(final_countdown([3,2,1,5,5,3,2,1,5,5]))  #, [2, [[3, 2, 1], [3, 2, 1]]]))



