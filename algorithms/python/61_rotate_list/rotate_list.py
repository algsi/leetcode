class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next is not None:
            cur = cur.next
            n += 1

        # now cur.next is None
        add = n - k % n
        if add == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret
