function binaryserach(arr,target){
    let low=0
    let high=arr.length-1
    while (low<=high){
        let midp=Math.floor(low+high/2)
        if(arr[midp]==target) return true
        else if(target>arr[midp]){
            low=midp +1
        }
        else {
            high=midp-1
        }
    }
    return false

}