"""
25. reverse nodes in k group

K 个一组翻转链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:
    """
    递归
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head


        pass

    def recursive(self, node: ListNode, count: int):
        pass
