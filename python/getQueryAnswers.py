def getQueryAnswers(cache_entries, queries):
    # Write your code here
    res = []
    ind = 0
    for q in queries:
        while ind < len(cache_entries):
            if cache_entries[ind][0] == q[1]:
                res.append(int(cache_entries[ind][2]))
            ind += 1
        ind = 0

    return res

# getMaximumAmount
def getMaximumAmount(quantity, m):
    # Write your code here
    print(quantity, m)
    maxSales = 0
    while m > 0:
        maxA = max(quantity)
        ind = quantity.index(maxA)
        quantity[ind] = maxA-1
        maxSales += maxA
        m -= 1
    print(maxSales)
    return maxSales

def saveThePrisoner(n, m, s):
    return (m-1 +s)%n or n

#staircase
def staircase(n):
    # Write your code here
    myArr=[' ']*n
    while n>0:
        for ind in range(n-1,len(myArr)):
            myArr[ind]='#'
            
        print(''.join(myArr))
        n-=1