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

