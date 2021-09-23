"""
92. reverse linked list ii

https://leetcode.com/problems/reverse-linked-list-ii/
https://leetcode-cn.com/problems/reverse-linked-list-ii/

反转链表 II
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head_node: ListNode):
            """
            反转链表，也可以使用递归法，这里使用迭代法
            """
            pre = None
            cur = head_node
            while cur:
                next_node = cur.next
                cur.next = pre
                pre = cur
                cur = next_node

        # 因为头节点可能会发生变化，这里使用虚拟头节点
        dummy_head = ListNode(-1)
        dummy_head.next = head

        # 第 1 步：找到前继节点
        pre = dummy_head
        for _ in range(left - 1):
            pre = pre.next

        # 第 2 步：找到后继节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next

        # 第 3 步：截取链表
        left_node = pre.next
        cur = right_node.next
        pre.next = None
        right_node.next = None

        # 第 4 步：反转链表
        reverse_linked_list(left_node)

        # 第 5 步：接回到原来的链表中
        pre.next = right_node
        left_node.next = cur
        return dummy_head.next
