import math
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


def commonChild(s1, s2):
    n=len(s1)
    s1='0'+s1
    s2='1'+s2
    count=[[0 for i in range(n+1)] for j in range(n+1)]
    print('ccc',count)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i]==s2[j]:
                count[i][j]=count[i-1][j-1]+1
            else:
                count[i][j]=max(count[i-1][j], count[i][j-1])
    return count[n][n]

def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for num in arr:
        total_sum -= num
        if left_sum == total_sum:
            return 'YES'
        left_sum += num
            
    return 'NO'
def counterGame(n):
    dict1 = {0:"Richard", 1:"Louise"}
    turn = 0
    while n > 1:
        if math.log2(n).is_integer():
            n //= 2 
        else:
            power_of_2 = 2 ** (int(math.log2(n)))
            n -= power_of_2
        turn = 1 - turn
    win = dict1[turn]
    return win

def sansaXor(arr):
    ln = len(arr)
    x = 0
    i = 0
    
    if (ln % 2 != 0):
        while (i < ln):
            x ^= arr[i]
            i += 2
        return x
    
    return 0


def get_all_subarrays(arr):
    subarrays = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarrays.append(arr[i:j])
    return subarrays

# Example usage
array = [1, 2, 3]
print(get_all_subarrays(array))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        return l1==l2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_price = float('inf')  # Start with the highest possible price

        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price to the lowest found so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Calculate max profit from the lowest price point
        
        return max_profit