const largestComponent = (graph) =>{
    const visited= new Set()
    let longest=0
    for(let node in graph){
       let size= exploreSize(graph,node, visited)
       if(size>longest) longest=size
    }
    return longest

}
const exploreSize= (graph,node,visited)=>{
    if(visited.has(node)) return 0
    visited.add(node)
    let size =1
    for(let neighboor of graph[node]){
        size+=exploreSize(graph,neighboor,visited)
    }
    return size
}