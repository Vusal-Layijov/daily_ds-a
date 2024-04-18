class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            # If the sum of all numbers is less than the desiredTotal, no one can win
            return False
        
        memo = {}

        def canWin(choices, total):
            if choices[-1] + total >= desiredTotal:
                return True
            if tuple(choices) in memo:
                return memo[tuple(choices)]
            for i in range(len(choices)):
                # If the opponent cannot win, then the current player can win
                if not canWin(choices[:i] + choices[i+1:], total + choices[i]):
                    memo[tuple(choices)] = True
                    return True
            memo[tuple(choices)] = False
            return False

        # Initial call with all choices available and total=0
        choices = list(range(1, maxChoosableInteger + 1))
        return canWin(choices, 0)

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        maxL=[words[0]]
        for i in range(1,len(groups)):
            if groups[i]!=groups[i-1]:
                maxL.append(words[i])
        return maxL
    

def flippingBits(n):
    # Write your code here
    newN=''
    for s in change32(n):
        if int(s):
            newN+='0'
        else:
            newN+='1'
    return int(newN,2)