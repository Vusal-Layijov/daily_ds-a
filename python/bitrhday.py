def birthday(s, d, m):
    # Write your code here
    result = 0
    for ind in range(len(s)):
        if ind + m <= len(s):
            if sum(s[ind:ind+m]) == d:
                result += 1
    return result
