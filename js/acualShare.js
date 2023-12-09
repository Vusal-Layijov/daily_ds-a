function bonAppetit(bill, k, b) {
    let total = 0;

    for (let i = 0; i < bill.length; i++) {
        if (k != i) {
            total += bill[i];
        }
    }

    let actualShare = total / 2;

    if (b == actualShare) {
        console.log("Bon Appetit")
    } else {
        console.log(b - actualShare)
    }
}
function sockMerchant(n, ar) {
    // Write your code here
    let obj = {}
    let res = 0
    for (let s of ar) {
        if (s in obj) {
            obj[s] += 1
            if (obj[s] == 2) {
                res += 1
                obj[s] = 0
            }

        } else {
            obj[s] = 1
        }
    }
    return res
}