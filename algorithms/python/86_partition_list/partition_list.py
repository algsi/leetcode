"""
86. partition list

https://leetcode.com/problems/partition-list/
https://leetcode-cn.com/problems/partition-list/

分隔链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    模拟
    """

    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head, large_head = ListNode(0), ListNode(0)
        small_cursor, large_cursor = small_head, large_head
        cur = head

        while cur:
            if cur.val < x:
                small_cursor.next = cur
                small_cursor = small_cursor.next
            else:
                large_cursor.next = cur
                large_cursor = large_cursor.next
            cur = cur.next

        # escape cycle in the list
        small_cursor.next = None
        large_cursor.next = None

        if small_head.next is None:
            return large_head.next
        else:
            small_cursor.next = large_head.next
            return small_head.next
