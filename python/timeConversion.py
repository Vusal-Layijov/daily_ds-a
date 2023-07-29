def timeConversion(s):
    # Write your code here
    if 'AM' in s:
        if s[0:2] == '12':
            return '00'+':'+s[3:-2]
        return s[0:-2]
    if 'PM' in s:
        if s[0:2] == '12':
            return s[0:-2]
        return str(12 + int(s[0:2]))+':'+s[3:-2]
