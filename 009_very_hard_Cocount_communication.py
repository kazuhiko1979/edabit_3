"""
Coconut Communication
"coconuts" has 8 letters.
A byte in binary has 8 bits.
A byte can represent a character.
We can use the word "coconuts" to communicate with each other in binary if we use upper case letters as 1s and lower case letters as 0s.

Create a function that translates a word in plain text, into Coconut.

Worked Example
The binary for "coconuts" is
01100011 01101111 01100011 01101111 01101110 01110101 01110100 01110011
c         o        c       o       n        u        t       s

Since 0s are lowercase and 1s are uppercase, we can map the binary like this.
cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS

coconut_translator("coconuts") ➞ "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"
Examples
coconut_translator("Hi") ➞ "cOcoNuts cOCoNutS"

coconut_translator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"

coconut_translator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"
Notes
All inputs will be strings.
Make sure to separate the coconuts with spaces.
"""


def coconut_translator(text):
    # 各文字をバイナリ形式に変換
    binary_representation = [format(ord(char), '08b') for char in text]

    # 各バイナリに対応する「coconuts」の文字列を作成し、変換
    coconuts_translations = [
        ''.join(
            letter.upper() if bit == '1' else letter
            for bit, letter in zip(bits, "coconuts")
        )
        for bits in binary_representation
    ]

    # 結果をスペースで結合して返す
    return ' '.join(coconuts_translations)

# def coconut_translator(text):
#
#     eight_bits = [' '.join(format(ord(char), '08b') for char in text)][0].split()
#     count = len(eight_bits)
#     cocounts = ["coconuts" for _ in range(count)]
#
#
#     result = ''
#     for bits, words in zip(eight_bits, cocounts):
#         for bit, word in zip(bits, words):
#             if bit == '1':
#                 upper_w = word.upper()
#                 result += upper_w
#             else:
#                 result += word
#         result += ' '
#     return result



print(coconut_translator('Hi'))
print(coconut_translator("edabit"))
print(coconut_translator("123"))
print(coconut_translator(""))



