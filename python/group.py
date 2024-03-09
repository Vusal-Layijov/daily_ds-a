def groupAnagrmas(strs):
    res={}
    enum
    for s in strs:
        count=[0]*26
        for c in s:
            count[ord(c)-ord('a')]+=1
        if tuple(count) in res:
            res[tuple(count)].append(s)
        else:
            res[tuple(count)]=[s]
    return list(res.values())
print(groupAnagrmas(["eat","tea","tan","ate","nat","bat"]))

def serviceLane(n, cases):
    output = []
    
    for case in cases:
        # output.append(min([width[i] for i in range(case[0], case[1]+1)]))
        output.append(min(width[case[0]:case[1]+1]))
        
    return output