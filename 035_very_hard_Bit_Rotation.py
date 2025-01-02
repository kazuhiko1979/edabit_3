"""
Bit Rotation
Python offers some bit operations but not bit rotation. To complete that, create a function that takes three parameters:

n: Integer, which in binary representaion should be rotated.
m: Number of rotation steps that should be performed.
d: Boolean value; True = rotation right, False = rotation left.
Your function should return an integer as a result of its rotated binary representation.

Examples
bit_rotate(8, 1, True) ➞ 4
# 8 in bin: 1000, rotated 1 step to the right: 0100, in dec: 4

bit_rotate(16, 1, False) ➞ 1
# 16 in bin: 10000, rotated 1 step to the left: 00001, in dec: 1

bit_rotate(17, 2, False) ➞ 6
# 17 in bin: 10001, rotated 2 steps to the left: 00110, in dec: 6
Notes
For parameters use unsigned integers only.
There is a solution with string operations and combined bit operations.Bit Rotation
Python offers some bit operations but not bit rotation. To complete that, create a function that takes three parameters:

n: Integer, which in binary representaion should be rotated.
m: Number of rotation steps that should be performed.
d: Boolean value; True = rotation right, False = rotation left.
Your function should return an integer as a result of its rotated binary representation.

Examples
bit_rotate(8, 1, True) ➞ 4
# 8 in bin: 1000, rotated 1 step to the right: 0100, in dec: 4

bit_rotate(16, 1, False) ➞ 1
# 16 in bin: 10000, rotated 1 step to the left: 00001, in dec: 1

bit_rotate(17, 2, False) ➞ 6
# 17 in bin: 10001, rotated 2 steps to the left: 00110, in dec: 6
Notes
For parameters use unsigned integers only.
There is a solution with string operations and combined bit operations.
"""

def bit_rotate(n, m, d):
    
    bit_len = n.bit_length()
    
    if bit_len == 0:
        return 0
    
    m %= bit_len
    
    if d: # 右回転の場合
        # 数字を右にずらす
        right_part = n >> m
        # 右から落ちた部分を左に移動
        left_part = (n & ((1 << m) - 1)) << (bit_len - m)
        # 右と左を足し合わせる
        rotated = right_part | left_part
        
        # 右回転の場合
        # rotated = (n >> m) | ((n & ((1 << m) - 1)) << (bit_len - m))
        return rotated
    else:
        # 左回転の場合
        rotated = ((n << m) & ((1 << bit_len) - 1)) | (n >> (bit_len - m))
        return rotated

    
    
print(bit_rotate(8, 1, True)) #  4)
print(bit_rotate(16, 2, True)) #  4)
print(bit_rotate(283, 7, True)) #  110)
print(bit_rotate(16, 1, False)) #  1)
print(bit_rotate(17, 2, False)) #  6)
print(bit_rotate(122, 7, False)) #  122)
print(bit_rotate(125, 10, True)) #  95)
print(bit_rotate(1022, 8, False)) #  767)
print(bit_rotate(33, 6, True)) #  33)