"""
21. merge two sorted lists

合并两个有序链表为一个有序的单链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


def merge_two_lists_1(l1: ListNode, l2: ListNode) -> ListNode:
    """
    递归
    时间复杂度：O(n + m)，其中 n 和 m 分别为两个链表的长度。
    空间复杂度：O(n + m)，其中 n 和 m 分别为两个链表的长度。调用递归函数需要消耗栈空间，栈空间大小取决于递归调用的深度。结束递归时调用函数最多 n + m 次。
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = merge_two_lists_1(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_1(l1, l2.next)
        return l2


def merge_two_lists_2(l1: ListNode, l2: ListNode) -> ListNode:
    """
    迭代：伪头节点的应用
    时间复杂度：O(n + m)
    空间复杂度：O(1)
    """
    dummy = ListNode(-1)
    prev = dummy
    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next

        prev = prev.next

    # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 if l1 is not None else l2

    return dummy.next
