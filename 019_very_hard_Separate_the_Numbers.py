def separate_numbers(input_str):

    str_length = len(input_str)

    for first_digit_len in range(1, str_length // 2 + 1):
        first_num = int(input_str[:first_digit_len])

        numbers = []
        current_pos = 0
        current_num = first_num
        is_valid = True

        while current_pos < str_length:
            current_str = str(current_num)

            if input_str[current_pos:].startswith(current_str):
                numbers.append(current_str)
                current_pos += len(current_str)
                current_num += 1
            else:
                is_valid = False
                break

        if is_valid:
            return "YES {}".format(numbers[0])

    return "NO"


print(separate_numbers("99910001001"))
print(separate_numbers("1234"))
print(separate_numbers("91011"))
print(separate_numbers("101103"))
print(separate_numbers("010203"))
print(separate_numbers("13"))
print(separate_numbers("1"))
print(separate_numbers("999100010001"))
print(separate_numbers("7891011"))
