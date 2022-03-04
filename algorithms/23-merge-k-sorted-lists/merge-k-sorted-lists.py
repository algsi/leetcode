"""
23. merge k sorted lists

合并K个排序链表
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
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


def merge_k_lists_1(lists: List[ListNode]) -> ListNode:
    """
    方法一
    merge list one by one(顺序合并)
    """
    ans = None
    for l in lists:
        ans = merge_two_lists(ans, l)
    return ans


def merge(lists: List[ListNode], lo, hi) -> ListNode:
    """
    merge lists from lo(inclusive) to hi(inclusive)
    """
    if lo == hi:
        return lists[lo]

    # 这一步判断是必要的，避免lists为空列表出现的异常
    if lo > hi:
        return None

    mid = (hi - lo) // 2 + lo

    return merge_two_lists(merge(lists, lo, mid), merge(lists, mid + 1, hi))


def merge_k_lists_2(lists: List[ListNode]) -> ListNode:
    """
    方法二（递归实现）
    merge with divide and conquer(分治合并)
    类似于自底向上归并排序
    """
    return merge(lists, 0, len(lists) - 1)


def merge_k_lists_3(lists: List[ListNode]) -> ListNode:
    """
    方法二（非递归实现）
    merge with divide and conquer(分治合并)
    类似于自底向上归并排序
    """
    amount = len(lists)

    # 归并间隙，成倍增长
    interval = 1

    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists
