"""
Product of Two Prime Numbers
Write a function that returns True if the given number num is a product of any two prime numbers.

Examples
product_of_primes(2059) ➞ True
# 29*71=2059

product_of_primes(10) ➞ True
# 2*5=10

product_of_primes(25) ➞ True
# 5*5=25

product_of_primes(999) ➞ False
# There are no prime numbers.
Notes
num is always greater than 0.
0 and 1 aren't prime numbers.
"""
import math

def product_of_primes(num):

    if is_prime(num):
        return False

    divisor = find_first_divisor(num)
    if divisor:
        other = num // divisor
        if is_prime(other):
            return True
    return False


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_first_divisor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i
    return None


print(product_of_primes(2059)) #, True)
print(product_of_primes(7)) #, False)
print(product_of_primes(25)) #, True)
print(product_of_primes(39)) #, True)
print(product_of_primes(5767)) #, True)
print(product_of_primes(77)) #, True)
print(product_of_primes(12)) #, False)
print(product_of_primes(8)) #, False)