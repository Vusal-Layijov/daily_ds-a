function balancedSums(arr) {
    // Write your code here
    let summ = arr.reduce((abv, val) => abv + val, 0)
    let left = 0
    for (let num of arr) {
        if (left == summ - num - left) {
            return 'YES'
        }
        left += num
    }
    return 'NO'
}