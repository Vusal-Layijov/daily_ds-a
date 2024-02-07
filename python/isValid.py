def is_valid(s):
    # Create a dictionary to count character frequencies
    char_count = {}

    # Count the frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Create a dictionary to count frequencies of frequencies
    freq_count = {}

    # Count the frequency of frequencies
    for count in char_count.values():
        if count in freq_count:
            freq_count[count] += 1
        else:
            freq_count[count] = 1

    # If there is only one unique frequency, the string is valid
    if len(freq_count) == 1:
        return "YES"

    # If there are two unique frequencies and one of them is 1, the string is valid
    if len(freq_count) == 2:
        freq1, freq2 = freq_count.keys()
        count1, count2 = freq_count.values()
        if (count1 == 1 and (freq1 - freq2 == 1 or freq1 == 1)) or (count2 == 1 and (freq2 - freq1 == 1 or freq2 == 1)):
            return "YES"

    # Otherwise, the string is not valid
    return "NO"


class Solution:
    def climbStairs(self, n: int) -> int:
        z = [1, 1, 2]
        for i in range(n):
            z.append(z[-1]+z[-2])
        return z[n]

# breakingRecords

def breakingRecords(scores):
    # Write your code here
    print(scores)
    maxS=scores[0]
    minS=scores[0]
    maxCount=0
    minCount=0
    for score in scores[1:]:
        if score > maxS:
            maxS=score
            maxCount+=1
        elif score<minS:
            minS=score
            minCount+=1
    return [maxCount,minCount]


def getMoneySpent(keyboards, drives, b):
    res = []
    for key in keyboards:
        for d in drives:
            res.append(key+d)
    res.sort(reverse=True)
    print('resss', res)
    for num in res:
        if num <= b:
            return num
    return -1


def non_adjacent_sum(nums):
  sum1=0
  sum2=0
  for num in nums:
    temp=sum1+num
    sum1=sum2
    sum2=max(temp,sum2)
  return sum2
