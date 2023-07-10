const hasPath = (graph, src, dst) =>{
    if (src===dst) return true
    for(let neighboor of graph[src] ){
        if(hasPath(graph,neighboor,dst)){
            return true
        }
    }
    return false
}
const hasPathBreadth = (graph, src, dst) =>{
    const queue = [src]
    if(src===dst) return true
    while(queue.length>0){
        const current = queue.shift()
        if(current===dst)return true
        for (let neighboor of graph[current]) {
            queue.push(neighboor)
        }
    }
    return false
}