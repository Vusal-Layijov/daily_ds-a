function shop(n, k, centers, roads) {
    const r = roads.reduce((acc, [a, b, cost]) => {
        if (!acc[a]) {
            acc[a] = [];
        }
        if (!acc[b]) {
            acc[b] = [];
        }
        acc[a].push([b, cost]);
        acc[b].push([a, cost]);
        return acc;
    }, new Array(n + 1));

    const lowest = [];
    for (let i = 0; i < n + 1; i += 1) {
        lowest.push(new Array(2 ** k).fill(null));
    }

    const c = centers.map(
        (item) => item.split(` `).slice(1).reduce((acc, it) => acc + 2 ** (it - 1), 0)
    );
    lowest[1][c[0]] = 0;

    const queue = [1];

    while (queue.length) {
        const center = queue.shift();
        r[center].forEach(([to, cost]) => {
            let isRefreshed = false;
            const fishes = c[to - 1];
            lowest[center].forEach((item, i) => {
                if (lowest[center][i] === null) {
                    return;
                }
                const b = (i | fishes);
                if (!lowest[to][b] || lowest[to][b] > item + cost) {
                    lowest[to][b] = item + cost;
                    isRefreshed = true;
                }
            });
            if (isRefreshed) {
                queue.push(to);
            }
        });
    }

    let min = lowest[n][2 ** k - 1] || Infinity;
    for (let i = 0; i < lowest[n].length - 1; i += 1) {
        if (!lowest[n][i]) {
            continue;
        }
        for (let j = i + 1; j < lowest[n].length; j += 1) {
            if (!lowest[n][j]) {
                continue;
            }
            if ((i | j) === 2 ** k - 1) {
                min = Math.min(min, Math.max(lowest[n][i], lowest[n][j]));
            }
        }
    }

    return min;
}

function lonelyinteger(a) {
    // Write your code here
    let myObj = {}
    for (let num of a) {
        if (num in myObj) {
            myObj[num] += 1
        } else {
            myObj[num] = 1
        }
    }
    for (let [key, value] of Object.entries(myObj)) {
        if (value == 1) return key
    }

}
var minCostClimbingStairs = function (cost) {

    cost.push(0)
    for (let i = cost.length - 3; i >= 0; i--) {
        cost[i] += Math.min(cost[i + 1], cost[i + 2])
    }
    return Math.min(cost[0], cost[1])
};
var findOrder = function (numCourses, prerequisites) {
    let ord = [];
    let preList = new Array(numCourses).fill(0).map(() => []);

    for (let p of prerequisites) {
        preList[p[0]].push(p[1]);
    }

    let visited = new Array(numCourses).fill(0);

    function dfs(c) {
        if (visited[c] === 1) return false; // cycle detected
        if (visited[c] === 2) return true; // already processed

        visited[c] = 1; // mark as visited (in recursion stack)

        for (let p of preList[c]) {
            if (!dfs(p)) {
                return false;
            }
        }

        visited[c] = 2; // mark as fully processed
        ord.push(c);

        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (visited[i] === 0) {
            if (!dfs(i)) {
                return []; // cycle detected, return empty array
            }
        }
    }

    return ord;
};
var invertTree = function (root) {
    if (!root) return null
    let tmp = root.left
    root.left = root.right
    root.right = tmp
    invertTree(root.left)
    invertTree(root.right)
    return root
};
var wordBreak = function (s, wordDict) {
    let newArray = new Array(s.length + 1).fill(false);
    newArray[s.length] = true; 

    for (let i = s.length - 1; i >= 0; i--) {
        for (let w of wordDict) {
            if (i + w.length <= s.length && s.substring(i, i + w.length) === w) {
                newArray[i] = newArray[i + w.length];
                if (newArray[i]) break; 
            }
        }
    }
    return newArray[0];
};
var isIsomorphic = function (s, t) {
    if (s.length !== t.length) return false;

    let mapST = {}; // Object for s -> t mapping
    let mapTS = {}; // Object for t -> s mapping

    for (let i = 0; i < s.length; i++) {
        let charS = s[i];
        let charT = t[i];

        // Check s -> t mapping
        if (mapST[charS] && mapST[charS] !== charT) {
            return false;
        }
        // Check t -> s mapping
        if (mapTS[charT] && mapTS[charT] !== charS) {
            return false;
        }

        // Create mappings
        mapST[charS] = charT;
        mapTS[charT] = charS;
    }

    return true;
};
