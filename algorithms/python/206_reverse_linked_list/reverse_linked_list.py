"""
206. reverse linked list

https://leetcode.com/problems/reverse-linked-list/

反转链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    """
    iterative
    """
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

    return prev
