# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

# s = input()
# s = 'azcbobobegghakl'
counter = 0
for c in s:
    if c in {'a', 'e', 'i', 'o', 'u'}: counter += 1
print('Number of vowels:', counter)
