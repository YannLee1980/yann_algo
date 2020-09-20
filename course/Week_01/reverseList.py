# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None :
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur

s = Solution()

head = n = ListNode(1)
for i in range(2, 4):
    tmp = ListNode(i)
    n.next = tmp
    n = tmp

s.reverseList(head)