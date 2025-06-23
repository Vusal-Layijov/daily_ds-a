def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        iW = 0
        ind = 0
        n, m = len(word), len(abbr)

        while ind < m and iW < n:
            if abbr[ind].isalpha():  # Direct letter match
                if word[iW] != abbr[ind]:
                    return False
                iW += 1
                ind += 1
            else:
                # Disallow leading zeros and ensure digit exists
                if abbr[ind] == '0':
                    return False

                num = 0
                while ind < m and abbr[ind].isdigit():
                    num = num * 10 + int(abbr[ind])
                    ind += 1
                
                iW += num
                if iW > n:  # Prevent skipping past the end
                    return False

        # Both pointers must reach the end
        return iW == n and ind == m
