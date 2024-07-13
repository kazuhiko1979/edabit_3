"""
Combine Arrays
Create a function that takes three lists and returns one list where all passed arrays are combined into nested lists.

These lists should be combined based on indexes: the first nested list should contain only the items on index 0, the second list on index 1, and so on.

If any list contains fewer items than necessary, supplement the missing item with "*".

Examples
combine_lists([False, "False"], ["True", True, "bool"], ["None", "undefined"]) ➞ [[False, "True", "None"], ["False", True, "undefined"], ["*", "bool", "*"]]

combine_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]) ➞ [[1, 4, 7], [2, 5,  8], [3, 6, 9]]

combine_lists(["Jack", "Joe", "Jill"], ["Stuart", "Sammy", "Silvia"], ["Rick", "Raymond", "Riri"]) ➞ [["Jack", "Stuart", "Rick"], ["Joe", "Sammy",  "Raymond"], ["Jill", "Silvia", "Riri"]]

"""
from itertools import zip_longest

def combine_lists(*lists):

    # 最大の長さを取得
    max_len = max(len(lst) for lst in lists)

    # リストを'*'で埋めて長さを揃える
    padded_lists = [lst + ['*'] * (max_len - len(lst)) for lst in lists]

    # 転置
    return list(map(list, zip(*padded_lists)))

    # lst_all = [lst1, lst2, lst3]
    # max_len = max(len(sublist) for sublist in lst_all)
    # dummy_lst = [["" for _ in range(max_len)] for _ in range(len(lst_all))]

    # for dummy_sub, lst_sub in zip(dummy_lst, lst_all):
    #     sub_n = (len(dummy_sub) - len(lst_sub))
    #     if sub_n > 0:
    #         lst_sub.append("*" * sub_n)
    #
    # transposed = []
    # for i in range(max_len):
    #     new_row = []
    #     for sublist in lst_all:
    #         new_row.append(sublist[i])
    #     transposed.append(new_row)
    # return transposed


print(combine_lists([False, 'False'], ['True', True, 'bool'], ['None', 'undefined'])) # [[False, 'True', 'None'], ['False', True, 'undefined'], ['*', 'bool', '*']])
print(combine_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(combine_lists(['Jack', 'Joe', 'Jill'], ['Stuart', 'Sammy', 'Silvia'], ['Rick', 'Raymond', 'Riri']))  # [['Jack', 'Stuart', 'Rick'], ['Joe', 'Sammy',  'Raymond'], ['Jill', 'Silvia', 'Riri']])
print(combine_lists(['JS', 'TS', 'CS'], ['React', 'Vue', 'Angular'], ['C', 'C++'])) # [['JS', 'React', 'C'], ['TS', 'Vue', 'C++'], ['CS', 'Angular', '*']]))