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