"""
Distance to Nearest Vowel
Write a function that takes in a string and for each character, returns the distance to the nearest vowel in the string. If the character is a vowel itself, return 0.

Examples
distance_to_nearest_vowel("aaaaa") ➞ [0, 0, 0, 0, 0]

distance_to_nearest_vowel("babbb") ➞ [1, 0, 1, 2, 3]

distance_to_nearest_vowel("abcdabcd") ➞ [0, 1, 2, 1, 0, 1, 2, 3]

distance_to_nearest_vowel("shopper") ➞ [2, 1, 0, 1, 1, 0, 1]
Notes
All input strings will contain at least one vowel.
Strings will be lowercased.
Vowels are: a, e, i, o, u.
"""

def distance_to_nearest_vowel(txt):

    vowels = set("aeiou")
    result = []

    for current_index, char in enumerate(txt):
        if char.lower in vowels:
            result.append(0)
        else:
            left_distance = float('inf')
            right_distance = float('inf')

            # move left
            for i in range(current_index, -1, -1):
                if txt[i].lower() in vowels:
                    left_distance = current_index - i
                    break

            # move right
            for i in range(current_index+1, len(txt)):
                if txt[i].lower() in vowels:
                    right_distance = i - current_index
                    break

            result.append(min(left_distance, right_distance))

    return result

print(distance_to_nearest_vowel("aaaaa"))
print(distance_to_nearest_vowel("babbb"))
print(distance_to_nearest_vowel("abcdabcd"))
print(distance_to_nearest_vowel("shopper"))