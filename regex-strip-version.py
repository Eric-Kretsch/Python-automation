#Regex Version of the strip() Method
#Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re

def stripChars(s, chars=None):
        if not chars:
            strip_left = re.compile(r'^\s*')  # string starting with whitespace
            strip_right = re.compile(r'\s*$')  # string ending with whitespace

            s = re.sub(strip_left, "", s)  # replacing strip_left with "" in string s
            s = re.sub(strip_right, "", s)  # replacing strip_right with "" in string s
        else:
            strip_char = re.compile(chars)
            s = re.sub(strip_char, "", s)
        return s

print(stripChars('    test1   ', '1'))
