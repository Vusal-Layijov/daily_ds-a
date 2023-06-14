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