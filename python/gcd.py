class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_len = gcd(len(str1), len(str2))
        common_str = str1[:gcd_len]  # Extract a substring of length gcd_len

        # Check if the common substring divides both str1 and str2
        if str1 == common_str * (len(str1) // gcd_len) and str2 == common_str * (len(str2) // gcd_len):
            return common_str
        else:
            return ""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        togo = ''
        result = []
        i = 0
        while i < (min(len(str1), len(str2))):
            togo = ''
            for j in range(i+1):
                if str1[j] == str2[j]:
                    togo += str1[j]
            if len(togo) > 0:
                if len(str1) % len(togo) == 0 and len(str2) % len(togo) == 0:
                    result.append(togo)
            i += 1
        if not result:
            return ''
        last = max(result)
        return last


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= maxx:
                result.append(True)
            else:
                result.append(False)
        return
    
def cipher(k, s):
    orig=""
    number_of_ones=0
    for i,b in enumerate(s[:len(s)-k+1]):
        if i>=k:
            if orig[i-k]=="1":
                number_of_ones-=1

        if (b=="1" and number_of_ones%2==0) or (b=="0" and number_of_ones%2==1):
            orig+="1"
            number_of_ones+=1
        else:
            orig+="0"

    return orig
def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while (r-l+1) -max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
