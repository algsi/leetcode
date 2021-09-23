"""
143. reorder list

https://leetcode.com/problems/reorder-list/
https://leetcode-cn.com/problems/reorder-list/

重排链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    线性表

    因为链表不支持下标随机访问，所以我们无法随机访问链表中任意位置的元素
    因此比较容易想到的一个方法是，我们利用线性表存储该链表，然后利用线性表可以下标访问的特点，直接按顺序访问指定元素，重建该链表即可。

    complexity analysis
    time analysis: O(N)
    space analysis: O(N)
    """

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        vec = list()
        node = head
        # 遍历链表构建线性表
        while node:
            vec.append(node)
            node = node.next
        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None


class Solution2:
    """
    寻找链表中点 + 链表逆序 + 合并链表

    注意：链表拆分一定要将前半部分的尾节点的 next 指针置为 null

    complexity analysis
    time analysis: O(N)
    space analysis: O(1)
    """

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = self.middle_node(head)
        l2 = mid.next
        mid.next = None  # 两条链表拆分，这一步一定需要
        l2 = self.reverse(l2)
        self.merge(head, l2)

    @staticmethod
    def middle_node(head: ListNode) -> ListNode:
        """
        find the middle node of the list
        """
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def reverse(head: ListNode) -> ListNode:
        """
        reverse the list
        """
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    @staticmethod
    def merge(l1: ListNode, l2: ListNode):
        """
        merge two lists

        交叉合并元素
        """
        while l1 and l2:
            l1_temp = l1.next
            l2_temp = l2.next

            l1.next = l2
            l1 = l1_temp

            l2.next = l1
            l2 = l2_temp
