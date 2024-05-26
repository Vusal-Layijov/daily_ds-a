function minimumMoves(grid, startX, startY, goalX, goalY) {
    // Write your code here

    //if start === goal
    if (startX === goalX && startY === goalY) return 0;

    //initializing variables
    const rows = grid.length;

    const cols = grid[0].length;

    const goal = String(goalX) + '-' + String(goalY);

    let level = 1;

    let levelNodes = new Set();

    let nextLevelNodes = new Set();

    let visited = new Set();

    //initializing iterations
    levelNodes.add(startX + '-' + startY);

    visited.add(startX + '-' + startY);

    updateNext(startX + '-' + startY);

    let iterator;

    while (nextLevelNodes.size > 0) {
        levelNodes = nextLevelNodes;
        nextLevelNodes = new Set();
        iterator = levelNodes.entries();
        for (const entry of iterator) {
            if (entry[0] === goal) {
                return level;
            } else {
                visited.add(entry[0]);
                updateNext(entry[0]);
            }
        }
        level++;
    }
    return 'There is no path from start to goal.';

    //subfunction to find the next elements to be checked
    function updateNext(str) {
        //defining increments to right, left, top and down directions 

        let increments = [[1, 0], [-1, 0], [0, 1], [0, -1]];

        let [dx, dy, x, y] = [0, 0, 0, 0];

        for (let i = 0; i < 4; i++) {

            dx = increments[i][0];

            dy = increments[i][1];

            x = Number(str.split('-')[0]) + dx;

            y = Number(str.split('-')[1]) + dy;

            while (y < cols && x < rows && y > -1 && x > -1) {

                if (grid[x][y] === 'X') break;

                if (!visited.has(String(x) + '-' + String(y))) {

                    nextLevelNodes.add(String(x) + '-' + String(y));
                }
                x += dx;

                y += dy;
            }
        }
    }

}

var longestPalindrome = function (s) {
    let longest = 0
    let res = ''
    for (let i = 0; i < s.length; i++) {
        let l = i
        let r = i
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            if (r - l + 1 > longest) {
                longest = r - l + 1
                res = s.slice(l, r + 1)
            }
            l--
            r += 1
        }
        l = i
        r = i + 1
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            if (r - l + 1 > longest) {
                longest = r - l + 1
                res = s.slice(l, r + 1)
            }
            l--
            r += 1
        }
    }
    return res
};
function orangesRotting(grid) {
    let q = [];
    let fresh = 0;
    let time = 0;

    // Initialize the queue with all rotten oranges and count fresh oranges
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            if (grid[r][c] === 1) {
                fresh += 1;
            }
            if (grid[r][c] === 2) {
                q.push([r, c]);
            }
        }
    }

    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    while (fresh > 0 && q.length > 0) {
        let length = q.length;
        for (let i = 0; i < length; i++) {
            let [r, c] = q.shift();

            for (let [dr, dc] of directions) {
                let row = r + dr;
                let col = c + dc;

                // If in bounds and fresh orange, make it rotten and add to queue
                if (
                    row >= 0 && row < grid.length &&
                    col >= 0 && col < grid[0].length &&
                    grid[row][col] === 1
                ) {
                    grid[row][col] = 2;
                    q.push([row, col]);
                    fresh -= 1;
                }
            }
        }
        time += 1;
    }

    return fresh === 0 ? time : -1;
}
var topKFrequent = function (nums, k) {
    const uniqueElements = new Set(nums);
    const frequency = {};
    uniqueElements.forEach(num => {
        frequency[num] = nums.filter(n => n === num).length;
    });

    const sortedElements = Object.entries(frequency).sort((a, b) => b[1] - a[1]);


    const result = sortedElements.slice(0, k).map(element => parseInt(element[0]));

    return result;
};
var pacificAtlantic = function (heights) {
    let ROWS = heights.length
    let COLS = heights[0].length
    let pac = new Set()
    let atl = new Set()
    function dfs(r, c, visit, prevHeight) {
        if (visit.has(`${r},${c}`) || r < 0 || c < 0 || r == ROWS || c == COLS || heights[r][c] < prevHeight) {
            return
        }
        visit.add(`${r},${c}`)
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
    }
    for (let c = 0; c < COLS; c++) {
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
    }
    for (let r = 0; r < ROWS; r++) {
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])
    }
    let res = []
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (pac.has(`${r},${c}`) && atl.has(`${r},${c}`)) {
                res.push([r, c])
            }
        }
    }
    return res
};

var solve = function (board) {
    let ROWS = board.length
    let COLS = board[0].length
    function dfs(r, c) {
        if (r < 0 || c < 0 || r == ROWS || c == COLS || board[r][c] != 'O') return
        board[r][c] = 'T'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    }
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (board[r][c] == 'O' && ([0, ROWS - 1].indexOf(r) != -1 || [0, COLS - 1].indexOf(c) != -1)) {
                dfs(r, c)
            }
        }
    }
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (board[r][c] == 'O') board[r][c] = 'X'
        }
    }
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (board[r][c] == 'T') board[r][c] = 'O'
        }
    }

};