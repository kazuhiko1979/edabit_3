"""
Ruth and Aaron
Two consecutive integers a and b are considered a Ruth-Aaron pair if the sum of the prime factors of a is equal to the sum of the prime factors of b.

Two definitions exist:

Summing up distinct prime factors. For example, 24 and 25 constitute a Ruth-Aaron pair by this definition. 8 and 9 do not.
P24 = [2, 3]  # sum = 5

P25 = [5]  # sum = 5, equal to 24

P8 = [2]  # sum = 2

P9 = [3]  # sum = 3
Summing up repeated prime factors. By this definition, 24 and 25 do not constitute a Ruth-Aaron pair. But 8 and 9 do.
P24 = [2, 2, 2, 3]  # sum = 9

P25 = [5, 5]  # sum = 10

P8 = [2, 2, 2]  # sum = 6

P9 = [3, 3]  # sum = 6, equal to 8
If two consecutive numbers have only distinct prime factors and have equal sums of prime factors, they are considered Ruth-Aaron pairs by both definitions.

P77 = [7, 11]  # sum = 18

P78 = [2, 3, 13]  # sum = 18
Create a function that takes a number n and returns:

False if it is not part of a Ruth-Aaron pair.
A 2-element list if it is part of a Ruth-Aaron pair.
The first element should be "Ruth" if n is the smaller number in the pair, or "Aaron" if it is the larger.
The second element should be 1 if n is part of a Ruth-Aaron pair under the first definition (sum of distinct prime factors)) # 2 if it qualifies by the second definition, 3 if it qualifies under both.
Examples
ruth_aaron(5) ➞ ["Ruth", 3]

ruth_aaron(25) ➞ ["Aaron", 1]

ruth_aaron(9) ➞ ["Aaron", 2]

ruth_aaron(11) ➞ False
"""

def ruth_aaron(n):
    
    def get_prime_factors(x):
        """
        自然数 x の素因数を、重複を含めて列挙したリストを返す。
        例: 12 -> [2, 2, 3]
        """
        factors = []
        num = x
        factor = 2
        while factor * factor <= num:
            while num % factor == 0:
                factors.append(factor)
                num //= factor
            factor += 1 if factor == 2 else 2
        if num > 1:
            factors.append(num)
        return factors
        
        
    def sum_of_distinct_prime_factors(x):
        """
        x の「異なる素因数」だけの和を返す。
        例: 24 -> [2, 3] の和 = 5
        """
        return sum(set(get_prime_factors(x)))


    def sum_of_prime_factors_with_multiplicity(x):
        """
        x の素因数(重複含む) の和を返す。
        例: 8 -> [2, 2, 2] の和 = 6
        """
        return sum(get_prime_factors(x))
        
    
    def check_pair(a, b):
        """
        2 つの整数 a, b が Ruth–Aaron の関係かを調べて
        0, 1, 2, 3 のいずれかを返す。

        返り値:
          0: ペアではない
          1: 重複なしだけ一致
          2: 重複ありだけ一致
          3: 両方一致
        """
        sd_a = sum_of_distinct_prime_factors(a)
        sd_b = sum_of_distinct_prime_factors(b)
        sm_a = sum_of_prime_factors_with_multiplicity(a)
        sm_b = sum_of_prime_factors_with_multiplicity(b)
        
        distinct_match = (sd_a == sd_b)
        multiplicity_match = (sm_a == sm_b)
        
        if distinct_match and multiplicity_match:
            return 3
        elif distinct_match:
            return 1
        elif multiplicity_match:
            return 2
        else:
            return 0
    
    # まず (n, n+1) を調べる。ペアなら n は小さい方 → "Ruth"
    pair_type = check_pair(n, n + 1)
    if pair_type != 0:
        return ["Ruth", pair_type]
    
     # 次に (n-1, n) を調べる。ペアなら n は大きい方 → "Aaron"
    pair_type = check_pair(n - 1, n)
    if pair_type != 0:
        return ["Aaron", pair_type]
    
    return False
    
    
print(ruth_aaron(5)) # ['Ruth',3])
print(ruth_aaron(25)) # ['Aaron',1])
print(ruth_aaron(498)) # False)
print(ruth_aaron(125)) # ['Ruth',2])
print(ruth_aaron(715)) # ['Aaron',3])
print(ruth_aaron(1470)) # False)
print(ruth_aaron(21183)) # ['Ruth',1])
print(ruth_aaron(5561)) # ['Aaron',2])
print(ruth_aaron(6225)) # False)
print(ruth_aaron(26642)) # ['Ruth',3])
print(ruth_aaron(18656)) # ['Aaron',1])
print(ruth_aaron(8558)) # False)

