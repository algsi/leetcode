"""
234. palindrome linked list

回文链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution1:
    def is_palindrome(self, head: ListNode) -> bool:
        """
        拷贝 + 双指针：将链表中的元素拷贝到数组中，然后使用双指针

        Complexity Analysis
        time complexity: O(N)
        space complexity: O(N)
        """
        while not head:
            return True

        # copy to array
        arr = []
        while head:
            arr.append(head)
            head = head.next

        # dual pointer
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left].val != arr[right].val:
                return False
            left += 1
            right -= 1

        return True


class Solution2:
    """
    1. 找到前半部分链表的尾节点
    2. 反转后半部分链表
    3. 判断是否回文
    4. 恢复链表
    5. 返回结果

    complexity analysis
    time complexity: O(N)
    space complexity: O(1)
    """

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        mid = self.middle(head)
        l2 = mid.next
        mid.next = None  # 断开连接，拆分成两条链表
        l2 = self.reverse(l2)
        return self.internal(head, l2)

    def internal(self, l1: ListNode, l2: ListNode) -> bool:
        """
        l1 的长度最多比 l2 多一个元素
        """
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return not l1 or not l1.next

    @staticmethod
    def middle(head: ListNode) -> ListNode:
        """
        return the middle node of the list
        """
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def reverse(node: ListNode) -> ListNode:
        """
        reverse the list
        """
        prev = None
        cur = node
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
