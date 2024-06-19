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


function gridChallenge(grid) {
    // Write your code here
    let res = []
    for (let r of grid) {
        let s = r.split('')
        s.sort()
        res.push(s.join(''))
    }
    let ROWS = grid.length
    let COLS = grid[0].length

    for (let r = 1; r < ROWS; r++) {
        for (let c = 1; c < COLS; c++) {
            if (res[c][r] < res[c - 1][r - 1]) {
                return 'NO'
            }
        }
    }
    return 'YES'
}

function jimOrders(orders) {
    // Write your code here

    let i = 1
    let obj = {}
    let res = []
    for (let o of orders) {
        let t = o[0] + o[1]
        obj[i] = t
        i++
    }
    let keyV = Object.entries(obj)
    keyV.sort((a, b) => a[1] - b[1])
    return keyV.map(a => parseInt(a[0]))
}