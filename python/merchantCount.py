def sockMerchant(n, ar):
    # Write your code here
    myset = set()
    result = []
    count = 0
    for num in ar:
        if num in myset:
            continue
        togo = ar.count(num)
        result.append(togo)
        myset.add(num)
    for num in result:
        if num // 2 > 0:
            count += num // 2
    return count


def caesarCipher(s, k):
    ans = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                ascii = ord('a') + (ord(c) - ord('a') + k) % 26
            else:
                ascii = ord('A') + (ord(c) - ord('A') + k) % 26
            ans += chr(ascii)
        else:
            ans += c
    return ans

#FIND PRIME DATES
month=[]
def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29
    elif year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28


def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31


def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while (True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1
        if x % 4 == 0 or x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 = y1 + 1
                m1 = m1 + 1
    return result


for i in range(1, 15):
    month.append(31)


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('ravan')
        x = 0
        togo = ''
        count = 1
        while x < len(chars)-1:
            if chars[x] == chars[x+1]:
                count += 1
            elif chars[x] != chars[x+1]:
                togo += chars[x]
                if count == 1:
                    pass
                else:
                    togo += str(count)
                    count = 1
            x += 1

        print('fffff', togo)
        chars.clear()
        for c in togo:
            chars.append(c)

        return len(chars)
    
# Reorder Routes to Make All Paths Lead to the City Zero

class Solution:
    res = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])
        for i in connections:
            adj[i[0]].append([i[1], 1])
            adj[i[1]].append([i[0], 0])

        def dfs(child, parent):
            for [c, s] in adj[child]:
                if c != parent:
                    self.res += s
                    dfs(c, child)
        dfs(0, -1)
        return self.res


#string challange
def StringChallenge(s):
    stack = []
    elements = {'b', 'i', 'em', 'div', 'p'}

    for char in s:
        if char == '<':
            stack.append('')
        elif char == '>':
            if stack:
                current_element = stack.pop()
                if not current_element:
                    continue  

                if current_element.startswith('/'):
                    opening_tag = current_element[1:]
                    if not stack or stack[-1] != opening_tag:
                        return opening_tag
                else:
                    stack.append(current_element)

    return 'true' if not stack else stack[-1][1:] if stack[-1].startswith('/') else stack[-1]

#searchingChallenge


def searching_challenge(str_arr):
    grid = [list(row) for row in str_arr]
    food_positions = []
    charlie_position = None
    home_position = None

    # Find the positions of Charlie, Home, and Food
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'C':
                charlie_position = (i, j)
            elif grid[i][j] == 'H':
                home_position = (i, j)
            elif grid[i][j] == 'F':
                food_positions.append((i, j))

    # Helper function for DFS
    def dfs(position, visited, steps):
        if not food_positions:
            # If all food is collected, calculate steps to home
            steps_to_home = abs(
                position[0] - home_position[0]) + abs(position[1] - home_position[1])
            return steps + steps_to_home

        min_steps = float('inf')  # Initialize min_steps

        for food_pos in food_positions:
            if food_pos not in visited:
                new_visited = visited.copy()
                new_visited.add(food_pos)

                steps_to_food = abs(
                    position[0] - food_pos[0]) + abs(position[1] - food_pos[1])
                result = dfs(food_pos, new_visited, steps + steps_to_food)

                if result != float('inf'):
                    min_steps = min(min_steps, result)

        return min_steps

    result = dfs(charlie_position, set(), 0)

    return -1 if result == float('inf') else result
