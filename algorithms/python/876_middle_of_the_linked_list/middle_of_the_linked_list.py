"""
876. middle of the linked list

https://leetcode.com/problems/middle-of-the-linked-list/
https://leetcode-cn.com/problems/middle-of-the-linked-list/

链表的中间节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    快慢指针

    快指针一次走两步，慢指针一次走一步
    """

    def middleNode(self, head: ListNode) -> ListNode:
        """
        当有两个中间节点时，该方法返回当时第二个中间节点
        """
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode2(self, head: ListNode) -> ListNode:
        """
        当有两个中间节点时，该方法返回当时第一个中间节点
        """
        if not head:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            # 增加一个条件，少走一步
            slow = slow.next
            fast = fast.next.next
        return slow
