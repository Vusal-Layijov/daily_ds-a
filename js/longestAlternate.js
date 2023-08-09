function alternate(s) {
    // Write your code here
    let myset = new Set(s)
    let maxlength = 0
    for (let char1 of myset) {
        for (let char2 of myset) {
            if (char1 !== char2) {
                let length = 0
                let valid = true
                let prev = null
                for (let char of s) {
                    if (char === char1 || char === char2) {
                        if (char === prev) {
                            valid = false
                            break
                        }
                        length++
                        prev = char
                    }
                }
                if (valid) {
                    maxlength = Math.max(maxlength, length)
                }
            }
        }
    }
    return maxlength

}