"""
83. remove duplicates from sorted list

删除排序链表中的重复元素
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


def delete_duplicates(head: ListNode) -> ListNode:
    """
    双指针
    """
    if not head:
        return None
    prev = head
    cur = prev.next
    while cur:
        # 一直等待下一个不同的节点出现，但也有可能后面的节点都是一样的，所以需要做额外都处理
        if cur.val != prev.val:
            prev.next = cur
            prev = cur

        cur = cur.next

    # 这一步是需要的，应对 [1,1,2,3,3] 这种情况
    prev.next = None

    return head
