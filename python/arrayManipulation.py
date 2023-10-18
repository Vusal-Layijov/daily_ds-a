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


def highestValuePalindrome(s, n, k):
    s = list(s)
    left, right = 0, n - 1
    num_changes = 0

    while left < right:
        if s[left] != s[right]:
            max_char = max(s[left], s[right])
            if max_char != '9' and num_changes < k - 1:
                s[left] = '9'
                s[right] = '9'
                num_changes += 2
            else:
                s[left] = max_char
                s[right] = max_char
                num_changes += 1
        left += 1
        right -= 1

    if n % 2 == 1 and num_changes < k:
        s[n // 2] = '9'

    if num_changes > k:
        return "-1"

    return ''.join(s)


# Example usage:
s1 = '1231'
k1 = 3
print(highestValuePalindrome(s1, len(s1), k1))  # Output: '9339'

s2 = '12321'
k2 = 1
print(highestValuePalindrome(s2, len(s2), k2))  # Output: '12921'
