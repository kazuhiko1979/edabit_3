"""
KixCodes in the Netherlands
In The Netherlands we have PostNL, the postal company. They use KixCodes, a fast way to deliver letters and packages that can be scanned during the process.

Kix Code

The code is a combination of: "Postal code", "House/box/call number" and "House appendage / suffix"

If there is a character between the house number and the suffix, we need to replace that with an X. Eventually, the code will be printed in the KixCode font.

Examples
kix_code("PostNL, Postbus 30250, 2500 GG 's Gravenhage") ➞ "2500GG30250"

kix_code("Liesanne B Wilkens, Kogge 11-1, 1657 KA Abbekerk") ➞ "1657KA11X1"

kix_code("Dijk, Antwoordnummer 80430, 2130 VA Hoofddorp") ➞ "2130VA80430"
Notes
Your function will get an address line (string) separated by comma's.
The input format will always be the same.
Watch out for the different suffixes!
"""

import re
# 先頭が空白1文字、その後に数字、アルファベット大文字2文字のパターン
pattern_1 = r'^ \d+\s+[A-Z]{2}'
pattern_2 = r'\d[\d\s\w\W]*\d*'

def kix_code(addr):

    result = []

    addr = [word for word in addr.split(',')]

    for word in addr[::-1]:
        match_1 = re.search(pattern_1, word)
        match_2 = re.search(pattern_2, word)
        if match_1:
            result.append(match_1.group())
        if match_2:
            result.append(match_2.group())

    result.pop(1)

    def replace_special_characters(input_string):
        input_string = input_string.lstrip()
        step1 = re.sub(r'[^\w]', 'X', input_string)
        result = step1.upper()
        return result

    w = replace_special_characters(result[-1])
    result[-1] = w

    combined_string = ''.join(result)
    result = combined_string.replace(' ', '')
    return result



print(kix_code("PostNL, Postbus 30250, 2500 GG 's Gravenhage")) # ➞ "2500GG30250"
print(kix_code("Liesanne B Wilkens, Kogge 11-1, 1657 KA Abbekerk")) # ➞ "1657KA11X1"
print(kix_code("Dijk, Antwoordnummer 80430, 2130 VA Hoofddorp"))  #➞ "2130VA80430"
print(kix_code("De Jong, Havendijk 13 hs, 1231 FZ POSTDAM"))