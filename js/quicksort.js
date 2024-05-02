function quicksort(arr){
    if(arr.length<=1) return arr
    const pivot = arr[0]
    const left = []
    const right = []
    for (let i=1;i<arr.length; i++){
        let val = arr[i]
        if(val<=pivot) left.push(val)
        else right.push(val)
    }
    const leftsort = quicksort(arr)
    const rightsort=quicksort(arr)
    return [...leftsort, pivot, ...rightsort]
}

var threeSum = function (nums) {
    const res = [];
    nums.sort((a, b) => a - b)

    for (let i = 0; i < nums.length; i++) {
        const a = nums[i];
        if (a > 0) break;
        if (i > 0 && a === nums[i - 1]) continue;

        let l = i + 1;
        let r = nums.length - 1;
        while (l < r) {
            const threeSum = a + nums[l] + nums[r];
            if (threeSum > 0) {
                r--;
            } else if (threeSum < 0) {
                l++;
            } else {
                res.push([a, nums[l], nums[r]]);
                l++;
                r--;
                while (nums[l] === nums[l - 1] && l < r) {
                    l++;
                }
            }
        }
    }
    return res;
}