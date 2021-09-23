"""
19. remove nth node from end of list

删除链表的倒数第N个节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    两次遍历
    """
    if not head:
        return None
    total = 0  # the number of nodes in this linked list
    cur = head
    while cur:
        total += 1
        cur = cur.next

    # dummy node
    dummy = ListNode(0)
    dummy.next = head
    pre, cur = dummy, head
    target = total - (n - 1)
    count = 1
    while count != target:
        cur = cur.next
        pre = pre.next
        count += 1
    pre.next = cur.next
    return dummy.next


def remove_nth_from_end_2(head: ListNode, n: int) -> ListNode:
    """
    一次遍历：双指针

    第一个指针从列表的开头向前移动 n 步，而第二个指针将从列表的开头出发。
    """
    if not head:
        return None
    # dummy node
    dummy = ListNode(0)
    dummy.next = head
    pre, node1 = dummy, head
    for _ in range(n):
        node1 = node1.next
    node2 = head
    while node1:
        node1 = node1.next
        node2 = node2.next
        pre = pre.next
    pre.next = node2.next
    return dummy.next
