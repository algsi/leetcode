"""
328. odd even linked list

https://leetcode.com/problems/odd-even-linked-list/
https://leetcode-cn.com/problems/odd-even-linked-list/

奇偶链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    链表分离合并
    """

    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head  # 奇
        even = head.next  # 偶
        even_head = even
        while even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
                even.next = odd.next
                even = even.next
            else:
                break
        odd.next = even_head
        return head
