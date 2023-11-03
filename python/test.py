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


class Solution:
    def removeStars(self, s: str) -> str:
        outputArr = []
        for chars in s:
            if chars == '*':
                outputArr.pop()
            else:
                outputArr.append(chars)

        return ''.join(outputArr)


def getMinSum(security_values, msg):
    n = len(msg)
    msg_values = [security_values[ord(ch) - ord('a')] for ch in msg]

    # Sort the message values in ascending order
    msg_values.sort()

    # Initialize two pointers, one at the beginning and one at the end of the sorted values
    left, right = 0, n - 1
    min_sum = 0

    while left < right:
        # Calculate the absolute difference between adjacent characters
        diff = msg_values[right] - msg_values[left]
        min_sum += diff

        # Move the pointers towards the center
        left += 1
        right -= 1

    return min_sum


# Example usage
security_values = [1, 2, 1, 3, 1, 3, 5, 7, 1, 1, 5,
                   5, 8, 10, 11, 1, 23, 2, 3, 7, 8, 9, 1, 6, 5, 9]
message = "afeb"
result = getMinSum(security_values, message)
print(result)  # Output: 2


class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            memo[n] = self.tribonacci(
                n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return memo[n]
