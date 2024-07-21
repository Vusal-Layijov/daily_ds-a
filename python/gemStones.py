def gemstones(arr):
    # Write your code here
    length = len(arr)
    gemObj = {}
    count = 0
    for mineral in arr:
        for gem in set(mineral):
            if gem in gemObj:
                gemObj[gem] += 1
            else:
                gemObj[gem] = 1
    for realG in list(gemObj.values()):
        if realG == length:
            count += 1
    return count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n-1 in numSet:
                continue
                
            currentSequenceSize = 1

            while (n+currentSequenceSize) in numSet:
                currentSequenceSize += 1

            longest = max(currentSequenceSize, longest)
    
        return longest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = start + (end - start ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])
