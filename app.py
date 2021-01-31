import random, string
# The sign that can be in a password

password_signs = ['´', '@', '$', '#', '/', '()', '<', '>']
password_min_length = 5
password_max_length = 32

lowercase_str = string.ascii_lowercase
uppercase_str = string.ascii_uppercase
all_letters = string.ascii_letters

def string_allowed(pass_str_allowed):

    for i in pass_str_allowed:
        if i not in pass_str_allowed:
            print('Its not allowed')
        if i in pass_str_allowed:
            print('Its allowed')

string_allowed(password_signs)