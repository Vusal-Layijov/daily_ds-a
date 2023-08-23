var canPartition = function (nums) {
    if (nums.reduce((acc, val) => acc + val, 0) % 2) {
        return false
    }
    let dp = new Set([0])
    let target = Math.floor(nums.reduce((acc, val) => acc + val, 0) / 2)
    for (let i = nums.length - 1; i--; i >= 0) {
        let nextDp = new Set()
        for (let sum of dp) {
            nextDp.add(sum + nums[i])
            nextDp.add(sum)
        }
        dp = nextDp

    }
    return dp.has(target)
};