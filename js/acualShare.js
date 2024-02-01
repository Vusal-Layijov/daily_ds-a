function bonAppetit(bill, k, b) {
    let total = 0;

    for (let i = 0; i < bill.length; i++) {
        if (k != i) {
            total += bill[i];
        }
    }

    let actualShare = total / 2;

    if (b == actualShare) {
        console.log("Bon Appetit")
    } else {
        console.log(b - actualShare)
    }
}
function sockMerchant(n, ar) {
    // Write your code here
    let obj = {}
    let res = 0
    for (let s of ar) {
        if (s in obj) {
            obj[s] += 1
            if (obj[s] == 2) {
                res += 1
                obj[s] = 0
            }

        } else {
            obj[s] = 1
        }
    }
    return res
}
function icecreamParlor(m, arr) {
    for (let i = 0; i < arr.length; i++) {
        let balance = m - arr[i];
        let find = arr.findIndex((num, index) => {
            return i != index && num === balance
        })
        if (find != -1) {
            return [i + 1, find + 1]
        }
    }
}
const largestComponenet = (graph) =>{
    let longest=0
    let visited= new Set()
    for (let node in graph){
        let size = explore(graph,node,visited)
        if(size>longest)longest=size
    }
}
const explore = (graph,node,visited)=>{
    if (visited.has(node)) return 0
    let size=1
    visited.add(size)
    for (let neigh of graph[node]){
        size+= explore(graph,neigh,visited)
    }
    return size

}