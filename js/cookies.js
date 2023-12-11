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


function dayOfProgrammer(year) {
    // Write your code here
    let d = ''
    let m = ''
    if (year < 1918) {
        if (year % 4 == 0) {
            d = '12'
            m = '09'
        } else {
            d = '13'
            m = '09'
        }
    } else if (year == 1918) {
        d = '26'
        m = '09'
    } else {
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
            d = "12";
            m = "09";
        } else {
            d = "13";
            m = "09";
        }
    }
    return d + '.' + m + '.' + year
}