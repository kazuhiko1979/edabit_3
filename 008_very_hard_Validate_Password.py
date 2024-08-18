"""
Validate Password
Write a regular expression that checks to see if a password is valid. For a password to be valid, it must meet the following requirments:

The password must contain at least one uppercase character.
The password must contain at least one lowercase character.
The password must contain at least one number.
The password must contain at least one special character ! ? * #
The password must be at least 8 characters in length.
Examples
"Password*12" ➞ True

"passWORD12!" ➞ True

"Pass" ➞ False
Notes
The lowercase char, uppercase char, special char, and number can appear at any part of the password.
You will only be writing a regular expression; do not write a function.
"""
import re
def is_valid_password(password):

    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!?*#]).{8,}$'
    return re.match(password_pattern, password) is not None

print(is_valid_password("Password*12"))
print(is_valid_password("passWORD12!"))
print(is_valid_password("Pass"))



