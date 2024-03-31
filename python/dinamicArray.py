def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]  # Initialize n empty arrays
    lastAnswer = 0
    answers = []

    for query in queries:
        query_type, x, y = int(query[0]), int(query[1]), int(query[2])
        print(query_type, x, y)
        idx = (x ^ lastAnswer) % n  # Calculate index based on XOR operation
        if query_type == 1:
            arr[idx].append(y)
        elif query_type == 2:
            # Use modulo to get correct index
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


def gridChallenge(grid):
    # Write your code here

    some = []
    for st in grid:
        new = list(st)
        nn = list(sorted(new))
        some.append(nn)
    print('sssss', some)
    for i in range(len(some)-1):
        for j in range(len(some[0])):
            if some[i+1][j] < some[i][j]:
                return 'NO'
    return 'YES'

#removeNthFromEnd

def removeNthFromEnd(head, n):
    # Write your code here
    st=head
    c=1
    while st.next:
        st=st.next
        c+=1
    if c==1:
        return []
    current=head
    nextNode=current.next
    dummy=SinglyLinkedListNode(0)
    dummy.next=current
    r=c-n
    while current.next and r>0:
        dummy=current
        current=nextNode
        nextNode=current.next
        r-=1
    dummy.next=nextNode
    return head


#separateNumbers
def separateNumbers(s):
    if s[0] == '0' or len(s) == 1:
        print('NO')
        return
    
    for i in range(1, len(s) // 2 + 1):
        x = int(s[:i])
        beautiful_number = str(x)
        while len(beautiful_number) < len(s):
            x += 1
            beautiful_number += str(x)
        if beautiful_number == s:
            print('YES', s[:i])
            return
    
    print('NO')
def separateNumbers2(s):
    first = None
    for i in range(1, len(s)//2+1):
        first = int(s[0: i])
        n = 1
        j = i
        while j < len(s):
            if s[j:].startswith(str(first+n)):
                j += len(str(first+n))
                n += 1
            else:
                first = None
                break
        
        if first:
            break
    
    if first:
        print(f"YES {str(first)}")
    else:
        print("NO")
    
#making anagrams
def makingAnagrams(s1, s2):
    # Write your code here
    l1=list(s1)
    l2=list(s2)
    for l in s1:
        if l in l2:
            l1.remove(l)
            l2.remove(l)
    #maxAreaOfIsland
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        maxA=0
        visited=set()
        def bfs(r,c):
        
            direction=[[0,1],[0,-1],[1,0],[-1,0]]
            count=1
            q=[(r,c)]
            while len(q)>0:
                row,col=q.pop(0)
                for dr,dc in direction:
                    if row+dr in range(rows) and col+dc in range(cols) and (row+dr,col+dc) not in visited and grid[row+dr][col+dc]==1:
                        visited.add((row+dr,col+dc))
                        q.append((row+dr,col+dc))
                        count+=1
            return count
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    visited.add((i,j))
                    num=bfs(i,j)
                    maxA=max(maxA,num)
        return maxA