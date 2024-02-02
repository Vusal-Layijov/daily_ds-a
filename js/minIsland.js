const minIsland = (grid) =>{
    let visited= new Set()
    let minSize=Infinity
    for (let r=0; r<grid.length; r++){
        for(let c=0; c<grid[0].length; c++){
            let size=exploreSize(grid, r,c,visited)
            if(size>0 && size<minSize){
                minSize=size
            }
        }
    }
    return minSize
}

const exploreSize=(grid,r,c,visited)=>{
    let rowInBounds= 0<=r && r<grid.length
    let colInBounds= 0<=c && c<grid[0].length
    if(!rowInBounds || !colInBounds)return 0
    if(grid[r][c]==='W') return 0
    let pos= r+','+c
    if(visited.has(pos)) return 0
    visited.add(pos)
    let size =1
    size+=exploreSize(grid,r-1,c,visited)
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r , c-1, visited)
    size += exploreSize(grid, r , c+1, visited)
    return size

}