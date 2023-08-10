function caesarCipher(s, k) {
    // Write your code here
    let lower = 'abcdefghijklmnopqrstuvwxyz'.split('')
    let upper = lower.map(el => el.toUpperCase())
    let togo = s.split('')
    for (let ind in s) {
        if (lower.includes(s[ind])) {
            let nextInd = (lower.indexOf(s[ind]) + k) % 26
            togo[ind] = lower[nextInd]

        }
        if (upper.includes(s[ind])) {
            let nextInd = (upper.indexOf(s[ind]) + k) % 26
            togo[ind] = upper[nextInd]
        }
    }
    return togo.join('')


}