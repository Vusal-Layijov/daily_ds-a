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

# ACM TEAM
def acmTeam(topic):
    
    n=len(topic)
    mySet=set()
    
    for num in range(1,n):
        for num2 in range(num+1,n+1):
            mySet.add((num,num2))
    myArr=list(mySet)
    myArr.sort()
    res=[0]*len(myArr)
    i=0
    for pair in myArr:
        sumM=0
        for ind in range(len(topic[pair[0]-1])):
            if topic[pair[0]-1][ind]=="1" or topic[pair[1]-1][ind]=="1":
                sumM+=1
        res[i]=sumM
        i+=1
    res2=[]
    num=max(res)
    res2.append(num)
    res2.append(res.count(num))
    return res2

#array stepper
def array_stepper(numbers):
  return _array_stepper(numbers,0,{})


def _array_stepper(numbers,i,memo):
  if i in memo:
    return memo[i]
  if i>=len(numbers)-1:
    return True
  maxStep=numbers[i]
  for step in range(1,maxStep+1):
    if _array_stepper(numbers,i+step,memo):
      memo[i]=True
      return True
  memo[i]=False
  return memo[i]

#max_palin_subsequence

def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, i, j, memo):
  key = (i, j)
  
  if key in memo:
    return memo[key]
  
  if i == j:
    return 1
  
  if i > j:
    return 0
  
  if string[i] == string[j]:
    memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
    return memo[key]
  else:
    memo[key] = max(
      _max_palin_subsequence(string, i + 1, j, memo),
      _max_palin_subsequence(string, i, j - 1, memo)
    )
    return memo[key]
  
def taumBday(b, w, bc, wc, z):
    # Write your code here
    minCost=min(bc,wc)
    sum1=b*bc + w*wc
    sum2=b*wc+b*z +w*wc
    sum3=w*bc+w*z +b*bc
    
    return min(sum1,sum2,sum3)