def theLoveLetterMystery(s):
    # Write your code here
    start = 0
    end = len(s)-1
    operations = 0
    while start < end:
        operations += abs(ord(s[start])-ord(s[end]))
        start += 1
        end -= 1
    return operations
