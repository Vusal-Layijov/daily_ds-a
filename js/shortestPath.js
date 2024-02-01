const shortestPath = (edges, nodeA, nodeB)=>{
    let graph = buildGraph(edges)
    let visited=new Set([nodeA])
    let q= [[nodeA,0]]
    while(q.length>0){
        let [cur,dis]=q.shift()
        if(cur===nodeB) return dis
        for(let neigh of graph[cur]){
            if(!visited.has(neigh)){
                visited.add(neigh)
                q.push([neigh,dis+1])
            }
        }
    }
    return -1

}
const buildGraph= (edges) =>{
    const graph={}
    for (let edge of edges){
        const [a,b]=edge
        if(!(a in graph))  graph[a]=[]
        if (!(b in graph)) graph[b] = []
        graph[a].push(b)
        graph[b].push(a)

    }
    return graph
}