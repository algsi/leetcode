"""
2. add two numbers

https://leetcode.com/problems/add-two-numbers/
https://leetcode-cn.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    模拟法
    """
    dummy_head = ListNode()
    node = dummy_head
    carry = 0
    while l1 or l2:
        l1_val, l2_val = 0, 0
        if l1:
            l1_val = l1.val
            l1 = l1.next
        if l2:
            l2_val = l2.val
            l2 = l2.next
        tmp_val = l1_val + l2_val + carry
        node.next = ListNode(tmp_val % 10)
        carry = tmp_val // 10
        node = node.next

    if carry != 0:
        node.next = ListNode(carry)

    return dummy_head.next
