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