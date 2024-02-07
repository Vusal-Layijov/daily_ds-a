def count_paths(grid):
  return _count_paths(grid,0,0,{})
  

  
def _count_paths(grid,r,c,memo):
  pos=(r,c)
  if pos in memo:
    return memo[pos]
  if r==len(grid) or c==len(grid[0]) or grid[r][c] == 'X':
    return 0
  if r==len(grid)-1 and c==len(grid[0])-1:
    return 1
  dc= _count_paths(grid,r+1,c,memo)
  rc=_count_paths(grid,r,c+1,memo)
  memo[pos]=dc+rc
  return memo[pos]


def max_path_sum(grid):
  return _max_pah_sum(grid,0,0,{})

def _max_pah_sum(grid,r,c,memo):
  if (r,c) in memo:
    return memo[(r,c)]
  if r==len(grid) or c==len(grid[0]):
    return float("-inf")
  if r==len(grid)-1 and c==len(grid[0])-1:
    return grid[r][c]
  dc = _max_pah_sum(grid,r+1,c,memo)
  dr= _max_pah_sum(grid,r,c+1,memo)
  memo[(r,c)]=grid[r][c] + max(dc,dr)
  return   memo[(r,c)]