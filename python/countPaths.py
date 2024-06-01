from typing import List
import heapq

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Tuple: (time, node, count)
        pq = [(0, 0)]
        times = [float('inf')] * n
        times[0] = 0
        ways = [0] * n
        ways[0] = 1
        
        while pq:
            curr_time, node = heapq.heappop(pq)
            if curr_time > times[node]:
                continue
            for neighbor, time in graph[node]:
                new_time = curr_time + time
                # Found a faster way to reach neighbor
                if new_time < times[neighbor]:
                    times[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_time, neighbor))
                # Found another way with the same minimum time
                elif new_time == times[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1]


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


def powerSum(X, N):
    def power_sum_recursive(total, power, num):
        if total == 0:
            return 1
        if total < 0 or num**power > total:
            return 0
        
        with_num = power_sum_recursive(total - num**power, power, num + 1)
       
        without_num = power_sum_recursive(total, power, num + 1)
        return with_num + without_num

    return power_sum_recursive(X, N, 1)