def numDecodings(s):
    dp={len(s):1}
    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i]=='0':
            return 0
        res= dfs(i+1)
        if(i+1 < len(s) and (s[i] == '1' or s[i] =='2' and s[i+1] in '0123456')):
            res += dfs(i+2)
        dp[i] =res
        return res
    return dfs(0)
def numDecodings(s):
    dp={len(s):1}
    for i in range(len(s) -1,-1,-1):
        if s[i] =='0':
            dp[i]=0
        else:
            dp[i]=dp[i+1]
        if(i+1<len(s) and (s[i]=='1' or s[i]=='2'and s[i+1] in '0123456')):
            dp[i]+=dp[i+2]
    return dp[0]


#minChange
def min_change(amount,coins):
  res=_min_change(amount,coins,{})
  if res==float('inf'):
    return -1
  else:
    return res


def _min_change(amount, coins,memo):
  if amount in memo:
    return memo[amount]
  if amount==0:
    return 0
  if amount <0:
    return float('inf')
  minChange=float('inf')
  for coin in coins:
    num_coins =1+ _min_change(amount-coin,coins, memo)
    if(num_coins<minChange):
      minChange=num_coins
  memo[amount]=minChange
  return minChange
  

def isPalindrome(s):
  return s == s[::-1]

def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return i if isPalindrome(s[:i] + s[i+1:]) else len(s) - 1 - i
            
    return -1