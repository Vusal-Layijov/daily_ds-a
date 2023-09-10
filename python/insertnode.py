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


def icecreamParlor(m, cost):
    flavor_indices = {}  # A dictionary to store the indices of visited prices

    for i, price in enumerate(cost, start=1):
        complement = m - price  # Calculate the complement price

        if complement in flavor_indices:
            # If the complement price has been visited, return the indices
            return [flavor_indices[complement], i]

        flavor_indices[price] = i  # Store the current price's index

    return []
