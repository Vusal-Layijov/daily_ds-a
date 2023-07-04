def findOrder(numCourses, prerequisites):
    preReq={c:[] for c in range(numCourses)}
    for crs,pre in prerequisites:
       preReq[crs].append(pre)
    output=[]
    visit, cycle =set(), set()
    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True
        cycle.add(crs)
        for pre in preReq[crs]:
            if dfs(pre)==False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True
    for c in range(numCourses):
        if dfs(c)==False:
            return []
    return output
