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
function hackerlandRadioTransmitters(x, k) {
    x.sort((a, b) => a - b); // Sort house locations in ascending order
    const n = x.length;
    let transmitters = 0;
    let i = 0;

    while (i < n) {
        transmitters++; // Place a transmitter
        let loc = x[i];

        // Move to the rightmost house that can be covered
        while (i < n && x[i] <= loc + k) {
            i++;
        }

        loc = x[i - 1];

        // Move to the right of the transmitter's range
        while (i < n && x[i] <= loc + k) {
            i++;
        }
    }

    return transmitters;
}

// Example usage:


