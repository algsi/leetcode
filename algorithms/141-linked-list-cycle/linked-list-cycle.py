"""
141. linked list cycle

https://leetcode.com/problems/linked-list-cycle/
https://leetcode-cn.com/problems/linked-list-cycle/

环形链表（判断单链表是否有环）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


def has_cycle(head: ListNode) -> bool:
    """
    快慢指针
    当两个指针都进入环之后，由于两个指针都速度不一样，总是会相遇的

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    if not head or not head.next:
        return False

    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next:
            # 如果链表无环，则 fast 指针一定会先到达末尾
            return False
        slow = slow.next
        fast = fast.next.next
    return True


def has_cycle_2(head: ListNode) -> bool:
    """
    哈希表

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
