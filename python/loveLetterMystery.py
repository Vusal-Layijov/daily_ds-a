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


def superReducedString(s):
    # Write your code here
    stack = []

    for letter in s:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack) if stack else 'Empty String'
    