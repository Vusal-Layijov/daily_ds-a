def getQueryAnswers(cache_entries, queries):
    # Write your code here
    res = []
    ind = 0
    for q in queries:
        while ind < len(cache_entries):
            if cache_entries[ind][0] == q[1]:
                res.append(int(cache_entries[ind][2]))
            ind += 1
        ind = 0

    return res
