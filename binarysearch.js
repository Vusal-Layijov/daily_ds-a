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