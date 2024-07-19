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