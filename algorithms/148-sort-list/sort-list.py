"""
148. sort list

https://leetcode.com/problems/sort-list/
https://leetcode-cn.com/problems/sort-list/

排序链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:
    """
    自顶向下归并排序

    递归：找到链表的中点，切分，排序，合并

    complexity analysis
    time complexity: O(nlogn)
    space complexity: O(logn) （递归所需的栈空间）
    """

    def sort_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # cut the linked list at the mid index
        # 找到链表中点，可使用快慢双指针
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # cut the linkage
        mid, slow.next = slow.next, None
        # recursive sort
        left, right = self.sort_list(head), self.sort_list(mid)
        return self.merge(left, right)

    @staticmethod
    def merge(head1: ListNode, head2: ListNode) -> ListNode:
        # merge head1 and head2 linked list and return it
        h = dummy_res = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                h.next = head1
                head1 = head1.next
            else:
                h.next = head2
                head2 = head2.next
            h = h.next

        if head1:
            h.next = head1
        elif head2:
            h.next = head2

        return dummy_res.next


class Solution2:
    """
    自底向上归并排序

    complexity analysis
    time complexity: O(nlogn)
    space complexity: O(1)
    """

    def sort_list(self, head: ListNode) -> ListNode:
        if not head:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        dummy_head = ListNode(0)
        dummy_head.next = head
        sub_length = 1
        while sub_length < length:
            prev = dummy_head
            cur = prev.next

            while cur is not None:
                # 第一个 sub list
                head1 = cur
                i = 1
                while i < sub_length and cur.next is not None:
                    cur = cur.next
                    i += 1

                # 第二个 sub list
                head2 = cur.next
                cur.next = None  # must cut the linkage
                i = 1
                cur = head2
                while i < sub_length and cur is not None and cur.next is not None:
                    cur = cur.next
                    i += 1

                # save the next head
                next_head = None
                if cur is not None:
                    next_head = cur.next
                    cur.next = None

                # merge and reconnect
                prev.next = self.merge(head1, head2)
                while prev.next is not None:
                    prev = prev.next

                cur = next_head

            # sub length * 2
            sub_length <<= 1

        return dummy_head.next

    # noinspection DuplicatedCode
    @staticmethod
    def merge(head1: ListNode, head2: ListNode) -> ListNode:
        # merge head1 and head2 linked list and return it
        h = dummy_res = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                h.next = head1
                head1 = head1.next
            else:
                h.next = head2
                head2 = head2.next
            h = h.next

        if head1:
            h.next = head1
        elif head2:
            h.next = head2

        return dummy_res.next
