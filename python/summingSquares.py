import math
def summing_squares(n):
  return _summing_squares(n,{})

def _summing_squares(n,memo):
  if n in memo:
    return memo[n]
  if n==0:
    return 0
  minS=float("inf")
  for i in range(1, math.floor(math.sqrt(n))+1):
    square=i*i
    numS=1+_summing_squares(n-square,memo)
    minS=min(minS,numS)
  memo[n]=minS
  return minS



def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
  
  coin = coins[i]
  
  total_count = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_count += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = total_count
  return total_count