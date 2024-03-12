import math
import os
import random
import re
import sys
import collections

MOD = 1000000000


#
# Complete the 'countPaths' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#

def countPaths(n, edges):
  graph = collections.defaultdict(list)

  for i, j in edges:
    graph[i - 1].append(j - 1)
  print(edges,graph)

  start = 0
  end = n - 1

  memo = [0] * n
  cycle_nodes = set()
  path_nodes = set()

  path = []
  seen = [False] * n

  def update_path_nodes(inc):
    for cur in path:
      path_nodes.add(cur)
      memo[cur] += inc
      memo[cur] %= MOD

  def update_cycle_nodes(cycle_start):
    k = len(path) - 1
    while path[k] != cycle_start:
      cycle_nodes.add(path[k])
      k -= 1
    cycle_nodes.add(cycle_start)

  def dfs(node):
    path.append(node)
    seen[node] = True

    if node == n - 1:
      update_path_nodes(1)
    else:
      for next in graph[node]:
        if seen[next]:
          update_cycle_nodes(next)
        else:
          if memo[next] > 0:
            update_path_nodes(memo[next])
          if memo[next] == 0:
            dfs(next)

    if memo[node] == 0:
      memo[node] = -1

    seen[node] = False
    path.pop()

  dfs(start)
  if len(cycle_nodes.intersection(path_nodes)) > 1:
    print('INFINITE PATHS')
  else:
    print(memo[start])



#ladyBug
def happyLadybugs(b):
    # Check if all ladybugs are already happy
    for i in range(len(b)):
        if b[i] != '_' and (i == 0 or b[i] != b[i-1]) and (i == len(b)-1 or b[i] != b[i+1]):
            break
    else:
        # If the loop did not break, all ladybugs are already happy
        return "YES"
    
    # Check if there is at least one empty cell to allow movement
    if '_' not in b:
        return "NO"
    
    # Count the occurrences of each ladybug
    ladybug_counts = {}
    for bug in b:
        if bug != '_':
            if bug in ladybug_counts:
                ladybug_counts[bug] += 1
            else:
                ladybug_counts[bug] = 1
    
    # If any ladybug does not have a pair, return "NO"
    for count in ladybug_counts.values():
        if count == 1:
            return "NO"
    
    # Otherwise, return "YES" since all ladybugs can be made happy
    return "YES"
