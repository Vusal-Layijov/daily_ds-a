function minUnFairness(k,arr){
    arr.sort((a,b)=>a-b)
    let minU=Infinity
    for (let i=0; i<=arr.length-k;i++){
        let unfair=arr[i+k-1]-arr[i]
        minU=Math.min(minU,unfair)
    }
    return minU
}