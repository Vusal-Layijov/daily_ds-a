function removeNthFromEnd(head, n) {
    let current = head;
    let count = 0;

    // Calculate the total number of nodes
    while (current) {
        count += 1;
        current = current.next;
    }

    // If there's only one node or n is out of range, return null
    if (count === 1 || n > count) {
        return null;
    }

    // Handle the case where you want to remove the first node
    if (n === count) {
        return head.next;
    }

    // Find the node before the one to be removed
    count = count - n - 1;
    current = head;

    while (count > 0) {
        current = current.next;
        count -= 1;
    }

    // Remove the nth node
    current.next = current.next.next;

    return head;
}
var isAlienSorted = function (words, order) {
    let myObj = {}
    for (let i = 0; i < order.length; i++) {
        myObj[order[i]] = i
    }
    for (let i = 0; i < words.length - 1; i++) {
        let w1 = words[i]
        let w2 = words[i + 1]
        for (let j = 0; j < w1.length; j++) {
            if (j == w2.length) return false
            if (w1[j] != w2[j]) {
                if (myObj[w2[j]] < myObj[w1[j]]) {
                    return false
                } else {
                    break
                }
            }
        }
    }
    return true
};