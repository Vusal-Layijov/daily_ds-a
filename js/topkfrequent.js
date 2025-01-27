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
var searchInsert = function (nums, target) {
    let start = 0
    let end = nums.length - 1

    while (start <= end) {
        let med = Math.floor((start + end) / 2)
        if (nums[med] === target) {
            return med
        } else if (nums[med] < target) {
            start = med + 1
        } else if (nums[med] > target) {
            end = med - 1
        }
    }
    return start
};
var guessNumber = function (n) {
    let low = 1;
    let high = n;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let res = guess(mid);
        if (res === 0) {
            return mid;
        } else if (res === 1) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
};
