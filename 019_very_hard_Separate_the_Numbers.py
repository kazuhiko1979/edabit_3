def separate_numbers(input_str: str) -> str:

    if input_str[0] == '0':
        return "NO"

    str_length = len(input_str)

    for first_length in range(1, str_length // 2 + 1):
        if is_valid_sequence(input_str, first_length):
            return "YES {}".format(input_str[:first_length])


def is_valid_sequence(input_str: str, first_length: int) -> bool:
    str_length = len(input_str)
    current_pos = 0
    current_num = int(input_str[:first_length])

    while current_pos < str_length:
        current_str = str(current_num)

        if not input_str[current_pos:].startswith(current_str):
            return False

        current_pos += len(current_str)
        current_num += 1

    return current_pos == str_length


print(separate_numbers("99910001001"))
print(separate_numbers("1234"))
print(separate_numbers("91011"))
print(separate_numbers("101103"))
print(separate_numbers("010203"))
print(separate_numbers("13"))
print(separate_numbers("1"))
print(separate_numbers("999100010001"))
print(separate_numbers("7891011"))
