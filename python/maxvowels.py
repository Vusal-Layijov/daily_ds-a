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
