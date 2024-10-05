"""
Sentence Primeness
A word value can be established summing up all the numeric values of every single character (excluding spaces and punctuation): a value from 1 ("a") to 26 ("z") is given to letters, while numbers have their literal values, from 0 to 9. The sentence value is the sum of the values of the words.

sentence = "ABC ! abc ... @ 123"
# Remove spaces, punctuation and any symbol.

sentence = ["ABC", "abc", "123"]

words values = "ABC" = 1+2+3 = 6 | "abc" = 1+2+3 = 6 | "123" = 1+2+3 = 6

sentence value = 6 + 6 + 6 = 18
Given a string sentence implement a function that returns:

Prime Sentence if the original sentence value is a prime.

Almost Prime Sentence (xxx) if the sentence value is not a prime but, after a single removal of any of the words the new sentence value is a prime (see example #2 for a clearer explanation), with xxx being the word removed. If more than a word can be removed to obtain a prime value, return the first encountered in the original sentence.

Composite Sentence if the sentence value is not a prime and more than one removal is necessary to make the new sentence value (or if none is possible).

Letters values are case insensitive ("aZ" = "Az" = 1 + 26 = 27), while numbers are treated as words ("123" = 1+2+3 = 6).

Examples
sentence_primeness("Help me!") ➞ "Prime Sentence"
# "Help" + "me" = 41 + 18 = 59 (prime)

sentence_primeness("42 is THE aNsWeR...") ➞ "Almost Prime Sentence (aNsWeR)
# "42" + "is" + "THE" + "aNsWeR" = 6 + 28 + 33 + 80 = 147 (not prime)
# Without "42" new value is 141
# Without "is" new value is 119
# Without "THE" new value is 114
# Without "aNsWeR" new value is 67 (prime!)
# If the word "aNsWeR" is removed from sentence the new value is a prime.

sentence_primeness("Did you smoke?") ➞ "Composite Sentence"
# "Did" + "you" + "smoke" = 17 + 61 + 63 = 141 (not prime)
# Without "Did" new value is 124
# Without "you" new value is 80
# Without "smoke" new value is 78
# No single removals make the new sentence value a prime.
Notes
Only letters and digits can be part of the sentence.
If it's an Almost Prime Sentence, the removed word between the brackets must maintain the same capitalization format found in the original sentence (see example #2).
The sentence is Almost Prime if just a single word can be removed to make value a prime, no multiple removals allowed.
Remember the rule for numbers: "10" is a word, so its value is 1+0 and not 10.
"""
import re
import math
from typing import List, Tuple

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

def word_to_value(word: str) -> int:
    """Convert a word to its numeric value."""
    return sum(
        ord(char.lower()) - ord('a') + 1 if char.isalpha() else int(char)
        for char in word if char.isalpha() or char.isdigit()
    )

def process_sentence(sentence: str) -> Tuple[List[str], List[int]]:
    """Process a sentence into words and their corresponding values."""
    words = re.findall(r'\b[a-zA-Z]+\b|\b\d+\b', sentence)
    word_values = [word_to_value(word) for word in words]
    return words, word_values

def sentence_primeness(sentence: str) -> str:
    """Determine the primeness category of a sentence."""
    words, word_values = process_sentence(sentence)
    total_sum = sum(word_values)

    if is_prime(total_sum):
        return "Prime Sentence"

    for word, value in zip(words, word_values):
        if is_prime(total_sum - value):
            return f"Almost Prime Sentence ({word})"

    return "Composite Sentence"

# テストケース
test_sentences = [
    "Help me!",
    "42 is THE aNsWeR...",
    "Did you Smoke?",
    "She SellS SeaShellS by the SeaShore",
    "Lorem. Ipsum. Dolor. Sit. Amet.",
    "three fASt hUNgry aniMALs -aNd- 3 slow faTTy kiDS",
    "This is a 'Prime' Sentence",
    "this is a composite sentence",
    "Primes, PRIMES EVERYWHERE!",
    "10 test cases are enough, this is the last one!"
]

for sentence in test_sentences:
    print(sentence_primeness(sentence))


# import re
# import math
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def sentence_primeness(sentence):
#
#     words = re.findall(r'\b[a-zA-Z]+\b|\b\d+\b', sentence)
#     word_sums = []
#     for word in words:
#         word_sum = 0
#         for char in word:
#             if char.isalpha():
#                 # アルファベットの場合
#                 word_sum += ord(char.lower()) - ord('a') + 1
#             elif char.isdigit():
#                 # 数字の場合
#                 word_sum += int(char)
#         word_sums.append(word_sum)
#
#     if is_prime(sum(word_sums)):
#         return "Prime Sentence"
#     else:
#         for word, sum_value in zip(words, word_sums):
#             if is_prime(sum(word_sums) - sum_value):
#                 return "Almost Prime Sentence ({})".format(word)
#         else:
#             return "Composite Sentence"


# print(sentence_primeness("Help me!")) #, "Prime Sentence", "Example #1")
# print(sentence_primeness("42 is THE aNsWeR...")) #, "Almost Prime Sentence (aNsWeR)", "Example #2")
# print(sentence_primeness("Did you Smoke?")) #, "Composite Sentence", "Example #3")
# print(sentence_primeness("She SellS SeaShellS by the SeaShore")) #, "Prime Sentence")
# print(sentence_primeness("Lorem. Ipsum. Dolor. Sit. Amet.")) #, "Almost Prime Sentence (Lorem)")
# print(sentence_primeness("three fASt hUNgry aniMALs -aNd- 3 slow faTTy kiDS")) # , "Almost Prime Sentence (aniMALs)")
# print(sentence_primeness("This is a 'Prime' Sentence")) #, "Composite Sentence")
# print(sentence_primeness("this is a composite sentence")) #, "Almost Prime Sentence (this)")
# print(sentence_primeness("Primes, PRIMES EVERYWHERE!")) #, "Composite Sentence")
# print(sentence_primeness("10 test cases are enough, this is the last one!")) #, "Prime Sentence")

