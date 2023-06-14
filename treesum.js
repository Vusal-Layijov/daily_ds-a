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