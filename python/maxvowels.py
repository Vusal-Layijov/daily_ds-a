class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_vowels = 0
        current_vowels = 0

        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        # Slide the window through the string
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_vowels -= 1
            if s[i] in vowels:
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        maxK = 0
        for ind in range(len(s)-k+1):
            sub = s[ind:ind+k]
            count = 0
            for letter in sub:
                if letter in vowels:
                    count += 1
            maxK = max(maxK, count)

        return maxK


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        left = 0
        maxLen = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            maxLen = max(maxLen, right-left+1)
        return maxLen
