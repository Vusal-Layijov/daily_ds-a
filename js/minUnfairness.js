function minUnFairness(k,arr){
    arr.sort((a,b)=>a-b)
    let minU=Infinity
    for (let i=0; i<=arr.length-k;i++){
        let unfair=arr[i+k-1]-arr[i]
        minU=Math.min(minU,unfair)
    }
    return minU
}
function largestPermutation(k, arr) {
    const n = arr.length;
    const pos = new Map();

    // Create a map to store the position of each element
    for (let i = 0; i < n; i++) {
        pos.set(arr[i], i);
    }

    for (let i = 0; i < n && k > 0; i++) {
        // The value that should be here if the array was sorted in descending order
        const valueToPlace = n - i;

        // If the value is already in the correct place, continue
        if (arr[i] === valueToPlace) {
            continue;
        }

        // Find the position of the valueToPlace
        const posToSwap = pos.get(valueToPlace);

        // Swap the values in the array
        [arr[i], arr[posToSwap]] = [arr[posToSwap], arr[i]];

        // Update the positions in the map
        pos.set(arr[posToSwap], posToSwap);
        pos.set(arr[i], i);

        // Decrement k as we used one swap
        k--;
    }

    return arr;
}