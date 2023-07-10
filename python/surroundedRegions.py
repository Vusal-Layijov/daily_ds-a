def solve(board):
    rows, cols = len(board), len(board[0])


    def dfs(r,c):
        if r<0 or c<0 or r==rows or c==cols or board[r][c] != 'o':
            return 
        board[r][c] ='t'
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
          if board[r][c] =='o' and (r in [0, rows-1] or c in [0,cols-1]):
            dfs(r,c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] =='o':
                board[r][c]='x'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 't':
                board[r][c] = 'o'




