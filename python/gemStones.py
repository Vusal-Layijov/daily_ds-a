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
