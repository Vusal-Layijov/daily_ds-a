var topKFrequent = function (nums, k) {
    let result = {}
    for (let num of nums) {
        if (result[num]) {
            result[num] += 1
        } else {
            result[num] = 1
        }
    }

    let togo = []
    let arr = Object.entries(result)
    let max = -100000000000000
    let maxpair = []
    let ind
    console.log(result, arr)
    while (k) {
        for (let pair of arr) {
            if (pair[1] > max) {
                maxpair = pair
                max = pair[1]
            }
        }
        ind = arr.indexOf(maxpair)
        togo.push(maxpair[0])
        arr.splice(ind, 1)
        maxpair = []
        max = 0
        k--
    }
    return togo
};