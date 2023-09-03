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
