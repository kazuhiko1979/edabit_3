"""Make Anagram
Given two strings, that may or may not be of the same length, determine the minimum number of character deletions required to make an anagram. Any characters can be deleted from either of the strings.

Examples
make_anagram("cde", "abc") ➞ 4
# Remove d and e from cde to get c.
# Remove a and b from abc to get c.

# It takes 4 deletions to make both strings anagrams.

make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") ➞ 30

make_anagram("showman", "woman") ➞ 2"""

from collections import Counter

def make_anagram(str1, str2):
    
    # 各文字の出現回数をカウント
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # すべてのユニークな文字を取得
    unique_chars = set(count1.keys()).union(set(count2.keys()))
    
    # 削除する文字数を計算
    deletions = sum(abs(count1[char] - count2[char]) for char in unique_chars)
    return deletions
    
print(make_anagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')) # 30)
print(make_anagram('bugexikjevtubidpulaelsbcqlupwetzyzdvjphn', 'lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk')) # 40)
print(make_anagram('fsqoiaidfaukvngpsugszsnseskicpejjvytviya', 'ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget')) # 42)
print(make_anagram('showman', 'woman')) # 2)
print(make_anagram('imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesfxkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln', 'wfnfdassvfugqjfuruwrdumdmvxpbjcxorettxmpcivurcolxmeagsdundjronoehtyaskpwumqmpgzmtdmbvsykxhblxspgnpgfzydukvizbhlwmaajuytrhxeepvmcltjmroibjsdkbqjnqjwmhsfopjvehhiuctgthrxqjaclqnyjwxxfpdueorkvaspdnywupvmy')) # 102)
print(make_anagram('cde', 'abc')) # 4)
    
