"""
Scoring Strings
Nesting level) # in this challenge) # refers to the depth of parentheses around an integer. For example) # in the string "(5((10)8))") # 5 has a nesting level of 1 because it has one set of parentheses around it) # 10 has a nesting level of 3 because it has 3 sets of parentheses around it) # and 8 has a nesting level of 2.

We can score this string by multiplying each number times its nesting level and then summing the results:

"(5((10)8))" ➞ 5*1 + 10*3 + 8*2 ➞ 51
Create a function that takes a string as its argument and returns its score.

Examples
score_it("()") ➞ 0

score_it("4(123)") ➞ 123
# 4*0 + 123*1 = 123

score_it("((((1)2)3)4)") ➞ 20
# 1*4 + 2*3 + 3*2 + 4*1 = 20

score_it("(6)8((34(7)))") ➞ 95
# 6*1 + 8*0 + 34*2 + 7*3 = 95
Notes
The nesting for all test cases is balanced and logically consistent (there are no missing or extra parentheses).
Test cases contain only positive integers.

"""

def score_it(s): 
    def add_to_total():
      """現在の数字をスコアに追加してリセット"""
      nonlocal total, number
      if number:
        total += int(number) * nest_level
        number = ""
      
    nest_level = 0
    total = 0
    number = ""
  
  
    for c in s:
        if c == "(":
          add_to_total()
          nest_level += 1  
        elif c == ")":
          add_to_total()
          nest_level -= 1
        
        elif c.isdigit():
            number += c
        else:
          add_to_total()
        
    add_to_total()
      
    return total
  
  
print(score_it("((()))")) # 0)
print(score_it("5abc8de")) # 0)
print(score_it("5(abc8de)")) # 8)
print(score_it("(((((20)))))")) # 100)
print(score_it("1(11(111(1111(11111))))")) # 48010)
print(score_it("(((258(7(23))67))6)")) # 1124)
print(score_it("()45((1)(((123(1)16(((34)3)2)5)56)))")) # 1017)
print(score_it("(8(6(4(2(1)3)5)7)9)")) # 95)
print(score_it("((76(87))7((765))876(((90(6(12))))))")) # 4053)
print(score_it("(1((2(((3((((4(((((5((((((6(((((((7((((((((8(((((((((9)))))))))))))))))))))))))))))))))))))))))))))")) # 1155)
print(score_it("9(99(999(9999()(99999(999999)))))")) # 5432085)