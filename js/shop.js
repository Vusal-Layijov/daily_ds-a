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