# a-Z = [a-zA-Z]
# 0-9 = [0-9]
# . _ time 1
# @ time 1
# . 2,3

import re as regex
email_condition = "^[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-zA-Z0-9]{2,3}$" # ^ = start of the string, $ = end of the string {2, 3} ==> org net ma
email = input("Enter your email: ")

if regex.search(email_condition, email):
    print("Valid Email")
else:
    print("Invalid Email")