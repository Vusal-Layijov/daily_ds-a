# //Remove Nth Node From End of List

def removeN(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next

# copy linked list with random pointer
def copyrandom(head):
    oldtoCopy = {None: None}
    cur = head
    while cur:
        copy = ListNode(cur.val)
        oldtoCopy[cur] = copy
        cur = cur.next
    cur = head
    while cur:
        copy = oldtoCopy[cur]
        copy.next = oldtoCopy[cur.next]
        copy.random = oldtoCopy[cur.random]
        cur = cur.next
    return oldtoCopy[head]
