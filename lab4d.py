#!/usr/bin/env python3
# Author ID: [Your Seneca ID]

def first_five(s):
    return s[:5]  # Return first five characters

def last_seven(s):
    return s[-7:]  # Return last seven characters

def middle_number(n):
    n_str = str(n)
    return n_str[1:3]  # Return second and third characters

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]  # Combine first three of s1 and last three of s2

if __name__ == '__main__':
    str1 = 'Hello World!!'
    str2 = 'Seneca College'
    num1 = 1500
    num2 = 1.50

    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
