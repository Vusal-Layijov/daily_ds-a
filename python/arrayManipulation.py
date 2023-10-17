def arrayManipulation(n, queries):
    myArr = [0] * (n + 1)  # Create an array of zeros with n+1 elements
    for q in queries:
        a, b, k = q
        myArr[a - 1] += k  # Add k to the starting index of the range
        myArr[b] -= k     # Subtract k from the next index after the range
        print(myArr)

    max_value = 0
    current_value = 0

    for val in myArr:
        current_value += val
        if current_value > max_value:
            max_value = current_value

    return max_value
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i==len(s)