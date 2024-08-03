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
function beautifulPairs(A, B) {
    let total = 0;

    if (A.length === 1) {
        return total;
    }

    for (let i = 0; i < A.length; i++) {
        let a = A[i];
        let index = B.indexOf(a);
        if (index !== -1) {
            total += 1;
            B.splice(index, 1);
        }
    }

    if (total < A.length) {
        return total + 1;
    } else {
        return A.length - 1;
    }
}

// Example usage:
let A = [1, 2, 3, 4];
let B = [1, 2, 3, 3];
console.log(beautifulPairs(A, B)); // Output: 4
