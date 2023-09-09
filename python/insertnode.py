def insertNodeAtPosition(llist, data, position):
    # Write your code here
    newNode = SinglyLinkedListNode(data)
    current = llist
    if position == 0:
        newNode.next = llist
        return newNode
    while position > 1 and current:
        current = current.next
        position -= 1
    next_node = current.next
    current.next = newNode
    newNode.next = next_node
    return llist
