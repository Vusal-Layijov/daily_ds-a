// You have a 2 - D grid of size m x n representing a box, and you have n balls.The box is open on the top and bottom sides.

// Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

// A board that redirects the ball to the right spans the top - left corner to the bottom - right corner and is represented in the grid as 1.
// A board that redirects the ball to the left spans the top - right corner to the bottom - left corner and is represented in the grid as -1.
// We drop one ball at the top of each column of the box.Each ball can get stuck in the box or fall out of the bottom.A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

// Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or - 1 if the ball gets stuck in the box.
 function findball(grid){
    let m = grid.length
    let n = grid[0].length
    let ans = new Array(n).fill(-1)
    for (let i =0; i<n; i++){
        let row=0
        let col=i
        let direction = 1
        while(row<m){
            if (grid[row][col] ===1){
                if(col===n-1 || grid[row][col+1]===-1){
                    break
                }
                col +=1
                direction=1
            }
            else{
                if(col==0 || grid[row][col-1]===1){
                    break
                }
                col -=1
                direction =-1
            }
            row+=1
        }
        if(row===m){
            ans[i]=col
        }
    }
    return ans

}
findball([[-1,1,1]])

// reorder linked list
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)

}
class LinkedList {
    constructor(head) {
        this.head = head
    }
}
let node6 = new ListNode(8)
let node5 = new ListNode(3, node6)
let node4 = new ListNode(7, node5)
let node3 = new ListNode(4, node4)
let node2 = new ListNode(2, node3)
let node1 = new ListNode(1, node2)
let current = new LinkedList(node1)


// let current2 = new LinkedList(node4)

function reorder(head) {
    let slow = head
    let fast = head.next
    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }
    let second = slow.next
    slow.next = null
    let prev = null
    while (second) {
        let tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    }
    let first = head
    second = prev
    while (second) {
        let temp1 = first.next
        let temp2 = second.next
        first.next = second
        second.next = temp1
        second = temp2
        first = temp1
    }
    return head
}
console.log(reorder(current.head))