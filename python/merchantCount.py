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

#FIND PRIME DATES
month=[]
def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29
    elif year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28


def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31


def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while (True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1
        if x % 4 == 0 or x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 = y1 + 1
                m1 = m1 + 1
    return result


for i in range(1, 15):
    month.append(31)
