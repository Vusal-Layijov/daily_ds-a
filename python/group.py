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

#stones
def stones(n, a, b):
    if a == b:
        return [(n-1)*a]
        
    smaller = min(a, b)
    larger = max(a, b)
    
    return [i*larger + (n-1-i)*smaller for i in range(n)]


#maxEvents:
def maxEvents(arrival, duration):
    # Combine arrival times and durations, then sort by finish time
    events = sorted([(arrival[i], arrival[i] + duration[i]) for i in range(len(arrival))], key=lambda x: x[1])
    
    # Initialize the count of events and the end time of the last selected event
    count = 0
    last_end_time = 0
    
    # Iterate through the events
    for start, end in events:
        # If the start time of the current event is not less than the end time of the last selected event
        if start >= last_end_time:
            # Select this event
            count += 1
            last_end_time = end
            
    return count