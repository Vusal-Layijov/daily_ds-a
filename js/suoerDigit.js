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


var isBalanced = function (root) {
    function dfs(root) {
        if (!root) return [true, 0]
        let left = dfs(root.left)
        let right = dfs(root.right)
        let balanced = (left[0] && right[0] && Math.abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + Math.max(left[1], right[1])]
    }
    return dfs(root)[0]
};


function parseAgeToMinutes(age) {
    const [value, unit] = age.split(' ');

    if (unit.includes('minute')) {
        return parseInt(value); // Convert minutes to minutes
    } else if (unit.includes('hour')) {
        return parseInt(value) * 60; // Convert hours to minutes
    }
    // You can add more conditions if needed (like days, weeks, etc.)
    return 0; // Default if the format is not recognized
}

function isArraySorted(arr) {
    for (let i = 1; i < arr.length; i++) {
        const prev = parseAgeToMinutes(arr[i - 1].age);
        const current = parseAgeToMinutes(arr[i].age);

        if (prev > current) {
            return false;
        }
    }
    return true;
}