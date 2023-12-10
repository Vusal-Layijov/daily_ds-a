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


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        time,fresh=0,0
        rows,cols=len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.pop(0)
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if(row<0 or row==len(grid) or col<0 or col==len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    fresh-=1
                    q.append([row,col])
            time+=1
        return time if fresh==0 else -1