# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/fc8f42302c644118adfcfa720f9f403e/ca19e125470846f2a36ad1225410e39a/

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.

# s = input()
# s = 'bobbdbbogmtboboobobobobobkobobobobbobobonqbo'

word_to_find = 'bob'

counter = 0
start_search = 0
while True:
    pos = s.find(word_to_find,start_search)
    if pos < 0: break
    counter += 1
    start_search = pos + 1

print("Number of times {0} occurs is: {1}".format(word_to_find, counter))
