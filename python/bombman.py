def bomberMan(n, grid):
    def detonate(current_grid):
        rows, cols = len(current_grid), len(current_grid[0])
        new_grid = [['O'] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if current_grid[i][j] == 'O':
                    new_grid[i][j] = '.'
                    if i > 0:
                        new_grid[i - 1][j] = '.'
                    if i < rows - 1:
                        new_grid[i + 1][j] = '.'
                    if j > 0:
                        new_grid[i][j - 1] = '.'
                    if j < cols - 1:
                        new_grid[i][j + 1] = '.'

        return [''.join(row) for row in new_grid]

    if n == 1:
        return grid

    if n % 4 == 2 or n % 4 == 0:
        return ['O' * len(row) for row in grid]
    elif n % 4 == 3:
        return detonate(detonate(grid))
    elif n % 4 == 1:
        return detonate(grid)

#uniqueParhs
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]


#num of islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visit = set()
        if not grid:
            return 0

        def bfs(r, c):
            q = [(r, c)]
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            while q:
                r, c = q.pop(0)
                for dr, dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == '1' and (r+dr, c+dc) not in visit:
                        visit.add((r+dr, c+dc))
                        q.append((r+dr, c+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        def capture(r,c):
            if r<0 or c<0 or r==rows or c==cols or board[r][c] != 'O':
                return
            board[r][c]="V"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if(board[r][c]=='O' and(r in [0,rows-1] or c in [0,cols-1])):
                    capture(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]="X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="V":
                    board[r][c]='O'
        
#substrings
def substrings(n: str) -> int:
    MOD = 10**9 + 7
    total_sum = 0
    substring_sum = 0

    # Iterate through each digit in the string
    for i in range(len(n)):
        # Calculate the contribution of the current digit to the sum of all substrings
        # Formula derived from pattern observation and mathematical induction
        substring_sum = (substring_sum * 10 + int(n[i]) * (i + 1)) % MOD
        total_sum = (total_sum + substring_sum) % MOD

    return total_sum


#CheckInclusion
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
def howManyGames(p, d, m, s):
    games = 0 
    while s >= p:  
        s -= p  
        games += 1  
        p = max(p - d, m)
    return games
