const connectedComponenetsCount = (graph) =>{
    const visited = new Set()
    let count = 0
    for (let node in graph) {
        if(explore(graph,node,visited)===true){
            count +=1
        }
    }
    return count
}
const explore = (graph, current, visited) => {
    if(visited.has(String(current))) return false
    visited.add(current)
    for(let neighbour of graph[current]){
        explore(graph, neighbour, visited)
    }
    return true
}