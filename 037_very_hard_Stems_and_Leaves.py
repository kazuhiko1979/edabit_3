"""
Stems and Leaves
In statistics a stem-and-leaf plot is a graphical representation of values distribution in a dataset, usually implemented for a small set of values. In this exercise we'll build a simple plot for positive integer values following the steps below.

1) You must separate each value in two parts: the stem, equal to all number digits but last and the leaf, equal to the last digit. For numbers in range 0-9 you must add a "0" at the start. Examples:

4872: stem is "487", leaf is "2".
429: stem is "42", leaf is "9".
85: stem is "8", leaf is "5".
1: stem is "0", leaf is "1".
2) Insert in the plot the stems without duplicate values in ascending order, and for every stem every proper leaf in ascending order. Examples for a dataset containing 22, 22, 13, 11, 11:

Stems are 1 and 2 (no duplicates in ascending order).
Leaves for stem 1 are 1, 1 and 3 (every leaf in ascending order)) # leaves for stem 2 are 2 and 2.
Given a list of positive integers you must return the stem-and-leaf plot as a list of strings, one for each stem: strings have to be formatted with stem and leaves separated by " I " (spaces included) and leaves in ascending order separated by a space between them.

Examples
stem_plot([111, 11, 1]) ➞ ["0 | 1", "1 | 1", "11 | 1"]

stem_plot([4, 8, 75]) ➞ ["0 | 4 8", "7 | 5"]

stem_plot([22, 22, 38, 22, 19]) ➞ ["1 | 9", "2 | 2 2 2", "3 | 8"]
Notes
Every given list is valid, containing only positive integers (no exceptions to handle).
Pay attention to leading and trailing zeroes."""

from collections import defaultdict


def stem_plot(lst):
    
    stem = []
    leaf = []
    for i in lst:
        if len(str(i)) == 1:
            stem.append(0)
            leaf.append(str(i))
        else: # 2桁以上の場合は幹を最後の桁以外、葉を最後の桁にする
            stem.append(str(i)[:-1])
            leaf.append(str(i)[-1])
    
    
    grouped_stem_leaf = defaultdict(list)
    
    for s, l in zip(stem, leaf):
        grouped_stem_leaf[str(s)].append(l)
    
    sorted_stem_leaf = dict(sorted(grouped_stem_leaf.items()))
    
    result = []
    
    for stem, leaves in sorted_stem_leaf.items():
        formatted_line  = "{} | {}".format(stem, ' '.join(leaves))
        result.append(formatted_line)
    
    return result
    


print(stem_plot([111, 11, 1])) # ["0 | 1", "1 | 1", "11 | 1"], "Example #1")
print(stem_plot([4, 8, 75])) # ["0 | 4 8", "7 | 5"], "Example #2")
print(stem_plot([22, 22, 38, 22, 19])) # ["1 | 9", "2 | 2 2 2", "3 | 8"], "Example #3")
print(stem_plot([1062, 310, 89, 9, 16])) # ["0 | 9", "1 | 6", "8 | 9", "31 | 0", "106 | 2"])
print(stem_plot([48, 125, 48, 48, 20, 21, 22, 125, 48, 20])) # ["2 | 0 0 1 2", "4 | 8 8 8 8", "12 | 5 5"])
print(stem_plot([36, 12, 2, 4, 1062, 1062, 2, 36, 234])) # ["0 | 2 2 4", "1 | 2", "3 | 6 6", "23 | 4", "106 | 2 2"])
print(stem_plot([555, 555, 555, 555])) # ["55 | 5 5 5 5"])
print(stem_plot([10, 20, 30, 1, 2, 3])) # ["0 | 1 2 3", "1 | 0", "2 | 0", "3 | 0"])