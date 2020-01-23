# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters
# occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# s = input()

slen = len(s)

max_len = 1
max_pos = 0

for i in range(slen):
    j = 1
    while i + j < slen and s[i + j - 1] <= s[i + j]:
        j += 1
    if max_len < j:
        max_len = j
        max_pos = i

longest_str = s[max_pos:max_pos + max_len]
print("Longest substring in alphabetical order is:", longest_str)
