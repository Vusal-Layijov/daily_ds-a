def birthday(s, d, m):
    # Write your code here
    result = 0
    for ind in range(len(s)):
        if ind + m <= len(s):
            if sum(s[ind:ind+m]) == d:
                result += 1
    return result

#pickNumbers

def pickingNumbers(a):
    # Write your code here
    finalSet = 0
    a.sort()
    for i in a:
        previousSet = 0
        for j in a:
            if i == j or (j - i) == 1:
                previousSet += 1
        if previousSet > finalSet:
            finalSet = previousSet
    return finalSet
