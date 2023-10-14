function hackerlandRadioTransmitters(x, k) {
    // Write your code here
    let sorted = x.sort((a, b) => a - b)
    let count = 0
    let range = k
    let res = []
    for (let i = 0; i < sorted.length - 1; i++) {
        if (sorted[i + 1] - sorted[i] <= k && range) {
            range -= sorted[i + 1] - sorted[i]
            continue
        } else {
            res.push(sorted[i])
            count += 1
            range = k
        }

    }
    console.log(res)
    return count



}