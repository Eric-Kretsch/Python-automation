#Write a function that uses regular expressions to make sure the password string it is passed is strong.
# #A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
# and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

import re

passworddetectionRegex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])          # two capital letters
    (?=.*[!@#$&*])               # special characters
    (?=.*[0-9].*[0-9])           # two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])    #three lower case letters
    .{10,}                       #at least 10 digits
    $
)''', re.VERBOSE)

def passwordDetection():
    passwordCheck = input("Please enter your password: ")
    mo = passworddetectionRegex.search(passwordCheck)
    if mo:
        return print("Strong password.")
    else:
        return print("Not a strong password.")

passwordDetection()
