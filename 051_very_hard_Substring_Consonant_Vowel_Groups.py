"""
Substring Consonant-Vowel Groups
Write two functions:

One to retrieve all unique substrings that start and end with a vowel.
One to retrieve all unique substrings that start and end with a consonant.
The resulting array should be sorted in lexicographic ascending order (same order as a dictionary).

Examples
get_vowel_substrings("apple")
➞ ["a", "apple", "e"]

get_vowel_substrings("hmm") ➞ []

get_consonant_substrings("aviation")
➞ ["n", "t", "tion", "v", "viat", "viation"]

get_consonant_substrings("motor")
➞ ["m", "mot", "motor", "r", "t", "tor"]
Notes
Remember the output array should have unique values.
The word itself counts as a potential substring.
Exclude the empty string when outputting the array.
"""

def get_substrings(s, is_vowel=True):
    vowels = "aeiou"
    substrings = set()
    
    for i in range(len(s)):
        if (s[i] in vowels) == is_vowel:
            for j in range(i, len(s)):
                if (s[j] in vowels) == is_vowel:
                    substrings.add(s[i:j+1])
                    
    return sorted(substrings)

def get_vowel_substrings(s):
    return get_substrings(s, is_vowel=True)

def get_consonant_substrings(s):
    return get_substrings(s, is_vowel=False)
    
    


print(get_vowel_substrings("apple")) # ["a", "apple", "e"])
print(get_vowel_substrings("carrot")) # ["a", "arro", "o"])
print(get_vowel_substrings("aviation")) # ["a", "ati", "atio", "avi", "avia", "aviati", "aviatio", "i", "ia", "iati", "iatio", "io", "o"])
print(get_vowel_substrings("motor")) # ["o", "oto"])
print(get_vowel_substrings("rhyme")) # ["e"])
print(get_vowel_substrings("hmm")) # [])

print(get_consonant_substrings("apple")) # ["l", "p", "pl", "pp", "ppl"])
print(get_consonant_substrings("carrot")) # ["c", "car", "carr", "carrot", "r", "rot", "rr", "rrot", "t"])
print(get_consonant_substrings("aviation")) # ["n", "t", "tion", "v", "viat", "viation"])
print(get_consonant_substrings("motor")) # ["m", "mot", "motor", "r", "t", "tor"])
print(get_consonant_substrings("rhyme")) # ["h", "hy", "hym", "m", "r", "rh", "rhy", "rhym", "y", "ym"])
print(get_consonant_substrings("hmm")) # ["h", "hm", "hmm", "m", "mm"])