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