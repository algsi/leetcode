"""
203. remove linked list elements

https://leetcode.com/problems/remove-linked-list-elements/
https://leetcode-cn.com/problems/remove-linked-list-elements/

移除链表元素
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: ListNode, val: int) -> ListNode:
    dummy_head = ListNode()
    dummy_head.next = head
    cur = dummy_head

    while cur.next is not None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy_head
