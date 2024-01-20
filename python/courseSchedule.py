def canFinish(numCourses,prerequisites):
    preMap={i:[] for i in range(numCourses)}
    for crs,pre in prerequisites:
        preMap[crs].append(pre)
    visitSet=set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs]==[]:
            return True
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        
        visitSet.remove(crs)
        preMap[crs]=[]
        return True
    for crs in range(numCourses):
        if not dfs(crs): return False
    return True

def hurdleRace(k, height):
    # Write your code here
    maxX=max(height)
    return maxX-k if maxX>k else 0


def angryProfessor(k, a):
    # Write your code here
    c=0
    for aS in a:
        if aS <=0:
            c+=1
    return 'NO' if c>=k else 'YES'

def beautifulDays(i, j, k):
    # Write your code here
    res=[]
    for num in range(i,j+1):
        r=str(num)
        new=int(r[::-1])
        print(new)
        if (num-new) % k==0:
            res.append(new)
    
    return len(res)

def viralAdvertising(n):
    # Write your code here
    cum=2
    curr=2
    for i in range(n-1):
        get=curr*3
        newC=get//2
        cum+=newC
        curr=newC
    return cum


def circularArrayRotation(a, k, queries):
    for _ in range(k):
        for i in range(len(a)-1,0,-1):
            tmp=a[i]
            a[i]=a[i-1]
            a[i-1]=tmp
            
    return a

def jumpingOnClouds(c, k):
    energy = 100
    index = 0
    while True:
        index = (index + k) % len(c)
        if c[index] == 1:
            energy -= 3
        else:
            energy -= 1
        if index == 0:
            break
    return energy
def findDigits(n):
    count = 0
    new = str(n)
    for d in new:
        if int(d) != 0 and n % int(d) == 0:
            count += 1
    return count
def appendAndDelete(s, t, k):    
    diff = 0
    shorter = min(len(s), len(t))
    for i in range(shorter):
        if s[i] != t[i] or i == shorter - 1:
            diff = i
            break    
    count = len(s) - diff + len(t) - diff
    if count <= k and (count - k) % 2 == 0:
        return "Yes"
    elif len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"
def squares(a, b):
    # Write your code here
    count=0
    for num in range(a,b+1):
        root=num**0.5
        if root.is_integer():
            count +=1
    return count