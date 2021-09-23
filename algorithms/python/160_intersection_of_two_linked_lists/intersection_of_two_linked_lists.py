"""
160. intersection of two linked lists

相交链表
"""

"""
编写一个程序，找到两个单链表相交的起始节点。

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: ListNode = None


def get_intersection_node_1(headA: ListNode, headB: ListNode) -> ListNode:
    """
    方法一：暴力法

    时间复杂度：O(m*n)
    空间复杂度：O(1)
    """
    pass


def get_intersection_node_2(headA: ListNode, headB: ListNode) -> ListNode:
    """
    方法一：哈希表法

    遍历链表 A 并将每一个节点的引用存储在哈希表中。然后检查链表 B 中的每一个节点 bi 是否在哈希表中，若在，则 bi 为相交节点

    时间复杂度：O(m+n)
    空间复杂度：O(m)或O(n)
    """
    if headA is None or headB is None:
        return None

    dic = set()
    p = headA
    while p is not None:
        dic.add(p)
        p = p.next
    p = headB
    while p is not None:
        if p in dic:
            return p
        p = p.next

    return None


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    """
    方法三：双指针法
    若两个链表相交，它们的末尾节点必然相同。
    创建两个指针 pA 和 pB，分别初始化为链表 A 和链表 B 的头节点。然后让他们向后逐节点遍历。
    当 pA 到达链表尾部时，将它重定位到链表 B 的头节点；类似的，当 pB 到达链表尾部时，将它重定位到链表 A 的头节点。
    若在某一时刻 pA 和 pB 相遇，则 pA/pB 为相交节点

    下面的代码中，如果两条链表不相交，则到最 p_a 和 p_b 都为 null，那它们就都相等了，此时退出循环，返回null

    时间复杂度：O(m+n)
    空间复杂度：O(1)
    """
    if headA is None or headB is None:
        return None

    p_a, p_b = headA, headB
    while p_a != p_b:
        p_a = headB if p_a is None else p_a.next
        p_b = headA if p_b is None else p_b.next

    return p_a
