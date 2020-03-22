# Problem 3

# Suppose you are given two strings (they may be empty), s1 and s2. You would
# like to "lace" these strings together, by successively alternating elements
# of each string (starting with the first character of s1). If one string is
# longer than the other, then the remaining elements of the longer string
# should simply be added at the end of the new string. For example, if we
# lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.

#Write an iterative procedure, called laceStrings(s1, s2) that does this.


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    resultLst = []
    size1 = len(s1)
    size2 = len(s2)
    size = min(size1, size2)
    for i in range(size):
        resultLst.extend([s1[i], s2[i]])
    if size == size1:
        resultLst.extend(list(s2[size:]))
    else:
        resultLst.extend(list(s1[size:]))

    return ''.join(resultLst)


def main():
    s1 = 'abcd'
    s2 = '123456'
    print(laceStrings(s1, s2))


if __name__ == '__main__':
    main()
