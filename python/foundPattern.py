def gridSearch(G, P):
    # Dimensions of grid and pattern
    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])
    
    # Iterate over each possible starting point in the grid
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            # Flag to check if pattern is found
            found = True
            # Check if the pattern matches the grid segment
            for pi in range(r):
                if not found:
                    break
                for pj in range(c):
                    if G[i + pi][j + pj] != P[pi][pj]:
                        found = False
                        break
            if found:
                return 'YES'
    return 'NO'
def almostSorted(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    
    index_list = []
    
    for i in range(len(sorted_arr)):
        if sorted_arr[i] != arr[i]:
            index_list.append(i+1)
    
    if len(index_list) == 2:
        print('yes')
        print('swap ' + str(index_list[0]) + ' ' + str(index_list[1]))
        
    else:
        sub_list = arr[index_list[0]-1: index_list[-1]]
        if sorted(sub_list, reverse=True) != arr[index_list[0]-1: index_list[-1]]:
            print('no')
        else:
            print('yes')
            print('reverse ' + str(index_list[0]) + ' ' + str(index_list[-1]))
