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
function bfs(n, m, edges, s) {
    const vis = new Array(n + 1).fill(false);
    const dis = {};
    const adj = new Array(n + 1).fill(null).map(() => []);

    edges.forEach((item) => {
        adj[item[0]].push(item[1]);
        adj[item[1]].push(item[0]);
    });

    const qu = [s];
    vis[s] = true;
    dis[s] = 0;

    while (qu.length > 0) {
        const ele = qu.shift();
        for (const nei of adj[ele]) {
            if (!vis[nei]) {
                vis[nei] = true;
                dis[nei] = 6 + dis[ele];
                qu.push(nei);
            }
        }
    }

    delete dis[0];
    delete dis[s];

    return Object.values(dis);
}
