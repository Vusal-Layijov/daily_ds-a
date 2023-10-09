def ladderLength(beginWord,endWord,wordList):
    if endWord not in wordList:
        return 0
    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern=word[:j] +'*' + word[j+1]
            nei[pattern].append(word)
    visit = set([beginWord])
    q = [beginWord]
    res =1
    while q:
        for i in range(len(q)):
            word = q.pop(0)
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1]
                for neighbour in nei[pattern]:
                    if neighbour not in visit:
                        visit.add(neighbour)
                        q.append(neighbour)


        res +=1
    return 0
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        res1=[]
        res2=[]
        for num in set1:
            if num not in set2:
                res1.append(num)
        for num in set2:
            if num not in set1:
                res2.append(num)
        return [res1,res2]