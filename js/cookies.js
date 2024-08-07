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
function chiefHopper(arr) {
    let low = 0;
    let high = Math.max(...arr);

    while (low < high) {
        let mid = Math.floor((low + high) / 2);
        if (isValidEnergy(mid, arr)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    return low;
}

function isValidEnergy(startEnergy, arr) {
    let energy = startEnergy;
    for (let height of arr) {
        if (energy < height) {
            energy -= (height - energy);
        } else {
            energy += (energy - height);
        }
        if (energy < 0) {
            return false;
        }
    }
    return true;
}

// Example usage:
let arr = [3, 4, 3, 2, 4];
console.log(chiefHopper(arr)); // Output: 4


function solve(n, operations) {
    // Write your code here
    // let arr= new Array(n+1).fill(0)
    // console.log(arr)
    // for (let o of operations){
    //     for(let i =o[0]; i<=o[1];i++){
    //         arr[i]+=o[2]
    //     }
    // }
    // let sum= arr.reduce((acc,ele)=>acc+ele,0)
    // return parseInt(sum/n)
    let sum = 0
    for (let o of operations) {
        let m = o[1] - o[0] + 1
        sum += m * o[2]
    }
    return parseInt(sum / n)

}
function sherlockAndMinimax(arr, p, q) {
    // Write your code here
    let myObj = {}
    for (let n of arr) {
        for (let i = q; i >= p; i--) {
            if (i in myObj) {
                myObj[i].push(Math.abs(i - n))
            } else {
                myObj[i] = [Math.abs(i - n)]
            }
        }
    }
    let minK = Infinity
    let maxV = -Infinity
    for (let [key, val] of Object.entries(myObj)) {
        let curK = parseInt(key)
        let curMaxV = Math.max(...val)
        if (curMaxV > maxV) {
            maxV = curMaxV
            minK = curK
        }
    }
    return minK

}