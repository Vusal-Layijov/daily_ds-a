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
