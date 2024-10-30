var cloneGraph = function (node) {
    let oldToNew = new Map();

    const dfs = function (node) {

        if (oldToNew.has(node)) {
            return oldToNew.get(node);
        }

        // Clone the node
        let copy = new Node(node.val, []);
        oldToNew.set(node, copy);


        node.neighbors.forEach(nei => {
            copy.neighbors.push(dfs(nei));
        });

        return copy;
    };

    return node ? dfs(node) : null;
};
function findJudge(n, trust) {
    const trustCount = {};  // Equivalent of myobg in Python
    const trustedByOthers = {};  // Equivalent of ob2 in Python

    // Initialize objects with default values
    for (let i = 1; i <= n; i++) {
        trustCount[i] = 0;
        trustedByOthers[i] = 0;
    }

    // Populate trustCount and trustedByOthers
    for (const [src, dst] of trust) {
        trustCount[dst] += 1;  // Increase count for person being trusted
        trustedByOthers[src] += 1;  // Increase count for person who trusts someone else
    }

    // Find the judge
    for (let i = 1; i <= n; i++) {
        if (trustCount[i] === n - 1 && trustedByOthers[i] === 0) {
            return i;
        }
    }

    return -1;  // Return -1 if no judge found
}
