function quicksort(arr){
    if(arr.length<=1) return arr
    const pivot = arr[0]
    const left = []
    const right = []
    for (let i=1;i<arr.length; i++){
        let val = arr[i]
        if(val<=pivot) left.push(val)
        else right.push(val)
    }
    const leftsort = quicksort(arr)
    const rightsort=quicksort(arr)
    return [...leftsort, pivot, ...rightsort]
}