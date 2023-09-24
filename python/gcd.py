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
