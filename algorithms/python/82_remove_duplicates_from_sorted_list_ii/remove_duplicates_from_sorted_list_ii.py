"""
82. remove duplicates from sorted list ii

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

删除排序链表中的重复元素 II
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def delete_duplicates(self, head: ListNode) -> ListNode:
        """
        dummy head + 迭代
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev = dummy_head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp = cur.next.next
                # 循环找到该重复序列的尾部
                while temp and temp.val == cur.val:
                    temp = temp.next
                cur = temp
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy_head.next

    def delete_duplicates_2(self, head: ListNode) -> ListNode:
        """
        递归
        """
        if head is None or head.next is None:
            return head
        if head.val != head.next.val:
            # 头部没有重复的节点，递归下一个节点
            head.next = self.delete_duplicates_2(head.next)
            return head
        else:
            # 头部有重复的节点，删除所有头部的重复节点，返回不重复的第一个节点
            while head.next is not None and head.val == head.next.val:
                head = head.next
            return self.delete_duplicates_2(head.next)
