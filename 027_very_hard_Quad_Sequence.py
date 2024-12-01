"""
Quad Sequence
Write a function that receives a list of x integers and returns a list of x integers in the Nth term of a quadratic number sequence (where x is the length of the incoming list). Your function should return the continuation of the quadratic sequence of the length equal to the length of the given list.

Examples
quad_sequence([48, 65, 84]) ➞ [105, 128, 153]

quad_sequence([0, 1, 6, 15, 28]) ➞ [45, 66, 91, 120, 153]

quad_sequence([9, 20, 33, 48]) ➞ [65, 84, 105, 128]
Notes
Both positive and negative numbers are included in the test cases."""

def quad_sequence(lst):
  
  if len(lst) < 3:
    return []

  if not all(isinstance(x, (int, float)) for x in lst):
    return []

  result = []
  target_length = len(lst)

  while len(result) < target_length:

    first_difference = [lst[i+1] - lst[i] for i in range(len(lst) - 1)]
    
    second_difference = [first_difference[j+1] - first_difference[j] for j in range(len(first_difference) - 1)]

    constant_diff = second_difference[0]
    next_first_diff = first_difference[-1] + constant_diff

    next_term = lst[-1] + next_first_diff
    result.append(next_term)
    
    lst.append(next_term) 

  return result



print(quad_sequence([48, 65, 84])) # [105, 128, 153])
print(quad_sequence([9, 20, 33, 48])) # [65, 84, 105, 128])
print(quad_sequence([0, 1, 6, 15, 28])) # [45, 66, 91, 120, 153])
print(quad_sequence([6, 10, 16, 24])) # [34, 46, 60, 76])
print(quad_sequence([3, 12, 27, 48, 75, 108, 147, 192, 243, 300])) # [363, 432, 507, 588, 675, 768, 867, 972, 1083, 1200])
print(quad_sequence([-3, 8, 23, 42, 65])) # [92, 123, 158, 197, 240])
print(quad_sequence([0, 12, 10])) # [-6, -36, -80])