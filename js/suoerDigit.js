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


var canVisitAllRooms = function (rooms) {
    const visit = new Array(rooms.length).fill(false);
    const queue = [];

    queue.push(0);

    while (queue.length > 0) {
        const curr = queue.shift();
        visit[curr] = true;

        for (const v of rooms[curr]) {
            if (!visit[v]) {
                queue.push(v);
            }
        }
    }

    return visit.every(v => v);
};


