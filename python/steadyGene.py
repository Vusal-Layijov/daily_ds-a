def steadyGene(gene):
    def check(size):
        for i in range(n-size+1):
            start , end = i, i + size - 1 
            for j in range(4):
                x = 0 
                if start != 0 :
                    x = dp[j][start-1]
                if dp[j][-1] - (dp[j][end] - x) > val :
                    break 
            else:
                return True 
        return False
                
    n = len(gene)
    dp = [[0 for i in range(n)] for j in range(4)]
    for i in range(n):
        x = 'ACGT'.index(gene[i])
        for j in range(4):
            dp[j][i] = dp[j][i-1]
        dp[x][i] += 1 
    val = n//4
    ans = n 
    low = 0 
    high = n 
    while low <= high :
        mid = (low+high)//2
        if check(mid):
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans 