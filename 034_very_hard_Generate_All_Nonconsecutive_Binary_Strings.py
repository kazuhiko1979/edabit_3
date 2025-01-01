"""
Generate All Nonconsecutive Binary Strings
Create a function to generate all nonconsecutive binary strings where nonconsecutive is defined as a string where no consecutive ones are present, and where n governs the length of each binary string.

Examples
generate_nonconsecutive(1) ➞ "0 1"

generate_nonconsecutive(2) ➞ "00 01 10"

generate_nonconsecutive(3) ➞ "000 001 010 100 101"

generate_nonconsecutive(4) ➞ "0000 0001 0010 0100 0101 1000 1001 1010"
"""
import itertools

def generate_nonconsecutive(n):
    
    # ステップ2: 長さnのすべての2進数列を生成する
    # - 0と1のすべての組み合わせを作成する（例: 00, 01, 10, 11など）
    # - itertoolsなどを使うと便利
    consecutives = list(itertools.product(["0","1"], repeat=n))
    temp = [nums for nums in consecutives if not '11' in ''.join(nums)]
    result = ""
    for i in temp:
        result += ''.join(i)
        result += ' '
        
    return result.lstrip()
            
        
print(generate_nonconsecutive(1))
print(generate_nonconsecutive(2))
print(generate_nonconsecutive(3))
print(generate_nonconsecutive(4))
print(generate_nonconsecutive(5))
print(generate_nonconsecutive(6))
print(generate_nonconsecutive(7))
print(generate_nonconsecutive(8))
print(generate_nonconsecutive(9))
print(generate_nonconsecutive(10))
