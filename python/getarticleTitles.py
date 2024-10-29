import requests

def getArticleTitles(author):
    # Write your code here
    titles=[]
    res=[]
    data=fetch_data(author,1)
    titles.append(data['data'])
    total_pages=data['total_pages']
    for i in range(2,total_pages+1):
        ret=fetch_data(author,i)
        titles.append(ret['data'])
    print(titles)
    for i in range(len(titles)):
        for obj in titles[i]:
            if obj['title']:
                res.append(obj['title'])
            if not obj['title'] and obj['story_title']:
                res.append(obj['story_title'])
    return res   
    
    
def fetch_data(author_name, page_num):
    # Base URL
    base_url = 'https://jsonmock.hackerrank.com/api/articles'

    # Parameters
    params = {
        'author': author_name,
        'page': page_num
    }

    # Making the request
    response = requests.get(base_url, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        return data
        # Handle the data
        # You can process or display the data as required
    else:
        print(f"Failed to retrieve data: {response.status_code}")

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)
            return perim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)







        