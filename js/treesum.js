  const treesum = (root)=>{
    if (root===null) return 0
    return root.val + treesum(root.left) + treesum(root.right)
  }
const tresumIterative = (root) =>{
    const stack = [root]
    const total =0
    while (stack.length>0){
        const node = stack.pop()
        total+=node.val
        if(node.left) stack.push(node.left)
        if(node.right) stack.push(node.right)
    }
    return total
}
const treeMinValue = (root) =>{
    let smallest = Infinity
    const stack =[root]
    while (stack.length>0){
        const current = stack.pop()
        if(current.val<smallest) smallest=current.val
        if(current.left !==null) stack.push(current.left)
        if(current.right !==null) stack.push(current.right)

    }
    return smallest
}
const treeMinValueRecur = (root) =>{
    if(root===null) return Infinity
    return Math.min(root.val,treeMinValueRecur(root.left),treeMinValueRecur(root.right))
}

var characterReplacement = function (s, k) {
    let count = {};
    let maxF = 0;
    let l = 0;
    let res = 0;

    for (let r = 0; r < s.length; r++) {
        count[s[r]] = (count[s[r]] || 0) + 1;
        maxF = Math.max(maxF, count[s[r]]);

        while ((r - l + 1) - maxF > k) {
            count[s[l]] -= 1;
            l += 1;
        }

        res = Math.max(res, r - l + 1);
    }

    return res;
};
function minimumAbsoluteDifference(arr) {
    // Write your code here
    let res = Infinity
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (Math.abs(arr[i] - arr[j]) < res) {
                res = Math.abs(arr[i] - arr[j])
            }
        }
    }
    return res
}

var generate = function (numRows) {
    let res = [[1]];
    for (let i = 0; i < numRows - 1; i++) {
        let tmp = [0];
        tmp = tmp.concat(res[res.length - 1]);
        tmp.push(0);
        let row = [];
        for (let j = 0; j < res[res.length - 1].length + 1; j++) {
            row.push(tmp[j] + tmp[j + 1]);
        }
        res.push(row);
    }
    return res;
};