"""
Split 25 (Part 1)
About a month ago I stumbled upon an interesting problem — something called the 25 split. In the problem, you had to break up 25 into parts that add to it, and, from those parts, try to create the biggest product.

For example, 3 * 22 = 66 or 5 * 5 * 5 * 5 * 5 = 3125. With this first part, return the value of the biggest product possible using natural number parts from a given number, x.

Examples
split(5) ➞ 6
# 3 times 2

split(10) ➞ 36
# 3 * 3 * 4

split(1) ➞ 1
"""
def split(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 4:
        return n

    max_prod = 0
    for i in range(2, n):
        prod = max(i * (n - i), i * split(n - i, memo))
        if prod > max_prod:
            max_prod = prod

    memo[n] = max_prod
    return max_prod

print(split(25)) #, 8748)
print(split(1)) #, 1)
print(split(10)) #, 36)
print(split(5)) #, 6)
print(split(15)) #, 243)
print(split(20)) #, 1458)