function binaryserach(arr,target){
    let low=0
    let high=arr.length-1
    while (low<=high){
        let midp=Math.floor(low+high/2)
        if(arr[midp]==target) return true
        else if(target>arr[midp]){
            low=midp +1
        }
        else {
            high=midp-1
        }
    }
    return false

}
// depth search
function depthFirstTraversal(root){
    if(root ===null) return 
    const stack =[]
    stack.push(root)
    while(stack.length>0){
        let node =stack.pop()
        console.log(node.value)
       if(node.right) stack.push(node.right)
        if (node.left) stack.push(node.left)
    }
}

function depthSearchRecursive(root){
    if (root ===null) return []
   
    const left= depthSearchRecursive(root.left)
    const right = depthSearchRecursive(root.right)
 
    return [root.value,...left, ...right]
}

//breadth search traversal
function breadthFirstTraversal(root){
    const queue = []

    queue.push(root)
    while(queue.length>0){
       let node=queue.shift()
       console.log(node.value)
       queue.push(node.left)
       queue.push(node.right)
    }
}
const treeIncludesBreadth=(root, target ) =>{
    if(root===null) return false
    const queue = [root]
    while (queue.length>0){
        const current = queue.shift()
        if(current.value ===target) return true
        if(current.left) queue.push(current.left)
        if(current.right) queue.push(current.right)
    }
    return false
}
function treeIncludesRecursive(root, target) {
    if(root===null) return false
    if(root.value===target) return true
    return treeIncludesRecursive(root.left,target) || treeIncludesRecursive(root.right, target)
}

var maxDepth = function (root) {
    if (root === null) return 0
    console.log(root)
    let queue = [root]
    count = 0
    while (queue.length > 0) {
        let level = queue.length
        for (let i = 0; i < level; i++) {
            let current = queue.shift()
            if (current.left) queue.push(current.left)
            if (current.right) queue.push(current.right)
        }

        count += 1
    }
    return count
};

var findSon = function (r) {
    let res = []
    let s = [r]
    while (s.length > 0) {
        let node = s.pop()
        if (node.left) {
            s.push(node.left)
        }
        if (node.right) {
            s.push(node.right)
        }
        if (!node.left && !node.right) {
            res.push(node.val)
        }
    }
    return res


}

var leafSimilar = function (root1, root2) {
    let v1 = findSon(root1)
    let v2 = findSon(root2)
    return v1.join('') === v2.join('')
};
function preOrderRec(root) {
    let w = '';
    if (root) {
        w += `${root.data} `;
        w += preOrderRec(root.left);
        w += preOrderRec(root.right);
    }
    return w;
}
function preOrder(root) {
    const out = preOrderRec(root);
    console.log(out);
}
var mergeTwoLists = function (list1, list2) {
    let dum = new ListNode()
    let tail = dum
    while (list1 && list2) {
        if (list1.val <= list2.val) {
            tail.next = list1
            list1 = list1.next

        } else {
            tail.next = list2
            list2 = list2.next
        }
        tail = tail.next
    }
    if (list1) {
        tail.next - list1
    }
    if (list2) {
        tail.next = list2
    }
    return dum.next

};
var findJudge = function (n, trust) {
    let trustCount = new Array(n + 1).fill(0);

    for (let [a, b] of trust) {
        trustCount[a]--;
        trustCount[b]++;
    }

    for (let i = 1; i <= n; i++) {
        if (trustCount[i] === n - 1) {
            return i;
        }
    }

    return -1;
};

function generate(numRows) {
    if (numRows === 0) {
        return [];
    }

    let result = [[1]];

    for (let i = 1; i < numRows; i++) {
        let prevRow = result[result.length - 1];
        let newRow = [1];

        for (let j = 1; j < i; j++) {
            newRow.push(prevRow[j - 1] + prevRow[j]);
        }

        newRow.push(1);
        result.push(newRow);
    }

    return result;
}

// Example usage:
let numRows = 5;
let triangle = generate(numRows);
for (let row of triangle) {
    console.log(row);
}
