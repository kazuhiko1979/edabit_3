"""
Counting Nespers
A permutation of a list is a way to reorder its entries. For instance, [1, 2, 3] has permutations:

[1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 1, 2] [3, 2, 1]
This challenge is about nested permutations (nespers, for short) which are the same idea as permutations, but now for nested lists.

For example, the nespers of [1, [2, 3]] are:

[1, [2, 3]] [1, [3, 2]] [[2, 3], 1] [[3, 2], 1]
Note that, as the name indicates, nespers must preserve the nested list structure, so that [2, [1, 3]] is not a nesper of [1, [2, 3]] since 1 and 2 are in different nest levels.

Put another way, a nesper treats each list level as a set (i.e. order is allowed to change)) # but elements can't move between sets.

Write a function that, given a nested list, returns the number of nespers of that list.

To see how to find the number of nespers, let's work out a larger example. Recall that, if a list has n elements, there are n! = n*(n-1)*(n-2)*...*3*2*1 permutations.

As such, I claim that [[1, 7], 3, [2, 4, 5, 6]] has 3! * 2! * 4! nespers. Why? Because there are 3! permutations of the outer level, 2! permutations of the [1, 7] level, and 4! permutations of the [2, 4, 5, 6] level.

Examples
nespers([1, 2, 3]) ➞ 6

nespers([1, [2, 3]]) ➞ 4

nespers([[1, 7], 3, [2, 4, 5, 6]]) ➞ 288

nespers([1, [3, [2, [5, 4]]]]) ➞ 16
# Note that there are 4 nesting levels.
Notes
The elements inside the nested list will always be distinct, to avoid questions about two nespers looking the same.
Some nesting levels may be empty. Recall that 0!=1."""

import math

def nespers(lst):
  
  # def factorial(n):
  #   return math.factorial(n)
  
  # if not isinstance(lst, list):
  #   return 1
  
  total_permutations = math.factorial(len(lst))
  
  for element in lst:
    if type(element) is list:
      total_permutations *= nespers(element)
    
  return total_permutations

print(nespers([1, 2, 3])) # 6)
print(nespers([1, 2, 3, 4, 5])) # 120)
print(nespers([1, [2, 3]])) # 4)
print(nespers([[1, 7],  3,  [2, 4, 5, 6]])) # 288)
print(nespers([1, [3, [2, [5, 4]]]])) # 16)
print(nespers([[], 1, [3, [2, [5, 4]]]])) # 48)
print(nespers([6, [], 1, [3, [2, [5, [], 4]]]])) # 576)
print(nespers([[], [2], [3, 6], [4, 7, 8, 9], [5, [11, 12, [13, 14]]]])) # 138240)
    
  
  
  
  
    
  
  
  