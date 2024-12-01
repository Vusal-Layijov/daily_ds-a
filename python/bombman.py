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

def workbook(n, k, arr):
    specialProblems = 0
    pageNum = 1
    
    for problems in arr:  # For each chapter
        for problem in range(1, problems + 1):  # For each problem in the chapter
            if problem == pageNum:
                specialProblems += 1
                
            # Increment page number if it's the last problem on the page
            # or if it's the last problem in the chapter
            if problem % k == 0 or problem == problems:
                pageNum += 1
                
    return specialProblems

def chocolateFeast(n, c, m):
    # Write your code here
    print(n,c,m)
    wrappers=n//c
    total=wrappers
    remainder=0
    while True:
        newBars=wrappers//m
        if newBars>=1:
            remainder=wrappers-newBars*m
            total+=newBars
            wrappers=newBars+remainder
        else:
            break
    return total

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        unique_elements = set(nums)
        frequency = {}
        for num in unique_elements:
            frequency[num] = nums.count(num)
        
        sorted_elements = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        
        result = [element[0] for element in sorted_elements[:k]]
        return result

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPr=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            if prices[i]>minPr:
                maxProfit=max(maxProfit,prices[i]-minPr)
            else:
                minPr=prices[i]
        return maxProfit
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1  # start with the smallest possible speed
        end = max(piles)  # the maximum speed needed could be the largest pile
        k = float('inf')

        while start <= end:
            mid = (start + end) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)  # calculate total hours to eat all bananas at speed 'mid'
            
            if hours <= h:
                k = min(mid, k)  # update minimum speed if this speed achieves within 'h' hours
                end = mid - 1
            else:
                start = mid + 1

        return k


def mergingIntervals(arr):
    if not arr:
        return []
    arr.sort()
    res=[]
    curr=arr[0]
    for i in range(1,len(arr)):
        p=arr[i]
        if p[0]<=curr[1]:
            curr[1]=max(curr[1],p[1])
        else:
            res.append(curr)
            curr=p
    res.append(curr)

    return res
        

print(mergingIntervals([[1, 3], [2, 6], [8, 10], [15, 18]])==[[1, 6], [8, 10], [15, 18]])

def crosswordPuzzle(crossword, words):
    # Write your code here
    solSteps=[]
    words = words.split(';')
    for i in range(len(crossword)):
       
        for j in range(len(crossword[i])):
            if crossword[i][j]=='-':
                if j<len(crossword[i])-1 and crossword[i][j+1]=='-' and (crossword[i][j-1]!='-' and j>0 ):
                    k=0
                    while crossword[i][j+k]=='-':
                       if j+k==9:
                           k+=1
                           break
                       k+=1
                    solSteps.append("h"+str(i)+str(j)+str(k))  
                elif j==0 and crossword[i][1]=='-':
                    k=0
                    while crossword[i][k]=='-':
                   
                       if k==9:
                           k=10
                           break
                       k+=1
                    solSteps.append("h"+str(i)+str(j)+str(k))
                elif  i<len(crossword)-1 and i> 0 and crossword[i+1][j]=='-' and crossword[i-1][j]!='-':
                    k=0
                    for x in range(i,len(crossword)):
                        if crossword[x][j]!='-':
                           break
                        k+=1
                    solSteps.append("v"+str(i)+str(j)+str(k))    
                elif  i== 0 and crossword[1][j]=='-':
                    k=0
                    for x in range(i,len(crossword)):
                        if crossword[x][j]!='-':
                           break
                        k+=1
                    solSteps.append("v"+str(i)+str(j)+str(k))    
    def canFillWord(word,blankword):
        orientation,row,col,size = blankword[0],blankword[1],blankword[2],blankword[3:]
        row,col,size = int(row),int(col),int(size)
        if len(word)!= size :
            return False
        if orientation=='v':
            for r in range(row, row+len(word)):
                if crossword[r][col]!="-" and crossword[r][col]!=word[r-row]:
                    return False
            for r in range(row, row+len(word)):
                if crossword[r][col]=="-" or crossword[r][col]==word[r-row]:
                    l=list(crossword[r])
                    l[col]=word[r-row]                
                    crossword[r]= "".join(l)
        if orientation=='h':
            for c in range(col, col+len(word)):
                if crossword[row][c]!="-" and crossword[row][c]!=word[c-col]:
                    return False
            l=list(crossword[row])
            for c in range(col,col+len(word)):
                if crossword[row][c]=="-" or crossword[row][c]==word[c-col]:
                    l[c] = word[c-col]
            crossword[row]="".join(l)
        return True    
    def unFill(word,blankword):
       
        orientation,row,col,size = blankword[0],int(blankword[1]),int(blankword[2]),int(blankword[3:])
        if orientation=='v':
            for r in range(row, row+len(word)):
                if crossword[r][col]==word[r-row]:
                    l=list(crossword[r])
                    l[col]="-"                
                    crossword[r]= "".join(l)
        if orientation=='h':
            l=list(crossword[row])
            for c in range(col,col+len(word)):
                if  crossword[row][c]==word[c-col]:
                    l[c] = "-"
            crossword[row]="".join(l)
           
    def solve(words,solSteps,i=0,k=0,done=[]):
        
        if len(done) == len(words):
            
            return crossword
       
        if canFillWord(words[i],solSteps[k]):
            
            if  words[i] not in done:
                if k < len(solSteps)-1:
                    k+=1
                done.append(words[i])
               
            
            i=0
           
            return solve(words,solSteps,i,k,done)
        else:
           
            if i < len(words)-1:
                i+=1
            else:
                i=0
               
                if done:
                    w = done[len(done)-1]
                    
                    for x in range(len(words)):
                        if len(words[x])==len(w) and words[x]!=w:
                            i = x
                            unFill(done[len(done)-1], solSteps[k-1])
                            
                            del done[len(done)-1]
                            if done:
                                
                                canFillWord(done[len(done)-1],solSteps[len(done)-1])
                            break
                    k = len(done)
                    print(words[i],solSteps[k])

                   
               
            return solve(words,solSteps,i,k,done)
    return solve(words,solSteps,i=0,k=0,done=[])