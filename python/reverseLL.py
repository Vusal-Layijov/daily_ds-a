def reverse(llist):
    # Write your code here
    prev = None
    current = llist
    while current:
        nextN = current.next
        current.next = prev
        current.prev = nextN
        prev = current
        current = nextN
    return prev
