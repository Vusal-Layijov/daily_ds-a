def maxSubarray(arr):
    # Write your code here
    maxx=arr[-1]
    for ind in range(-2,-len(arr)-1,-1):
        if maxx <0 and arr[ind]<0:
            maxx=max(arr[ind],maxx)
        else:
            maxx+=arr[ind]
            maxx=max(arr[ind],maxx)
        
        
    
    
    
    print(arr)
    subSeq=[]
    for num in arr:
        if num>0:
            subSeq.append(num)
    summ=sum(subSeq)
    if summ==0:
        summ=max(arr)
    return maxx,summ


def legoBlocks(n, m):
    MOD = 1000000007

    # Create a DP array to store the number of ways to build a wall of height i
    dp = [0] * (n + 1)

    # Initialize the base case
    dp[0] = 1

    # Define the block sizes
    block_sizes = [1, 2, 3, 4]

    # Calculate the number of ways to build the wall for each height
    for height in range(1, n + 1):
        for block_size in block_sizes:
            if height >= block_size:
                dp[height] = (dp[height] + dp[height - block_size]) % MOD

    # Calculate the total number of valid wall formations for width m
    total_ways = 0
    for height in range(1, n + 1):
        total_ways = (total_ways + dp[height]) % MOD

    return total_ways


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are also empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Plant a flower
                    count += 1
            i += 1

        return count >= n
