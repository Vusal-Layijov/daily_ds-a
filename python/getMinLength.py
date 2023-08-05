def gcd(a,b):
    while b:
        a,b=b, a%b
    return a
def getMinLength(arr):
    gcd_result= arr[0]
    for num in arr:
        gcd_result=gcd(gcd_result, num)
    return gcd_result
#beautiful binary string


def beautifulBinaryString(b):
    # Write your code here
    return b.count('010')
