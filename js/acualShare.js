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