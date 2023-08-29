function superDigit(n, k) {
    // Calculate the sum of digits of the given number
    function digitSum(number) {
        let sum = 0
        for (let digit of number) {
            sum += parseInt(digit)
        }
        return sum.toString()
    }

    // Calculate the super digit recursively
    function calculateSuperDigit(number) {
        if (number.length === 1) {
            return parseInt(number)
        }
        const sum = digitSum(number)
        return calculateSuperDigit(sum)
    }

    // Calculate super digit of n*k
    const concatenatedNumber = n.repeat(k)
    return calculateSuperDigit(concatenatedNumber)
}
