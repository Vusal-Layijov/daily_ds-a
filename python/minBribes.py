def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)):
        if q[i]-(i+1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                count += 1
    print(count)
