def bigSorting(unsorted):

    unsorted.sort(key = lambda x: int(x))

    return unsorted


def number_of_points(nums):
    # Write your code here
    myset = set()
    for pair in nums:
        for num in range(pair[0], pair[1]+1):
            myset.add(num)
    print(myset)
    return len(myset)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        togo = ''
        count = 0
        len1 = len(word1)
        len2 = len(word2)
        while count <= len1 or count <= len2:
            if count < len1:
                togo += word1[count]
            if count < len2:
                togo += word2[count]
            count += 1
        return togo