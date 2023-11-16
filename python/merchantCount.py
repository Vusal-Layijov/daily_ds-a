def sockMerchant(n, ar):
    # Write your code here
    myset = set()
    result = []
    count = 0
    for num in ar:
        if num in myset:
            continue
        togo = ar.count(num)
        result.append(togo)
        myset.add(num)
    for num in result:
        if num // 2 > 0:
            count += num // 2
    return count


def caesarCipher(s, k):
    ans = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                ascii = ord('a') + (ord(c) - ord('a') + k) % 26
            else:
                ascii = ord('A') + (ord(c) - ord('A') + k) % 26
            ans += chr(ascii)
        else:
            ans += c
    return ans
