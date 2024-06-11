def coinChange(coins,amount):
    dp=[amount+1]*(amount+1)
    dp[0]=0
    for a in range(1,amount+1):
        for c in coins:
            if a-c>=0:
                dp[a]= min(dp[a], 1+ dp[a-c])
    return dp[amount] if dp[amount] != amount +1 else -1 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True