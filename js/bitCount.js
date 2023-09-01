function sumXor(n) {
    // Write your code here
    if (n == 0) return 1
    let bitcount = n.toString(2).split('0').length - 1
    return 2 ** bitcount


}