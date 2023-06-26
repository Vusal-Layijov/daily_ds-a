const edges=[
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]
const shortestPath = (edges, nodeA,nodeB) =>{
    const graph = buildGraph(edges)
    let visited= new Set([nodeA])
    const queue = [[nodeA,0]]
    while(queue.length>0){
        const[node,distance]=queue.shift()
        if(node===nodeB) return distance
        for(let neighbour of graph[node]){
           if(!visited.has(neighbour)){
         queue.push([neighbour,distance+1])
         visited.add(neighbour)
           }    
        }
    }
    return -1
}
const buildGraph = (edges)=>{
    let graph ={}
    for (let edge of edges){
        const [a,b] =edge
        if(!(a in graph)) graph[a]=[]
        if(!(b in graph)) graph[b]=[]
        graph[a].push(b)
        graph[b].push(a)
    }
}  