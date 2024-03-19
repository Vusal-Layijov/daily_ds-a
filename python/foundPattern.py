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
