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
// #max area of islands
var maxAreaOfIsland = function (grid) {
    let rows = grid.length;
    let cols = grid[0].length;
    let visit = new Set();

    function key(r, c) {
        return r + "," + c;
    }

    function dfs(r, c) {
        if (visit.has(key(r, c)) || r < 0 || r == rows || c < 0 || c == cols || grid[r][c] == 0) {
            return 0;
        }
        visit.add(key(r, c));
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1);
    }

    let maxI = 0;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            maxI = Math.max(maxI, dfs(r, c));
        }
    }
    return maxI;
};

let result = "";
const history = [""];

function processCommand(input) {
    const [command, option] = input.split(" ");
    switch (command) {
        case "1":
            result += option;
            history.push(result);
            break;
        case "2":
            result = result.slice(0, result.length - option);
            history.push(result);
            break;
        case "3":
            console.log(result[option - 1]);
            break;
        case "4":
            history.pop();
            result = history[history.length - 1];
            break;
        default:
            break;
    }
}

function processData(input) {
    input.split(/\r?\n/).forEach(e => processCommand(e))

}
function largestRectangle(h) {
    let stack = [];
    let maxArea = 0;
    let index = 0;

    while (index < h.length) {
        // Push the current bar to the stack if it's higher than the bar at stack top
        if (stack.length === 0 || h[stack[stack.length - 1]] <= h[index]) {
            stack.push(index++);
        } else {
            // Calculate area with h[tp] as the smallest (or minimum height) bar 'h'
            let tp = stack.pop();
            // If the stack is empty means the popped element was the smallest element so far
            let area = h[tp] * (stack.length === 0 ? index : index - stack[stack.length - 1] - 1);
            maxArea = Math.max(maxArea, area);
        }
    }

    // Now pop the remaining bars from stack and calculate area with every popped bar
    while (stack.length !== 0) {
        let tp = stack.pop();
        let area = h[tp] * (stack.length === 0 ? index : index - stack[stack.length - 1] - 1);
        maxArea = Math.max(maxArea, area);
    }

    return maxArea;
}

// Example usage
const heights = [1, 2, 3, 4, 5];
console.log(largestRectangle(heights)); // Output: 9
