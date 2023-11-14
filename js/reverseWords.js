var reverseWords = function (s) {
    let newA = s.split(' ')
    newA.reverse()
    console.log(newA)
    let son = newA.filter(word => word)
    console.log('ssss', son)
    return son.join(' ')
};
function hourglassSum(arr) {
    // Write your code here
    let maxS = -63
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            let nextS = arr[i].slice(j, j + 3).reduce((acc, cur) => acc + cur, 0)
            nextS += arr[i + 1][j + 1]
            nextS += arr[i + 2].slice(j, j + 3).reduce((acc, cur) => acc + cur, 0)
            maxS = Math.max(maxS, nextS)
        }

    }
    return maxS


}