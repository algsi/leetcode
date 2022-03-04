"""
142. linked list cycle ii

https://leetcode.com/problems/linked-list-cycle-ii/
https://leetcode-cn.com/problems/linked-list-cycle-ii/

环形链表 II（给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null）
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


def detect_cycle_1(head: ListNode) -> ListNode:
    """
    哈希表

    如果我们用一个 Set 保存已经访问过的节点，我们可以遍历整个列表并返回第一个出现重复的节点。

    time complexity: O(n)
    space complexity: O(n)
    """
    if head is None:
        return None
    visited = set()
    node = head
    while node is not None:
        if node in visited:
            return node
        else:
            node = node.next

    return None


def detect_cycle_2(head: ListNode) -> ListNode:
    """
    快慢指针 + Floyd

    https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

    首先让两个指针相遇，如果链表没有环则直接返回。相遇之后，停止fast指针，重新启用一个指针指向链表头节点，让这个指针和slow指针同时移动，
    它们会在环的入口相遇。

    time complexity: O(n)
    space complexity: O(1)
    """
    if head is None:
        return
    slow, fast = head, head

    # 先让快慢指针相遇
    while True:
        if not fast or not fast.next:
            return
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Floyd
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow
