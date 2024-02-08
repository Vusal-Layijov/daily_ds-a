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