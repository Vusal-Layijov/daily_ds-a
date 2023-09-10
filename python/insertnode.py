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


def isBalanced(s):
    stack = []  # Initialize an empty stack

    # Define a dictionary to map closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the string
    for char in s:
        if char in bracket_pairs.values():
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_pairs.keys():
            # If it's a closing bracket
            if not stack:
                return "NO"  # There's no matching opening bracket, so it's unbalanced
            if stack[-1] == bracket_pairs[char]:
                stack.pop()  # Pop the matching opening bracket from the stack
            else:
                return "NO"  # The brackets are not balanced

    # After processing all characters, the stack should be empty if it's balanced
    return "YES" if not stack else "NO"
