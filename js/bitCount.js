function sumXor(n) {
    // Write your code here
    if (n == 0) return 1
    let bitcount = n.toString(2).split('0').length - 1
    return 2 ** bitcount


}
var longestConsecutive = function (nums) {
    let numSet = new Set(nums)
    let longest = 0
    for (let n of nums) {
        if (!numSet.has(n - 1)) {
            length = 0
            while (numSet.has(n + length)) {
                length += 1
            }
            longest = Math.max(length, longest)
        }
    }
    return longest
};
var findMin = function (nums) {
    return Math.min(...nums)
};
function maximumToys(prices, k) {
    // Write your code here
    prices.sort((a, b) => a - b)
    let total = 0
    let i = 0
    while (k >= 0 && prices[i] <= k) {
        k -= prices[i]
        total += 1
        i += 1
    }
    return total
}
function halloweenParty(k) {
    // Write your code here
    if (k == 1) return 0
    if (k == 2) return 1
    if (k == 3) return 2
    if (k % 2 == 0) {
        return (k / 2) ** 2
    } else {
        let f = Math.floor(k / 2)
        let s = f + 1
        return f * s
    }
}