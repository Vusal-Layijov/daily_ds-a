// Merge Sort out-of-place
// Do not modify the original array
function mergeSort(arr) {

    // Check if the input is length 1 or less
    // If so, it's already sorted: return
    if (arr.length <= 1) return arr;

    // Divide the array in half
    const mid = Math.floor(arr.length / 2);

    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
    // Recursively sort the left half
    const leftSort = mergeSort(left);
    // Recursively sort the right half
    const rightSort = mergeSort(right);
    // Merge the halves together and return
    return merge(leftSort, rightSort);
}


// Takes in two sorted arrays and returns them merged into one
function merge(arrA, arrB) {

    // Create an empty return array
    const res = [];
    // Point to the first value of each array
    let indexA = 0;
    let indexB = 0;
    // While there are still values in each array...
    while (indexA < arrA.length && indexB < arrB.length) {
        // Compare the first values of each array
        // Add the smaller value to the return array
        // Move the pointer to the next value in that array
        if (arrA[indexA] <= arrB[indexB]) {
            res.push(arrA[indexA]);
            indexA++;
        } else {
            res.push(arrB[indexB]);
            indexB++;
        }
    }

    // Return the return array
    return [...res, ...arrA.slice(indexA), ...arrB.slice(indexB)]
}

function closestNumbers(arr) {
    // Write your code here
    arr.sort(function (a, b) { return a - b })
    let diff = arr[1] - arr[0]
    let temp = 0

    for (let x = 2; x < arr.length; x++) {
        temp = arr[x] - arr[x - 1]
        if (temp <= diff) {
            diff = temp
        }
    }

    let data = []

    for (let index = 1; index < arr.length; index++) {
        if (arr[index] - arr[index - 1] === diff) {
            data.push(arr[index - 1], arr[index])
        }
    }

    return data
}