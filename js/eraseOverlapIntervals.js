var eraseOverlapIntervals = function (intervals) {
    intervals.sort((a, b) => a[1] - b[1])
    let count = 0
    let end = -Infinity
    for (let interval of intervals) {
        if (interval[0] >= end) {
            end = interval[1]
        } else {
            count += 1
        }
    }
    return count
};

function toys(w) {
    // Write your code here
    w.sort((a, b) => a - b)
    let count = 1
    let s = 0
    let end = 1
    while (end < w.length) {
        if (w[end] - w[s] <= 4) {
            end += 1
        } else {
            count += 1
            s = end
        }
    }
    return count

}