"""
24. swap nodes in pairs

两两交换链表中的节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:
    """
    递归
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nxt = head.next
        head.next = self.swapPairs(nxt.next)
        nxt.next = head
        return nxt


class Solution2:
    """
    迭代 + 虚头节点
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # dummy head
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur is not None:
            nxt = cur.next
            if nxt is None:
                break
            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            prev = cur
            cur = cur.next

        return dummy.next
