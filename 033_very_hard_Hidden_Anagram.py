"""
Hidden Anagram
Create a function that takes two strings. The first string contains a sentence containing the letters of the second string in a consecutive sequence but in a different order. The hidden anagram must contain all the letters, including duplicates, from the second string in any order and must not contain any other alphabetic characters.

Write a function to find the anagram of the second string embedded somewhere in the first string. You should ignore character case, any spaces, and punctuation marks and return the anagram as a lower case string with no spaces or punctuation marks.

Examples
hidden_anagram("An old west action hero actor", "Clint Eastwood") ➞ "noldwestactio"
# The sequence "n old west actio" is a perfect anagram of "Clint Eastwood".

hidden_anagram("Mr. Mojo Rising could be a song title", "Jim Morrison") ➞ "mrmojorisin"
# The sequence "Mr. Mojo Risin" ignoring the full stop, is a perfect
# anagram of "Jim Morrison".

hidden_anagram("Banana? margaritas", "ANAGRAM") ➞ "anamarg"
# The sequence "ana? marg" ignoring "?" is a perfect anagram of "Anagram".

hidden_anagram("D  e b90it->?$ (c)a r...d,,#~", "bad credit") ➞ "debitcard"
# When all spaces, numbers and puntuation marks are removed
# from the whole phrase, the remaining characters form the sequence
# "Debitcard" which is a perfect anagram of "bad credit".

hidden_anagram("Bright is the moon", "Bongo mirth") ➞ "noutfond"
# The words "Bright moon" are an anagram of "bongo mirth" but they are
# not a continuous alphabetical sequence because the words "is the" are in
# between. Hence the negative result, "noutfond" is returned."""

import string
import re

def hidden_anagram(sentence, target):
  
    text = re.sub(r'[^a-z]', '', sentence.lower())
    phrase = re.sub(r'[^a-z]', '', target.lower())
    
    for i in range(len(text)):
        if sorted(phrase) == sorted(text[i:i + len(phrase)]):
            return text[i:i + len(phrase)]
    return 'noutfond'
    
    # """
    # Finds the hidden anagram of the target string within the sentence.

    # Args:
    #     sentence (str): The sentence to search within.
    #     target (str): The target string to find as an anagram.

    # Returns:
    #     str: The anagram if found, otherwise 'noutfond'.
    # """
  
    # def clean_text(text):
    #     # return ''.join(c for c in text.lower() if c in string.ascii_lowercase)
    #     return ''.join(filter(str.isalpha, text.lower()))

    # # Clean and preprocess inputs
    # clean_sentence = clean_text(sentence)
    # clean_target = clean_text(target)

    # # Prepare the target for comparison
    # sorted_target = ''.join(sorted(clean_target))    
    # target_length = len(clean_target)
    
    # # Sliding window to check substrings
    # for i in range(len(clean_sentence) - target_length + 1):
    #   substring = clean_sentence[i:i + target_length]
    #   if ''.join(sorted(substring)) == sorted_target:
    #     return substring
    # return 'noutfond'


print(hidden_anagram("Sir Patrick Moore was a famous moon starer", "Astronomer")) #  "moonstarer")
print(hidden_anagram("A building, built to stay free of defects, is uncommon!", "Statue of Liberty")) #  "builttostayfree")
print(hidden_anagram('Bright is the moon', 'Bongo mirth')) #  'noutfond')
print(hidden_anagram("Anchor man Bill, a well known TV personality, was confused about becoming president", "Abraham Lincoln")) #  "anchormanbilla")
print(hidden_anagram("There seem to be more and more television ads on the box these days!", "enslave idiots")) #  "televisionads")
print(hidden_anagram("The thing orators hate most is a throat infection", "A sore throat")) #  "oratorshate")
print(hidden_anagram("I thought I heard a high cornet note of great beuaty", "One Cornetto")) #  "cornetnoteo")
print(hidden_anagram('D  e b90it->?$ (c)a r...d,,#~', 'bad credit')) #  'debitcard')
print(hidden_anagram("You won't find any anagram here!", 'aerogramhenna')) #  'noutfond')