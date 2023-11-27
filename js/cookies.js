function cookies(k, A) {
    // Write your code here
    let count = 0
    A.sort((a, b) => b - a)
    if (A[A.length - 1] >= k) {
        return count
    }
    while (A.length >= 2) {
        let least = A.pop()
        let secondLeast = A.pop()
        let newS = least + (2 * secondLeast)
        A.push(newS)
        count += 1
        A.sort((a, b) => b - a)
        if (A[A.length - 1] >= k) {
            return count
        }
    }
    return -1

}
