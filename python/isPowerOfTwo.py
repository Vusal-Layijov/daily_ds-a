def is_power_of_two(x):
    return (x & (x - 1)) == 0


def counterGame(n):
    louise_turn = True

    while n > 1:
        if is_power_of_two(n):
            n //= 2
        else:
            largest_power_of_two = 1 << (n.bit_length() - 1)
            n -= largest_power_of_two

        louise_turn = not louise_turn

    return "Louise" if louise_turn else "Richard"
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
