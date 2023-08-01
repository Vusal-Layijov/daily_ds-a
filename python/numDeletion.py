def alternatingCharacters(s):
    # Write your code here
    numDeletion = 0
    for ind in range(len(s)-1):
        if s[ind] == 'A' and s[ind+1] == 'A':
            numDeletion += 1
            continue
        if s[ind] == 'B' and s[ind+1] == 'B':
            numDeletion += 1
            continue
    return numDeletion
