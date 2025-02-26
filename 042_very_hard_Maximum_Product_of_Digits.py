"""
Maximum Product of Digits
Write a function that returns all numbers less than or equal to N with the maximum product of digits.

Examples
max_product(8) ➞ [8]

max_product(27) ➞ [27]

max_product(211) ➞ [99, 199]

max_product(9578) ➞ [8999]
Notes
Search for numbers in the range: [0, n].

"""
def max_product(n):

    max_product_numbers = []
    max_product_value = 0

    for i in range(n + 1):
        product = 1
        for digit in str(i):
            product *= int(digit)

        if product > max_product_value:
            max_product_value = product
            max_product_numbers = [i]
        elif product == max_product_value:
            max_product_numbers.append(i)
    
    return max_product_numbers


print(max_product(8)) # [8])
print(max_product(21)) # [9, 19])
print(max_product(26)) # [26])
print(max_product(27)) # [27])
print(max_product(43)) # [39])
print(max_product(90)) # [89])
print(max_product(199)) # [99, 199])
print(max_product(211)) # [99, 199])
print(max_product(455)) # [399])
print(max_product(917)) # [899])
print(max_product(1578)) # [999])
print(max_product(9578)) # [8999])
print(max_product(11111)) # [9999])
print(max_product(41111)) # [39999])
