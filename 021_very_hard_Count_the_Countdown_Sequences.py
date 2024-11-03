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

def find_countdown(numbers, start, used_indices):

    if start in used_indices:
        return []

    # 1から始まる場合は即座に[1]を返す
    if numbers[start] == 1:
        return [1]

    sequence = []
    current = numbers[start]
    sequence_indices = []

    # 現在の位置から連続する数値探索
    for i in range(start, len(numbers)):

        if i in used_indices:
            return []

        # 期待する数字(current)と一致するか確認
        if numbers[i] == current:
            sequence.append(current)
            sequence_indices.append(i)
            # 1まで到着したらシーケンス完成
            if current == 1:
                used_indices.update(sequence_indices)
                return sequence
            current -= 1
        else:
            return []

    return []

def final_countdown(numbers):

    if not numbers:
        return [0, []]

    result = []
    used_indices = set()

    for i in range(len(numbers)):
        sequence = find_countdown(numbers, i, used_indices)
        if sequence:
            result.append(sequence)

    return [len(result), result]

    # for i, num in enumerate(reversed(lst)):
    #     if num == 1:
    #         count_down.append(num)
    #     elif num > 1 and len(count_down) >= 1:
    #         if (num - count_down[-1]) == 1:
    #             count_down.append(num)
    #         else:
    #             result.append(count_down[::-1])
    #             count_down = []
    #
    # if count_down != []:
    #     result.append(count_down[::-1])
    #     return [len(result), result]
    # else:
    #     return [len(result), result]

print(final_countdown([5,4,3,2,1])) #, [1, [[5, 4, 3, 2, 1]]])
print(final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]))
print(final_countdown([2,5,4,3,2,1,2])) # , [1, [[5, 4, 3, 2, 1]]])
print(final_countdown([4,3,2,5,4,3])) # , [0, []]))
print(final_countdown([4,3,2,5,4,3,1])) # , [1, [[1]]]))
print(final_countdown([3,2,1,5,5,3,2,1,5,5]))  #, [2, [[3, 2, 1], [3, 2, 1]]]))



